<template>
  <div id="map-wrapper" class="map-wrapper">
    <!-- <div>dkdkdk</div>   -->
    <!-- <v-btn @click="check()">check</v-btn> -->
  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapGetters, mapState } from "vuex";
import { createInstance } from "@/api/index.js";

const MAP_GEOJSON = require('./gangwon.json'); // json 파일 입력시 해당지역 지도 출력

export default {
  components: {
  },
  props: {
  },
  data() {
    return {
      province: undefined, // 마우스가 지역구 위에 있을 때 정보
      items: [],
      names: [],
      cityname: "없음"
    }
  },
  computed: {
    ...mapGetters([
      "SET_SELECT_MAP"
    ]),
    ...mapState([
      "select_map", "satis_area"
    ])
  },
  created() {
    this.store()
    // this.check()
    for(var i=0; i<this.items.length; i++) {
      console.log(this.items[i]["city"])
    }
  },
  mounted() {
    this.drawMap();
  },

  methods: {
    store() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "강원도") {
          this.items.push(this.satis_area[i])
          this.names.push(this.satis_area[i].city)
        }
      }
    },
    check() {
      console.log(this.cityname)
    },
    // 선택된 지역
    selectProvince(province) {
      this.province = province;
    },
    move(city){
      this.$store.dispatch("SET_SELECT_MAP", city).then(()=>{

        const instance = createInstance();
        instance.get("/tour/detail/?code="+ city)
        .then(
            (response) => {
                console.log(response.data);
                this.$store.dispatch("SET_TOUR_DETAIL", response.data).then(()=>{
                  this.$router.replace("/map");
                });
              }
        )
        .catch(() => {
            alert("에러발생!");
          //this.$router.push("/");
        });
              
      });
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
      // 도시명이 그려지는 그래픽 노드
      const namesLayer = g.append('g').classed('names-layer', true);
      const namesLayer2 = g.append('g').classed('names-layer2', true);

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
        .range(['#dbdbdb', '#dbdbdb']);

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
          _this.move(name);
      }

      function mouseover(d){
        let name = d.path[0]["__data__"].properties["SIG_KOR_NM"];
        name = "강원도 " + name
        // arlert(name)
        // Highlight hovered province
        d3.select(this).style('fill', '#1483ce');
        d3.select(this).style('cursor', 'pointer');
        // this.cityname = name
        // alert(this.cityname)
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
        // this.cityname = "";
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
          "lat" : "37.70913611",
          "lon" : "128.8784972"
        },
        {
          "name":"고성군",
          "lat" : "38.32796111",
          "lon" : "128.4251639"
        },
        {
          "name":"동해시",
          "lat" : "37.48193056",
          "lon" : "129.1066333"
        },
        {
          "name":"삼척시",
          "lat" : "37.26708611",
          "lon" : "129.1674889"
        },
        {
          "name":"속초시",
          "lat" : "38.154275",
          "lon" : "128.5541667"
        },
        // {
        //   "name":"양구군",
        //   "lat" : "38.10729167",
        //   "lon" : "127.9922444"
        // },
        {
          "name":"양양군",
          "lat" : "38.02283333",
          "lon" : "128.6213556"
        },
        {
          "name":"영월군",
          "lat" : "37.18086111",
          "lon" : "128.4640194"
        },
        {
          "name":"원주시",
          "lat" : "37.30908333",
          "lon" : "127.9220556"
        },
        {
          "name":"인제군",
          "lat" : "38.06697222",
          "lon" : "128.2586972"
        },
        {
          "name":"정선군",
          "lat" : "37.37780833",
          "lon" : "128.7230861"
        },
        {
          "name":"철원군",
          "lat" : "38.18005556",
          "lon" : "127.4157333"
        },
        {
          "name":"춘천시",
          "lat" : "37.87854167",
          "lon" : "127.7323111"
        },
        {
          "name":"태백시",
          "lat" : "37.12122778",
          "lon" : "128.9879972"
        },
        {
          "name":"평창군",
          "lat" : "37.48791667",
          "lon" : "128.4223528"
        },
        {
          "name":"홍천군",
          "lat" : "37.72442222",
          "lon" : "128.1508417"
        },
        {
          "name":"화천군",
          "lat" : "38.10340833",
          "lon" : "127.7103556"
        },
        {
          "name":"횡성군",
          "lat" : "37.48895833",
          "lon" : "128.1572222"
        },
      ];
      const iconsInfo2 = [
        {
          "name":"양구군",
          "lat" : "38.10729167",
          "lon" : "127.9922444"
        },
      ]
      
      // 아이콘 그리기
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
        .attr("xlink:href",d=> {
          for (let index = 0; index < this.items.length; index++) {
            if (d.name === this.items[index].city) {
              return require(`../../assets/img/만족도/${this.items[index]["score"]}.png`)
            }
          }
        })
        .transition()
        .ease(d3.easeElastic)
        .duration(2000)
        .delay((d, i)=> i * 50)
        .attr('opacity', 1)
        .attr('y',  d=> projection([d.lon, d.lat])[1]-50)

      iconsLayer
        .selectAll('svg')
        .data(iconsInfo2)
        .enter()
        .append("svg:image")
        .attr("width", 60)
        .attr("height", 60)
        .attr('x', d=> projection([d.lon, d.lat])[0]-40)
        .attr('y', d=> projection([d.lon, d.lat])[1]-80)
        .attr('opacity', 1)
        .attr("xlink:href", require("../../assets/img/만족도/5.png"))
        .transition()
        .ease(d3.easeElastic)
        .duration(2000)
        .delay((d, i)=> i * 50)
        .attr('opacity', 1)
        .attr('y',  d=> projection([d.lon, d.lat])[1]-50)

      namesLayer
        .selectAll('text')
        .data(iconsInfo)
        .enter()
        .append('text')
        .attr('x', d=> projection([d.lon, d.lat])[0]-30)
        .attr('y', d=> projection([d.lon, d.lat])[1]-80)
        .text(function(d) {
            return d.name;
        })
        .transition()
        .ease(d3.easeElastic)
        .duration(2000)
        .delay((d, i)=> i * 50)
        .attr('opacity', 1)
        .attr('y',  d=> projection([d.lon, d.lat])[1]-50)

      namesLayer2
        .selectAll('text')
        .data(iconsInfo2)
        .enter()
        .append('text')
        .attr('x', d=> projection([d.lon, d.lat])[0]-30)
        .attr('y', d=> projection([d.lon, d.lat])[1]-80)
        .text(function(d) {
            return d.name;
        })
        .transition()
        .ease(d3.easeElastic)
        .duration(2000)
        .delay((d, i)=> i * 50)
        .attr('opacity', 1)
        .attr('y',  d=> projection([d.lon, d.lat])[1]-50)
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
    fill: #ffff;
    stroke: #ffff;
    stroke-width: 1px;
  }
}
</style>
