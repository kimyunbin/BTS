<template>
  <div id="map-wrapper" class="map-wrapper">

  </div>
</template>

<script>
import * as d3 from 'd3';
import { mapGetters, mapState } from "vuex";
import { createInstance } from "@/api/index.js";

const MAP_GEOJSON = require('./gyeonggi.json'); // json 파일 입력시 해당지역 지도 출력

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
    ...mapGetters([
      "SET_SELECT_MAP","SET_TOUR_DETAIL"
    ]),
    ...mapState([
      "select_map", "satis_area"
    ])
  },
  created() {
    this.store()
    console.log(this.items.length)
    // this.check()
    // for (let i=0; this.items.length; i++) {
    //   console.log(this.items[i]["city"])
    // }
  },
  mounted() {
    this.drawMap();
  },

  methods: {
    store() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "경기도") {
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
    move(city){
      this.$store.dispatch("SET_SELECT_MAP", city).then(()=>{

        const instance = createInstance();
        instance.get("/tour/detail?code="+ city)
        .then(
            (response) => {
                console.log(response.data);
                this.$store.dispatch("SET_TOUR_DETAIL", response.data).then(()=>{
                  this.$router.replace("/map");
                });
              }
        )
        .catch(error => {
            console.log(error);
          //this.$router.push("/");
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
        name = "경기도 " + name
        console.log(name)
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
          "name":"가평군",
          "lon" : "127.4617778",
          "lat" : "37.82883056"
        },
        {
          "name":"고양시",
          "lon" : "126.8470556",
          "lat" : "37.62590833"
        },
        // {
        //   "name":"과천시",
        //   "lon" : "126.9898",
        //   "lat" : "37.42637222"
        // },
        {
          "name":"광명시",
          "lon" : "126.8667083",
          "lat" : "37.43575"
        },
        {
          "name":"광주시",
          "lon" : "127.3077861",
          "lat" : "37.39450556"
        },
        {
          "name":"구리시",
          "lon" : "127.1418639",
          "lat" : "37.581625"
        },
        // {
        //   "name":"군포시",
        //   "lon" : "126.9375",
        //   "lat" : "37.35865833"
        // },
        {
          "name":"김포시",
          "lon" : "126.6227778",
          "lat" : "37.67245833"
        },
        {
          "name":"남양주시",
          "lon" : "127.2686333",
          "lat" : "37.63317778"
        },
        {
          "name":"동두천시",
          "lon" : "127.0876528",
          "lat" : "37.90091667"
        },
        {
          "name":"부천시",
          "lon" : "126.796",
          "lat" : "37.4935917"
        },
        {
          "name":"성남시",
          "lon" : "127.1477194",
          "lat" : "37.38749167"
        },
        {
          "name":"수원시",
          "lon" : "127.0122222",
          "lat" : "37.30101111"
        },
        {
          "name":"시흥시",
          "lon" : "126.8050778",
          "lat" : "37.37731944"
        },
        {
          "name":"안산시",
          "lon" : "126.8468194",
          "lat" : "37.29851944"
        },
        {
          "name":"안성시",
          "lon" : "127.2818444",
          "lat" : "37.005175"
        },
        {
          "name":"안양시",
          "lon" : "126.9533556",
          "lat" : "37.3597"
        },
        {
          "name":"양주시",
          "lon" : "127.0478194",
          "lat" : "37.78245"
        },
        {
          "name":"양평군",
          "lon" : "127.5598861",
          "lat" : "37.48893611"
        },
        {
          "name":"여주시",
          "lon" : "127.6396222",
          "lat" : "37.29535833"
        },
        {
          "name":"연천군",
          "lon" : "127.0770667",
          "lat" : "38.09336389"
        },
        {
          "name":"오산시",
          "lon" : "127.0796417",
          "lat" : "37.14691389"
        },
        {
          "name":"용인시",
          "lon" : "127.2038444",
          "lat" : "37.23147778"
        },
        // {
        //   "name":"의왕시",
        //   "lon" : "126.9703889",
        //   "lat" : "37.34195"
        // },
        {
          "name":"의정부시",
          "lon" : "127.0858417",
          "lat" : "37.69828889"
        },
        {
          "name":"이천시",
          "lon" : "127.4732194",
          "lat" : "37.20343611"
        },
        {
          "name":"파주시",
          "lon" : "126.8019528",
          "lat" : "37.80708333"
        },
        {
          "name":"평택시",
          "lon" : "127.0046556",
          "lat" : "36.98943889"
        },
        {
          "name":"포천시",
          "lon" : "127.2524194",
          "lat" : "37.92215556"
        },
        {
          "name":"하남시",
          "lon" : "127.217",
          "lat" : "37.49649722"
        },
        {
          "name":"화성시",
          "lon" : "126.8935306",
          "lat" : "37.14681667"
        },
      ];

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
