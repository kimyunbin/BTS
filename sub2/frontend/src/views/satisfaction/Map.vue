<template>
  <div id="map-wrapper" class="map-wrapper"></div>
</template>

<script>
import * as d3 from 'd3';

const MAP_GEOJSON = require('./do.json'); // json 파일 입력시 해당지역 지도 출력

export default {
  components: {
  },
  props: {
  },
  data() {
    return {
      province: undefined, // 마우스가 지역구 위에 있을 때 정보
    }
  },
  computed: {
  },
  created() {
  },
  mounted() {
    this.drawMap();
  },

  methods: {
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
      const labelLayer = g.append('g').classed('label-layer', true);
      // 도시명이 그려지는 그래픽 노드
      const namesLayer = g.append('g').classed('names-layer', true);

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
        let name = d.path[0]["__data__"].properties["CTP_KOR_NM"];
          console.log(name)
          let url ="http://localhost:8080/";
          //let url ="http://j5c203.p.ssafy.io/";
          if (name === "강원도") {
            location.href =url+"gangwon";
          }
          if (name === "경기도") {
            location.href =url+"gyeonggi";
          }
          if (name === "서울특별시") {
            location.href =url+"seoul";
          }
          if (name === "인천광역시") {
            location.href =url+"incheon";
          }
          if (name === "경상북도") {
            location.href =url+"gyeongbuk";
          }
          if (name === "충청북도") {
            location.href =url+"chungbuk";
          }
          if (name === "세종특별자치시") {
            location.href =url+"sejong";
          }
          if (name === "대전광역시") {
            location.href =url+"daejeon";
          }
          if (name === "충청남도") {
            location.href =url+"chungnam";
          }
          if (name === "대구광역시") {
            location.href =url+"daegu";
          }
          if (name === "울산광역시") {
            location.href =url+"ulsan";
          }
          if (name === "부산광역시") {
            location.href =url+"busan";
          }
          if (name === "경상남도") {
            location.href =url+"gyeongnam";
          }
          if (name === "전라북도") {
            location.href =url+"jeonbuk";
          }
          if (name === "광주광역시") {
            location.href =url+"gwangju";
          }
          if (name === "전라남도") {
            location.href =url+"jeonnam";
          }
          if (name === "제주특별자치도") {
            location.href =url+"jeju";
          }
          
      }

      function mouseover(d){
        // Highlight hovered province
        d3.select(this).style('fill', '#1483ce');
        d3.select(this).style('cursor', 'pointer');
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
          "name":"강원도",
          "lat" : "37.32442222",
          "lon" : "128.3008417"
        },
        {
          "name":"경기도",
          "lat" : "37.43091667",
          "lon" : "127.1876528"

        },
        {
          "name":"서울특별시",
          "lat" : "37.10609444",
          "lon" : "126.9875222"
        },
        {
          "name":"인천광역시",
          "lat" : "37.22384843",
          "lon" : "126.2407617"
        },
        {
          "name":"충청북도",
          "lat" : "36.33243056",
          "lon" : "127.7088306"
        },
        {
          "name":"충청남도",
          "lat" : "36.01836111",
          "lon" : "126.8029083"
        },
        {
          "name":"세종특별자치시",
          "lat" : "36.1200000",
          "lon" : "127.2400000"
        },
        {
          "name":"대전광역시",
          "lat" : "35.84582989",
          "lon" : "127.411381"
        },
        {
          "name":"대구광역시",
          "lat" : "35.33621351",
          "lon" : "128.587702"
        },
        {
          "name":"경상북도",
          "lat" : "35.90975833",
          "lon" : "128.6993639"
        },
        {
          "name":"경상남도",
          "lat" : "34.80703333",
          "lon" : "128.3000000"
        },
        {
          "name":"울산광역시",
          "lat" : "35.08371228",
          "lon" : "129.2728162"
        },
        {
          "name":"부산광역시",
          "lat" : "34.75995278",
          "lon" : "129.0453194"
        },
        {
          "name":"전라북도",
          "lat" : "35.20918889",
          "lon" : "127.1219194"
        },
        {
          "name":"전라남도",
          "lat" : "34.378525",
          "lon" : "126.9391083"
        },
        {
          "name":"광주광역시",
          "lat" : "34.6825164",
          "lon" : "126.8295063"
        },
        {
          "name":"제주특별자치도",
          "lat" : "32.89631111",
          "lon" : "126.4332083"
        },
      ]

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
    fill: #fff;
    stroke: #fff;
    stroke-width: 1px;
  }
}
</style>
