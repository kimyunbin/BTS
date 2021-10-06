<template>
<div>
  <div id="map-wrapper" class="map-wrapper">
    <div class="text">
      <p>해당 지역은</p>&nbsp;
      <p>
        <span class="word wisteria">다시 뛰는</span>
        <span class="word belize">공정도시</span>
        <span class="word pomegranate">서울</span>
    <!--     <span class="word green">beautiful.</span> -->
    <!--     <span class="word midnight">cheap.</span> -->
      </p>
    </div>
  </div>
  <div class="tablebox">
    <img class="table" src="@/assets/img/만족도/table.png" alt="table">
  </div>
</div>
</template>

<script>
import * as d3 from 'd3';
import { mapGetters, mapState } from "vuex";
import { createInstance } from "@/api/index.js";

const MAP_GEOJSON = require('./seoul.json'); // json 파일 입력시 해당지역 지도 출력

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
      cityname: "",
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
    
    var words = document.getElementsByClassName('word');
    var wordArray = [];
    var currentWord = 0;

    words[currentWord].style.opacity = 1;
    for (var i = 0; i < words.length; i++) {
      splitLetters(words[i]);
    }

    function changeWord() {
      var cw = wordArray[currentWord];
      var nw = currentWord == words.length-1 ? wordArray[0] : wordArray[currentWord+1];
      for (var i = 0; i < cw.length; i++) {
        animateLetterOut(cw, i);
      }
      
      for (var i = 0; i < nw.length; i++) {
        nw[i].className = 'letter behind';
        nw[0].parentElement.style.opacity = 1;
        animateLetterIn(nw, i);
      }
      
      currentWord = (currentWord == wordArray.length-1) ? 0 : currentWord+1;
    }

    function animateLetterOut(cw, i) {
      setTimeout(function() {
        cw[i].className = 'letter out';
      }, i*80);
    }

    function animateLetterIn(nw, i) {
      setTimeout(function() {
        nw[i].className = 'letter in';
      }, 340+(i*80));
    }

    function splitLetters(word) {
      var content = word.innerHTML;
      word.innerHTML = '';
      var letters = [];
      for (var i = 0; i < content.length; i++) {
        var letter = document.createElement('span');
        letter.className = 'letter';
        letter.innerHTML = content.charAt(i);
        word.appendChild(letter);
        letters.push(letter);
      }
      
      wordArray.push(letters);
    }

    changeWord();
    setInterval(changeWord, 4000);
  },

  methods: {
    store() {
      for(var i=0; i < this.satis_area.length; i++) {
        if(this.satis_area[i]["state"] === "서울특별시") {
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
                console.log(response.data);
                this.$store.dispatch("SET_TOUR_DETAIL", response.data).then(()=>{
                  this.$router.push("/map");
                });
              }
        )
        .catch(() => {
            // alert("에러발생!");
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
        
        let name = d.path[0]["__data__"].properties["SIG_KOR_NM"].replace("시","시 ");
        name = "서울특별시 " + name
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
          "name":"강남구",
          "lat" : "37.494575",
          "lon" : "127.0585556"
        },
        {
          "name":"강동구",
          "lat" : "37.53736667",
          "lon" : "127.1458639"
        },
        {
          "name":"강북구",
          "lat" : "37.63695556",
          "lon" : "127.0077194"
        },
        {
          "name":"강서구",
          "lat" : "37.54815556",
          "lon" : "126.851675"
        },
        {
          "name":"관악구",
          "lat" : "37.45938611",
          "lon" : "126.9538444"
        },
        {
          "name":"광진구",
          "lat" : "37.53573889",
          "lon" : "127.0845333"
        },
        {
          "name":"구로구",
          "lat" : "37.49265",
          "lon" : "126.8595972"
        },
        {
          "name":"금천구",
          "lat" : "37.44910833",
          "lon" : "126.9041972"
        },
        {
          "name":"노원구",
          "lat" : "37.64146111",
          "lon" : "127.0783889"
        },
        {
          "name":"도봉구",
          "lat" : "37.66583333",
          "lon" : "127.0395222"
        },
        {
          "name":"동대문구",
          "lat" : "37.571625",
          "lon" : "127.0621417"
        },
        // {
        //   "name":"동작구",
        //   "lat" : "37.50965556",
        //   "lon" : "126.941575"
        // },
        {
          "name":"마포구",
          "lat" : "37.56070556",
          "lon" : "126.9005306"
        },
        {
          "name":"서대문구",
          "lat" : "37.57636667",
          "lon" : "126.9388972"
        },
        {
          "name":"서초구",
          "lat" : "37.48078611",
          "lon" : "127.0148111"
        },
        {
          "name":"성동구",
          "lat" : "37.54061111",
          "lon" : "127.03955"
        },
        {
          "name":"성북구",
          "lat" : "37.59638333",
          "lon" : "127.0203333"
        },
        {
          "name":"송파구",
          "lat" : "37.51175556",
          "lon" : "127.1079306"
        },
        {
          "name":"양천구",
          "lat" : "37.51423056",
          "lon" : "126.8587083"
        },
        {
          "name":"영등포구",
          "lat" : "37.51361111",
          "lon" : "126.9083417"
        },
        {
          "name":"용산구",
          "lat" : "37.52609444",
          "lon" : "126.9875222"
        },
        {
          "name":"은평구",
          "lat" : "37.60996944",
          "lon" : "126.9312417"
        },
        {
          "name":"종로구",
          "lat" : "37.57837778",
          "lon" : "126.9816417"
        },
        {
          "name":"중구",
          "lat" : "37.55100278",
          "lon" : "126.9996417"
        },
        // {
        //   "name":"중랑구",
        //   "lat" : "37.60380556",
        //   "lon" : "127.0947778"
        // },
      ];
      const iconInfo2 = [
        {
          "name":"동작구",
          "lat" : "37.49565556",
          "lon" : "126.961575"
        },
        {
          "name":"중랑구",
          "lat" : "37.59380556",
          "lon" : "127.0947778"
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
        .data(iconInfo2)
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
        .data(iconInfo2)
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

<style lang="scss" scoped>
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
.tablebox {
  display: flex;
  text-align: center;
}
.table {
  // margin-top: 3rem;
  height: 8rem;
  width: 40rem;
  margin:0 auto;  
}
.description {
  margin-top: 3rem;
}

@import url(https://fonts.googleapis.com/css?family=Open+Sans:600);

.text {
  font-family: 'Open Sans', sans-serif;
  font-weight: 600;
  font-size: 40px;
  // position: absolute;
  // width: 450px;
  // left: 50%;
  margin-left: -8rem;
  // height: 40px;
  top: 50%;
  margin-top: 2.5rem;
}

p {
  display: inline-block;
  vertical-align: top;
  margin: 0;
}

.word {
  position: absolute;
  width: 220px;
  opacity: 0;
}

.letter {
  display: inline-block;
  position: relative;
  float: left;
  transform: translateZ(25px);
  transform-origin: 50% 50% 25px;
}

.letter.out {
  transform: rotateX(90deg);
  transition: transform 0.32s cubic-bezier(0.55, 0.055, 0.675, 0.19);
}

.letter.behind {
  transform: rotateX(-90deg);
}

.letter.in {
  transform: rotateX(0deg);
  transition: transform 0.38s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.wisteria {
  color: #8e44ad;
}

.belize {
  color: #2980b9;
}

.pomegranate {
  color: #c0392b;
}

.green {
  color: #16a085;
}

.midnight {
  color: #2c3e50;
}
</style>
