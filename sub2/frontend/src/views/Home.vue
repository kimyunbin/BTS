<template>
  <div id="app">
    <br>
    <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
      <v-btn
        :to="'/keyword'"
        color="primary"
        elevation="3"
        large
        class="justify-center"
      >키워드검색&nbsp;<i class="fas fa-plus"></i>
      </v-btn>

      <v-btn
        @click="checkOtherRoad()"
        color="primary"
        elevation="3"
        large
        class="justify-center"
      >다른사람경로보기&nbsp;<i class="fas fa-plus"></i>
      </v-btn>
    </v-layout>

    <ul class="slides">
    <input type="radio" name="radio-btn" id="img-1" checked />
    <li class="slide-container">
    <div class="slide">
      <a href="/satisfactionmap">
      <img src="https://i.ibb.co/PFJwzf5/06.jpg" /></a>
    </div>
    <div class="nav">
      <label for="img-6" class="prev">&#x2039;</label>
      <label for="img-2" class="next">&#x203a;</label>
    </div>
    </li>

    <input type="radio" name="radio-btn" id="img-2" />
    <li class="slide-container">
        <div class="slide">
          <a href="/satisfactionmap">
          <img src="https://i.ibb.co/Z6T3bLs/image.jpg" /></a>
        </div>
    <div class="nav">
      <label for="img-1" class="prev">&#x2039;</label>
      <label for="img-3" class="next">&#x203a;</label>
    </div>
    </li>

    <input type="radio" name="radio-btn" id="img-3" />
    <li class="slide-container">
        <div class="slide">
          <a href="/satisfactionmap">
          <img src="https://i.ibb.co/x5MCb10/image.jpg" /></a>
        </div>
    <div class="nav">
      <label for="img-2" class="prev">&#x2039;</label>
      <label for="img-4" class="next">&#x203a;</label>
    </div>
    </li>

    <input type="radio" name="radio-btn" id="img-4" />
    <li class="slide-container">
        <div class="slide">
          <a href="/satisfactionmap">
          <img src="https://i.ibb.co/qBfG2mk/image.jpg" /></a>
        </div>
    <div class="nav">
      <label for="img-3" class="prev">&#x2039;</label>
      <label for="img-5" class="next">&#x203a;</label>
    </div>
    </li>

    <input type="radio" name="radio-btn" id="img-5" />
    <li class="slide-container">
        <div class="slide">
          <a href="/satisfactionmap">
          <img src="https://i.ibb.co/dJ1Kt0H/image.jpg" /></a>
        </div>
    <div class="nav">
      <label for="img-4" class="prev">&#x2039;</label>
      <label for="img-6" class="next">&#x203a;</label>
    </div>
    </li>

    <input type="radio" name="radio-btn" id="img-6" />
    <li class="slide-container">
        <div class="slide">
          <a href="/satisfactionmap">
          <img src="https://i.ibb.co/WtCgpYM/image.jpg" /></a>
        </div>
    <div class="nav">
      <label for="img-5" class="prev">&#x2039;</label>
      <label for="img-1" class="next">&#x203a;</label>
    </div>
    </li>

    <li class="nav-dots">
      <label for="img-1" class="nav-dot" id="img-dot-1"></label>
      <label for="img-2" class="nav-dot" id="img-dot-2"></label>
      <label for="img-3" class="nav-dot" id="img-dot-3"></label>
      <label for="img-4" class="nav-dot" id="img-dot-4"></label>
      <label for="img-5" class="nav-dot" id="img-dot-5"></label>
      <label for="img-6" class="nav-dot" id="img-dot-6"></label>
    </li>
</ul>

    <div id="demo">
      <div id="slider">
      <input checked="" type="radio" name="slider" id="slide1" selected="false">
      <input type="radio" name="slider" id="slide2" selected="false">
      <input type="radio" name="slider" id="slide3" selected="false">
      <input type="radio" name="slider" id="slide4" selected="false">
      <div id="slides">
        <div id="overflow">
          <div class="inner">
            <article v-for="(item,i) in items2" :key="i" class="slide">
              <div class="image-container">
                <a :href="item.src">
                <img :src="item.img" alt="item.title" style="margin-bottom:10px"/>
                </a>
              </div>
              <p><br></p>
              <div class="title" style="padding-top:5px">{{item.title}}</div>
              
            </article>
          </div> <!-- .inner -->
        </div> <!-- #overflow -->
      </div>
      <label for="slide1"></label>
      <label for="slide2"></label>
      <label for="slide3"></label>
      <label for="slide4"></label>
    </div>
  </div>
    <br><br><br>
    <h1><b>차범희님을 위한 추천 여행지역</b></h1>
    <br>
    <section>

      <vue-horizontal-list :items="items2" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>

      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>다른 유저가 갔던 여행 경로 추천</b></h1>
    <br>
    <section>
      <v-layout row justify-center align-center wrap class="mt-4 pt-2" v-if="other_road.length>2">
        <v-card @click="setDetailRoad(0)" hover>
          <div id="map" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[0][0].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0][0].name}}의 경로</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover>
          <div id="map2" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[1][0].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[1][0].name}}</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover>
          <div id="map3" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[2][0].title}}</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[2][0].name}}의 경로</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;
      </v-layout>
    </section>



      <!-- <v-btn round dark @click="move('최신')" v-b-tooltip.hover title="click!" >
          최신
      </v-btn>
      <v-btn round dark @click="move('아이들과')" v-b-tooltip.hover title="click!" >
          아이들과
      </v-btn>
      <v-btn round  dark @click="move('커플/신혼')" v-b-tooltip.hover title="click!" >
          커플/신혼
      </v-btn>
      <v-btn round  dark @click="move('남자끼리')" v-b-tooltip.hover title="click!" >
          남자끼리
      </v-btn>
      <v-btn round  dark @click="move('여자끼리')" v-b-tooltip.hover title="click!" >
          여자끼리
      </v-btn> -->
      <!-- <section style="">
      <vue-horizontal-list :items="other_road" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <OtherRoad
            :road="item"
          />
        </template>
      </vue-horizontal-list>
    </section> -->

    <!-- <section>
      <OtherRoad
        v-for="(road, idx) in other_road"
        :key="idx"
        :road="road"
      ></OtherRoad>
    </section> -->

    <br>
    <br>
    <h1><b>남자를 위한 추천 여행지역</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="gender_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>다른 유저가 추천하는 여행지역</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="traveler_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>예산 추천 여행지역</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="budget_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>동행자 추천 여행지역</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="companion_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>
  </div>
</template>

<script>
import VueHorizontalList from "vue-horizontal-list";
import PlaceComponent from "@/components/PlaceComponent";
import { mapGetters, mapState } from "vuex";

export default{
  name: "ServeDev",
  components: {
    VueHorizontalList,
    PlaceComponent,
    
  },
  computed:{
    ...mapGetters([
      "other_road","SET_SELECT_ROAD"
    ]),
    ...mapState([
      "is_login", "user_info", "gender_recom_area", "traveler_recom_area",
      "budget_recom_area", "companion_recom_area"
    ])
  },
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();

      $(document).ready(function(){
      $('.slider').slider();
    });
  },
  data() {
    return {
      swiperOption: {
          slidesPerView: 'auto',
          spaceBetween: 30,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          }
      },
      items2 : [
        {
          src:"/satisfactionmap",
          title: '함양 용추폭포',
          img: "https://i.ibb.co/Sc2d57d/image.jpg",
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex arcu, fringilla in urna quis, ultrices efficitur neque. Morbi lacinia arcu tellus, a imperdiet'
        }, 
        {
          src:"/satisfactionmap",
          title: '단양 만천하스카이워크',
          img: "https://i.ibb.co/D40Hy4z/image.jpg",
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex arcu, fringilla in urna quis, ultrices efficitur neque. Morbi lacinia arcu tellus, a imperdiet'
        }, 
        {
          src:"/satisfactionmap",
          title: '영천 팔공산 도립공원',
          img: "https://i.ibb.co/p43Ckf9/image.jpg",
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex arcu, fringilla in urna quis, ultrices efficitur neque. Morbi lacinia arcu tellus, a imperdiet'
        }, 
        {
          src:"/satisfactionmap",
          title: '소양강스카이워크',
          img: "https://i.ibb.co/Cv4fSBn/image.jpg",
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex arcu, fringilla in urna quis, ultrices efficitur neque. Morbi lacinia arcu tellus, a imperdiet'
        }
      ],
      options: {
        item: {
          padding: -20
        },
        map:{
          padding: -20
        },
        responsive: [
          { end: 576, size: 1 },
          { start: 576, end: 768, size: 2 },
          { start: 768, end: 992, size: 3 },
          { size: 4 },
        ],
        list: {

          windowed: 1200,
          padding: 30,
        },
        position: {
          start: 0,
        },
        autoplay: { play: false, repeat: true, speed: 2400 },
        hover:{
          cursor:"pointer"
        }
      },
    
      
      items: [
        { id:"1", title: "부산", content: "Content item with description", src: "https://i.ibb.co/sv0Cqg1/image.jpg"},
        { id:"2", title: "대구", content: "Content item with description", src: "https://i.ibb.co/KmtrYTf/image.jpg"},
        { id:"3", title: "서울", content: "Content item with description", src: "https://i.ibb.co/w6cC5MT/image.jpg"},
        { id:"4", title: "여수", content: "Content item with description", src: "https://i.ibb.co/60yjckh/image.jpg"},
        { id:"5", title: "의정부", content: "Content item with description", src: "https://i.ibb.co/Z24FjMD/image.jpg"},
        { id:"6", title: "전주", content: "Content item with description", src: "https://i.ibb.co/0V3grZZ/image.jpg"},
        { id:"7", title: "강원", content: "Content item with description", src: "https://i.ibb.co/kBjW0Wg/image.jpg"},
        { id:"8", title: "화성", content: "Content item with description", src: "https://i.ibb.co/StjhL5X/image.png"},
        { id:"9", title: "제주", content: "Content item with description", src: "https://i.ibb.co/gWBNgwm/image.jpg"},
      ],
      items2: [],
      genderItems: [],
      username: '',
    };
  },
  created() {
    this.$store.dispatch("GET_RECOMMEND_AREA")
    .then(()=>{
     this.items2 =  this.$store.state.recom_area
    })
    this.$store.dispatch("GET_OTHER_RECOMMEND_AREA")

  },

  methods: {
    check(){
      console.log(this.is_login);
      console.log(this.other_road);
    },
    setDetailRoad(num){
      this.$store.dispatch("SET_SELECT_ROAD", this.other_road[num]).then(()=>{
        this.$router.replace("/otherroad");
      });
    },
    checkOtherRoad(){
      console.log(this.other_road);
      //console.log(this.other_road[1].length);
    },
    addKakaoMapScript() {
      const script = document.createElement("script");

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=2308e0069ab87daa299bf6d8b3db30e6";
      document.head.appendChild(script);
    },
    initMap() {
      var container = document.getElementById("map");
      var container2 = document.getElementById("map2");
      var container3 = document.getElementById("map3");
      var lat = [];
      var lng = [];
      for(var j = 0; j < this.other_road.length; j++){
        lat[j] = 0;
        lng[j] = 0;
      }
      for(var j = 0; j < this.other_road.length; j++){
        //console.log(lat[j]);
        //console.log(lng[j]);
        for (var i = 0; i < this.other_road[j].length; i++) {
          lat[j] +=  parseFloat(this.other_road[j][i].lat);
          lng[j] +=  parseFloat(this.other_road[j][i].lng);
          //console.log(lat[j]);
          //console.log(lng[j]);
        }
        lat[j] /= this.other_road[j].length;
        lng[j] /= this.other_road[j].length;

      }


      var options = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[0], lat[0]), //지도의 중심좌표.
        level: 8 //지도의 레벨(확대, 축소 정도)
      };

      var options2 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[1], lat[1]), //지도의 중심좌표.
        level: 8 //지도의 레벨(확대, 축소 정도)
      };

      var options3 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[2], lat[2]), //지도의 중심좌표.
        level: 8 //지도의 레벨(확대, 축소 정도)
      };

      var map = new kakao.maps.Map(container, options);
      var map2 = new kakao.maps.Map(container2, options2);
      var map3 = new kakao.maps.Map(container3, options3);
      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

      for (var i = 0; i < this.other_road[0].length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[0][i].lng, this.other_road[0][i].lat);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[0][i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      for (var i = 0; i < this.other_road[1].length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[1][i].lng, this.other_road[1][i].lat);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map2, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[1][i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      for (var i = 0; i < this.other_road[2].length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[2][i].lng, this.other_road[2][i].lat);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map3, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[2][i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      this.makePolyLine(map, 0);
      this.makePolyLine(map2, 1);
      this.makePolyLine(map3, 2);
    },
    makePolyLine(map, n){

      var linePath = [];

      for(var i = 0; i< this.other_road[n].length; i++){
        linePath.push( new kakao.maps.LatLng(this.other_road[n][i].lng, this.other_road[n][i].lat));
      }

      // 지도에 표시할 선을 생성합니다
      var polyline = new kakao.maps.Polyline({
          path: linePath, // 선을 구성하는 좌표배열 입니다
          strokeWeight: 5, // 선의 두께 입니다
          strokeColor: '#0000FF', // 선의 색깔입니다
          strokeOpacity: 0.9, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
          strokeStyle: 'solid' // 선의 스타일입니다
      });

      // 지도에 선을 표시합니다
      polyline.setMap(map);
    }
  },
};
</script>

<style > 

@media (min-width: 1200px) {
    #app {
      padding-left: 0px;
      padding-right: 0px;
    }
  }
  .map {
  width: 350px;
  height: 300px;
}

</style>
<<<<<<< HEAD
<style scoped>
@import url(https://fonts.googleapis.com/css?family=Varela+Round);

html, body { background: #333 url("https://codepen.io/images/classy_fabric.png"); }

.slides {
    padding: 0;
    width: 1050px;
    height: 620px;
    display: block;
    margin: 0 auto;
    position: relative;
}

.slides * {
    user-select: none;
    -ms-user-select: none;
    -moz-user-select: none;
    -khtml-user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none;
}

.slides input { display: none; }

.slide-container { display: block; }

.slide {
    top: 0;
    opacity: 0;
    width: 1050px;
    height: 620px;
    display: block;
    position: absolute;
    transform: scale(0);
    transition: all .7s ease-in-out;
}

.slide img {
    width: 100%;
    height: 100%;
}

.nav label {
    width: 200px;
    height: 100%;
    display: none;
    position: absolute;

    opacity: 0;
    z-index: 9;
    cursor: pointer;

    transition: opacity .2s;

    color: #FFF;
    font-size: 156pt;
    text-align: center;
    line-height: 640px;
    font-family: "Varela Round", sans-serif;
    background-color: rgba(255, 255, 255, .3);
    text-shadow: 0px 0px 15px rgb(119, 119, 119);
}

.slide:hover + .nav label { opacity: 0.5; }

.nav label:hover { opacity: 1; }

.nav .next { right: 0; }

input:checked + .slide-container  .slide {
    opacity: 1;

    transform: scale(1);

    transition: opacity 1s ease-in-out;
}

input:checked + .slide-container .nav label { display: block; }

.nav-dots {
  width: 100%;
  bottom: 9px;
  height: 11px;
  display: block;
  position: absolute;
  text-align: center;
}

.nav-dots .nav-dot {
  top: -5px;
  width: 11px;
  height: 11px;
  margin: 0 4px;
  position: relative;
  border-radius: 100%;
  display: inline-block;
  background-color: rgba(0, 0, 0, 0.6);
}

.nav-dots .nav-dot:hover {
  cursor: pointer;
  background-color: rgba(0, 0, 0, 0.8);
}

input#img-1:checked ~ .nav-dots label#img-dot-1,
input#img-2:checked ~ .nav-dots label#img-dot-2,
input#img-3:checked ~ .nav-dots label#img-dot-3,
input#img-4:checked ~ .nav-dots label#img-dot-4,
input#img-5:checked ~ .nav-dots label#img-dot-5,
input#img-6:checked ~ .nav-dots label#img-dot-6 {
  background: rgba(0, 0, 0, 0.8);
}
</style>

<style lang="scss">
// .slide {
  
//   .image-container {
//     img {
//       width: 1200px;
//       height: 700px;
//     }
//     float: left;
//     width: 100%;
//     margin-right: 15px;
//   }
//   .title {
//     font-size: 20px;
//     font-weight: 700;
//     text-align: left;
//   }
//   .teaser {
//     text-align: left;
//   }
  
// }

// * {
//   -webkit-box-sizing: border-box;
//   -moz-box-sizing: border-box;
//   -ms-box-sizing: border-box;
//   box-sizing: border-box;
// }

// #slider {
//   max-width: 1600px;
//   text-align: center;
//   margin: 0 auto;
// }

// #overflow {
//   width: 100%;
//   overflow: hidden;
// }

// #slides .inner {
//   width: 400%;
// }

// #slides .inner {
//   -webkit-transform: translateZ(0);
//   -moz-transform: translateZ(0);
//   -o-transform: translateZ(0);
//   -ms-transform: translateZ(0);
//   transform: translateZ(0);

//   -webkit-transition: all 800ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -moz-transition: all 800ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -o-transition: all 800ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -ms-transition: all 800ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   transition: all 800ms cubic-bezier(0.770, 0.000, 0.175, 1.000);

//   -webkit-transition-timing-function: cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -moz-transition-timing-function: cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -o-transition-timing-function: cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   -ms-transition-timing-function: cubic-bezier(0.770, 0.000, 0.175, 1.000);
//   transition-timing-function: cubic-bezier(0.770, 0.000, 0.175, 1.000);
// }

// #slides article {
//   width: 25%;
//   float: left;
// }

// #slide1:checked ~ #slides .inner {
//   margin-left: 0;
// }

// #slide2:checked ~ #slides .inner {
//   margin-left: -100%;
// }

// #slide3:checked ~ #slides .inner {
//   margin-left: -200%;
// }

// #slide4:checked ~ #slides .inner {
//   margin-left: -300%;
// }

// input[type="radio"] {
//   display: none;
// }

// label {
//   background: #CCC;
//   display: inline-block;
//   cursor: pointer;
//   width: 13px;
//   height: 13px;
//   border-radius: 5px;
// }

// #slide1:checked ~ label[for="slide1"],
// #slide2:checked ~ label[for="slide2"],
// #slide3:checked ~ label[for="slide3"],
// #slide4:checked ~ label[for="slide4"] {
//   background: #333;
// }
</style>
=======
>>>>>>> b47026525afafa48045ba7988578293f902a2137
