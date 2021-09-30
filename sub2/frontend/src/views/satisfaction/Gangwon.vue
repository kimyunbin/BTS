<template>
  <div id="map-wrapper" class="map-wrapper">

  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapState } from "vuex";
import one from "../../assets/img/만족도/1.png"

const MAP_GEOJSON = require('./gangwon.json'); // json 파일 입력시 해당지역 지도 출력

export default {
  components: {
  },
  props: {
  },
  data() {
    return {
      province: undefined, // 마우스가 지역구 위에 있을 때 정보
      items: []
    }
  },
  computed: {
    ...mapState(["satis_area"])
  },
  created() {
    this.store()
    // this.check()
    console.log(this.items)
  },
  mounted() {
    this.drawMap();
  },

  methods: {
    store() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "강원도") {
          this.items.push(this.satis_area[i])
        }
      }
    },
    check() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "철원군") {
          console.log(this.satis_area[i]["city"])
        } else {
          console.log("x")
        }
      }
    },
    // 선택된 지역
    selectProvince(province) {
      this.province = province;
    },
    partyColor(code) {
      let color = null;
      return color;
    },
    drawMap() {
      // 지도정보
      const geojson = MAP_GEOJSON;
      // 지도의 중심점 찾기
      const center = d3.geoCentroid(geojson);

      let centered = undefined;

      // 현재의 브라우저의 크기 계산
      const divWidth = document.getElementById("map-wrapper").clientWidth;
      const width = (divWidth < 1000) ? divWidth * 0.9 : 1000;
      const height = width * 1;

      // 지도를 그리기 위한 svg 생성
      const svg = d3
      // .select('.d3')
        .select('.map-wrapper')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

      // 배경 그리기
      const background = svg.append('rect')
        .attr('class', 'background')
        .attr('width', width)
        .attr('height', height)

      // 지도가 그려지는 그래픽 노드(g) 생성
      const g = svg.append('g');
      // const effectLayer = g.append('g').classed('effect-layer', true);
      // 지도가 그려지는 그래픽 노드
      const mapLayer = g.append('g').classed('map-layer', true);
      // 아이콘이 그려지는 그래픽 노드
      const iconsLayer = g.append('g').classed('icons-layer', true);

      // 지도의 출력 방법을 선택(메로카토르)
      let projection = d3.geoMercator()
        .scale(1)
        .translate([0, 0]); 

      // svg 그림의 크기에 따라 출력될 지도의 크기를 다시 계산
      const path = d3.geoPath().projection(projection);
      const bounds = path.bounds(geojson);
      const widthScale = (bounds[1][0] - bounds[0][0]) / width; 
      const heightScale = (bounds[1][1] - bounds[0][1]) / height; 
      const scale = 0.95 / Math.max(widthScale, heightScale);
      const xoffset = width/2 - scale * (bounds[1][0] + bounds[0][0]) /2 + 0; 
      const yoffset = height/2 - scale * (bounds[1][1] + bounds[0][1])/2 + 0; 
      const offset = [xoffset, yoffset];
      projection.scale(scale).translate(offset);

      const color = d3.scaleLinear()
        .domain([1, 20])
        .clamp(true)
        // .range(['#08304b', '#08304b']);
        .range(['#595959', '#595959']);

      const _this = this;
      // Get province color
      function fillFn(d){

        const pcolor = _this.partyColor(d.properties.SGG_Code);
        if(pcolor) {
          return pcolor;
        }

        return color(nameLength(d));
      }

      function clicked(d) {
        
        let name = d.path[0]["__data__"].properties["SIG_KOR_NM"];
        name = "강원도 " + name
        console.log(name)
      }

      function mouseover(d){
        // Highlight hovered province
        d3.select(this).style('fill', '#1483ce');
        // d3.select(this).style('fill', '#004EA2');
        if(d) {
          _this.selectProvince(d.properties);
        }
      }

      function mouseout(d){
        _this.selectProvince(undefined);
        // Reset province color
        mapLayer.selectAll('path')
          .style('fill', (d) => {
            return centered && d===centered ? '#D5708B' : fillFn(d);
          });
      }

      // Get province name length
      function nameLength(d){
        const n = nameFn(d);
        return n ? n.length : 0;
      }

      // Get province name
      function nameFn(d){
        return d && d.properties ? d.properties.name : null;
      }

      // Add background
      background
        .on('click', clicked);

      // 지도 그리기
      mapLayer
        .selectAll('path')
        .data(geojson.features)
        .enter().append('path') 
        .attr('d', path)
        .attr('vector-effect', 'non-scaling-stroke')
        .style('fill', fillFn)
        .on('mouseover', mouseover)
        .on('mouseout', mouseout)
        .on('click', clicked);

      const iconsInfo = [
        {
          "name":"강릉시",
          "lat" : "37.74913611",
          "lon" : "128.8784972"
        },
        {
          "name":"고성군",
          "lat" : "38.37796111",
          "lon" : "128.4701639"
        },
        {
          "name":"동해시",
          "lat" : "37.52193056",
          "lon" : "129.1166333"
        },
        {
          "name":"삼척시",
          "lat" : "37.44708611",
          "lon" : "129.1674889"
        },
        {
          "name":"속초시",
          "lat" : "38.204275",
          "lon" : "128.5941667"
        },
        {
          "name":"양구군",
          "lat" : "38.10729167",
          "lon" : "127.9922444"
        },
        {
          "name":"양양군",
          "lat" : "38.07283333",
          "lon" : "128.6213556"
        },
        {
          "name":"영월군",
          "lat" : "37.18086111",
          "lon" : "128.4640194"
        },
        {
          "name":"원주시",
          "lat" : "37.33908333",
          "lon" : "127.9220556"
        },
        {
          "name":"인제군",
          "lat" : "38.06697222",
          "lon" : "128.1726972"
        },
        {
          "name":"정선군",
          "lat" : "37.37780833",
          "lon" : "128.6630861"
        },
        {
          "name":"철원군",
          "lat" : "38.14405556",
          "lon" : "127.3157333"
        },
        {
          "name":"춘천시",
          "lat" : "37.87854167",
          "lon" : "127.7323111"
        },
        {
          "name":"태백시",
          "lat" : "37.16122778",
          "lon" : "128.9879972"
        },
        {
          "name":"평창군",
          "lat" : "37.36791667",
          "lon" : "128.3923528"
        },
        {
          "name":"홍천군",
          "lat" : "37.69442222",
          "lon" : "127.8908417"
        },
        {
          "name":"화천군",
          "lat" : "38.10340833",
          "lon" : "127.7103556"
        },
        {
          "name":"횡성군",
          "lat" : "37.48895833",
          "lon" : "127.9872222"
        },
      ];

      // 아이콘 그리기
      if(this.items[0]["score"] === 10) {
        iconsLayer
          .selectAll('svg')
          .data(iconsInfo)
          .enter()
          .append("svg:image")
          .attr("width", 60)
          .attr("height", 60)
          .attr('x', d=> projection([d.lon, d.lat])[0]-40)
          .attr('y', d=> projection([d.lon, d.lat])[1]-80)
          .attr('opacity', 1)
          .attr("xlink:href", require("../../assets/img/만족도/1.png"))
          // .on('click', d => {
          //   console.log(d)
          // })
          .transition()
          .ease(d3.easeElastic)
          .duration(2000)
          .delay((d, i)=> i * 50)
          .attr('opacity', 1)
          .attr('y',  d=> projection([d.lon, d.lat])[1]-30)
      } else {
        iconsLayer
          .selectAll('svg')
          .data(iconsInfo)
          .enter()
          .append("svg:image")
          .attr("width", 60)
          .attr("height", 60)
          .attr('x', d=> projection([d.lon, d.lat])[0]-40)
          .attr('y', d=> projection([d.lon, d.lat])[1]-80)
          .attr('opacity', 1)
          .attr("xlink:href", require("../../assets/img/만족도/1.png"))
          // .on('click', d => {
          //   console.log(d)
          // })
          .transition()
          .ease(d3.easeElastic)
          .duration(2000)
          .delay((d, i)=> i * 50)
          .attr('opacity', 1)
          .attr('y',  d=> projection([d.lon, d.lat])[1]-30)

      }

    }
  }
}

</script>

<style lang="scss" scope>
.map-wrapper {
  position:relative;
  text-align: center;

  .province-title {
    position: absolute;
    top: 10px;
    left: 40px;
    width: 600px;
    color: white;
    z-index: 100;
    pointer-events: none;
    font-size: 0.9rem;
  }
  .province-info {
    // background: white;
    position: absolute;
    color: white;
    top: 50px;
    right: 60px;
    width: 600px;
    height: 500px;
    z-index: 101;
    font-size: 0.9rem;
    pointer-events: none;
  }
  .province-state {
    // background: white;
    position: absolute;
    color: white;
    bottom: 200px;
    right: 10px;
    width: 300px;
    z-index: 102;
    pointer-events: none;
  }
  .province-summary {
    // background: white;
    position: absolute;
    color: white;
    bottom: 10px;
    right: 10px;
    width: 300px;
    z-index: 103;
    pointer-events: none;
  }
  .province-state > ul, .province-summary > ul {
    list-style: none;
  }
  .background {
    /* fill: #021019; */
    fill: transparent;
    pointer-events: all;
  }
  .map-layer {
    fill: #08304b;
    stroke: #021019;
    stroke-width: 1px;
  }
}
</style>
