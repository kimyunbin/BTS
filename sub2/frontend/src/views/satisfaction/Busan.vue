<template>
  <div id="map-wrapper" class="map-wrapper">

  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapGetters, mapState } from "vuex";
import { createInstance } from "@/api/index.js";
const MAP_GEOJSON = require('./busan.json'); // json 파일 입력시 해당지역 지도 출력

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
      cityname: ""
    }
  },
  computed:{
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
    // for(var i=0; i<this.items.length; i++) {
    //   console.log(this.items[i]["city"])
    // }
    console.log(this.items)
  },
  mounted() {
    this.drawMap();
    
  },

  methods: {
    store() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "부산광역시") {
          this.items.push(this.satis_area[i])
          this.names.push(this.satis_area[i].city)
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
    move(city){
      this.$store.dispatch("SET_SELECT_MAP", city).then(()=>{
        const instance = createInstance();
      
        instance.get("/tour/detail/?code="+ city)
        .then(
            (response) => {
                  console.log(response);
                  this.$store.dispatch("SET_TOUR_DETAIL", response.data).then(()=>{
                  //const image_instance = imageInstance();
                  this.$router.replace("/map");
                });
              }
        )
        .catch(error => {
          // console.log(error);
        });
              
      });
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
        .range(['#dbdbdb', '#dbdbdb']);

      const _this = this;

      //
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
        name = "부산광역시 " + name
        console.log(name);
        _this.move(name);
      }

      function mouseover(d){
        // Highlight hovered province
        d3.select(this).style('fill', '#1483ce');
        d3.select(this).style('cursor', 'pointer');
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
          "name":"강서구",
          "lat" : "35.14916389",
          "lon" : "128.9129083"
        },
        {
          "name":"금정구",
          "lat" : "35.25007778",
          "lon" : "129.0943194"
        },
        {
          "name":"남구",
          "lat" : "35.11340833",
          "lon" : "129.0965"
        },
        {
          "name":"동구",
          "lat" : "35.11589444",
          "lon" : "129.049175"
        },
        {
          "name":"동래구",
          "lat" : "35.19687222",
          "lon" : "129.0858556"
        },
        {
          "name":"부산진구",
          "lat" : "35.15995278",
          "lon" : "129.0453194"
        },
        {
          "name":"북구",
          "lat" : "35.22418056",
          "lon" : "129.032475"
        },
        {
          "name":"사하구",
          "lat" : "35.08142778",
          "lon" : "128.9770417"
        },
        {
          "name":"서구",
          "lat" : "35.09483611",
          "lon" : "129.0263778"
        },
        {
          "name":"수영구",
          "lat" : "35.15246667",
          "lon" : "129.118375"
        },
        {
          "name":"연제구",
          "lat" : "35.17018611",
          "lon" : "129.092075"
        },
        // {
        //   "name":"영도구",
        //   "lat" : "35.08811667",
        //   "lon" : "129.0701861"
        // },
        // {
        //   "name":"중구",
        //   "lat" : "35.10321667",
        //   "lon" : "129.0345083"
        // },
        {
          "name":"해운대구",
          "lat" : "35.19001944",
          "lon" : "129.1658083"
        },
        {
          "name":"기장군",
          "lat" : "35.28877541",
          "lon" : "129.2122873"
        },
      ];
      const iconsInfo2 = [
        {
          "name":"사상구",
          "lat" : "35.14946667",
          "lon" : "128.9933333"
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
