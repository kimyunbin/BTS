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

      <!-- <v-btn @click="check()"></v-btn> -->
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

    <br><br><br>
    <h1><b>{{user_info}} 님을 위한 추천 여행지역</b></h1>
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
          <div id="amap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[0].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0].user.nickname}}님</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover>
          <div id="bmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[1].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[1].user.nickname}}님</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover>
          <div id="cmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[2].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[2].user.nickname}}님</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;
      </v-layout>
    </section>

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
import { createInstance2} from "@/api/index.js";

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
          padding: 10
        },
        map:{
          padding: 10
        },
        responsive: [
          { end: 576, size: 1 },
          { start: 576, end: 768, size: 2 },
          { start: 768, end: 992, size: 3 },
          { size: 4 },
        ],
        list: {
          windowed: 1200,
          padding: 10,
        },
        position: {
          start: 4,
        },
        autoplay: { play: true, repeat: true, speed: 2400 },
        hover:{
          cursor:"pointer"
        }
      },
      username: '',
    };
  },
  created() {
    this.$store.dispatch("GET_RECOMMEND_AREA")
    .then(()=>{
      this.items2 =  this.$store.state.recom_area
    })

    const random_instance = createInstance2();
    random_instance.get("/tour/routerandom/").then(
      (response) =>{
        this.$store.commit("CLEAR_OTHER_ROAD", response.data);
        this.$store.commit("SET_OTHER_ROAD", response.data);
        window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
      $(document).ready(function(){
      $('.slider').slider();
    });
      }
    )
    this.$store.dispatch("GET_OTHER_RECOMMEND_AREA")
    const instance2 = createInstance2();
          instance2.get("/tour/route/follow/").then(
            (response) =>{
              this.$store.dispatch("SET_MY_WISH_ROAD", response.data.data).then(()=>{
                
              })
          })

  },

  methods: {
    check(){
      console.log(this.my_wish_road);

    },
    setDetailRoad(num){
      console.log(this.other_road[num].spots);
      this.$store.dispatch("SET_SELECT_ROAD", this.other_road[num]).then(()=>{
        this.$router.replace("/otherroad");
      });
    },
    checkOtherRoad(){
      console.log(this.other_road);
    },
    addKakaoMapScript() {
      const script = document.createElement("script");

      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=2308e0069ab87daa299bf6d8b3db30e6";
      document.head.appendChild(script);
    },
    initMap() {
      var container = document.getElementById("amap");
      var container2 = document.getElementById("bmap");
      var container3 = document.getElementById("cmap");
      var lat = [];
      var lng = [];
      for(var j = 0; j < this.other_road.length; j++){
        lat[j] = 0;
        lng[j] = 0;
      }
      for(var j = 0; j < this.other_road.length; j++){
        for (var i = 0; i < this.other_road[j].spots.length; i++) {
          lat[j] +=  parseFloat(this.other_road[j].spots[i].touristspot.latitude);
          lng[j] +=  parseFloat(this.other_road[j].spots[i].touristspot.longitude);
        }
        lat[j] /= this.other_road[j].spots.length;
        lng[j] /= this.other_road[j].spots.length;
        
      }
    


      var options = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[0], lat[0]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };

      var options2 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[1], lat[1]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };

      var options3 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng[2], lat[2]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };

      var map = new kakao.maps.Map(container, options);
      var map2 = new kakao.maps.Map(container2, options2);
      var map3 = new kakao.maps.Map(container3, options3);
      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

      for (var i = 0; i < this.other_road[0].spots.length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[0].spots[i].touristspot.longitude, this.other_road[0].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          console.log(this.other_road[0].spots[i].touristspot.title);
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[0].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
          //console.log(marker);
      }
      for (var i = 0; i < this.other_road[1].spots.length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[1].spots[i].touristspot.longitude, this.other_road[1].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map2, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[1].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      for (var i = 0; i < this.other_road[2].spots.length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.other_road[2].spots[i].touristspot.longitude, this.other_road[2].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map3, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[2].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      this.makePolyLine(map, 0);
      this.makePolyLine(map2, 1);
      this.makePolyLine(map3, 2);
    },
    makePolyLine(map, n){

      var linePath = [];

      for(var i = 0; i< this.other_road[n].spots.length; i++){
        linePath.push( new kakao.maps.LatLng(this.other_road[n].spots[i].touristspot.longitude, this.other_road[n].spots[i].touristspot.latitude));
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

</style>
