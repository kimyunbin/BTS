<template>
  <div id="app">
    <div class="back-ground">
      <h4 data-aos="fade-up">더 나은 여행경험</h4>
      <p class="q" data-aos="fade-up">만족도를 알고 싶으세요?</p>
      <div class="b" @click="toMap">
        <p class="to_map"></p>
      </div>
    </div>
    <br>
    <div class="empty"></div>
    <br><br><br><br><br>
    <h1><b>{{user_info}} 님을 위한 추천 여행지역</b></h1>
    <section>

      <vue-horizontal-list :items="items2" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>        
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
            padding=10
          />
        </template>

      </vue-horizontal-list>
    </section>

    <br><br>
    <h1 data-aos="fade-down"><b>{{user_info}} 님을 위한 관광지 추천 </b></h1>
    <section data-aos="fade-up">
      <vue-horizontal-list :items="recom_spot||items" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <SpotComponents
            :item="item"
          />
        </template>

      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1 data-aos="fade-right"><b>다른 유저가 갔던 여행 경로 추천</b></h1>
    <section v-if="other_road.length>0" data-aos="fade-left">
      <v-layout row justify-center align-center wrap class="mt-4 pt-2" >
        <v-card @click="setDetailRoad(0)" hover v-if="other_road.length>0">
          <div id="amap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[0].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0].user.nickname}}님</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover v-if="other_road.length>1">
          <div id="bmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>{{other_road[1].title}} 여행경로</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[1].user.nickname}}님</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover v-if="other_road.length>2">
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
    <h1 data-aos="fade-right"><b>{{recom_name[0]}}를 위한 추천 여행지역</b></h1>
    <section style="" data-aos="fade-left">
      <vue-horizontal-list :items="gender_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <h1 data-aos="fade-right"><b>{{recom_name[1]}} 추천하는 여행지역</b></h1>
    <section style="" data-aos="fade-left">
      <vue-horizontal-list :items="traveler_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceComponent
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <h1 data-aos="fade-left"><b>{{recom_name[2]}}</b></h1>
    <section style="" data-aos="fade-right">
      <vue-horizontal-list :items="budget_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
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
    <h1 data-aos="fade-left"><b>{{recom_name[3]}} 추천 여행지역</b></h1>
    <section style="" data-aos="fade-right">
      <vue-horizontal-list :items="companion_recom_area" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
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
import defaultimg from "@/assets/img/1.jpg";
import SpotComponents from "@/components/SpotComponents";
import { mapGetters, mapState } from "vuex";
import { createInstance2} from "@/api/index.js";

export default{
  name: "ServeDev",
  components: {
    VueHorizontalList,
    PlaceComponent,
    SpotComponents,
    defaultimg
    
  },
  computed:{
    ...mapGetters([
      "other_road","SET_SELECT_ROAD"
    ]),
    ...mapState([
      "is_login", "user_info", "gender_recom_area", "traveler_recom_area",
      "budget_recom_area", "companion_recom_area", "recom_name"
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
          name: '',
          imgurl: "",
          state: ''
        }, 
        {
          name: '',
          imgurl: "",
          state: ''
        }, 
        {
          name: '',
          imgurl: "",
          state: ''
        }, 
        {
          name: '',
          imgurl: "",
          state: ''
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
        autoplay: { play: true, repeat: true, speed: 3500 },
        hover:{
          cursor:"pointer"
        }
      },
    
      
      recom_spot: [
        { id:"1", title: "", address: "", img:[{awsimages: ""}]},
        { id:"2", title: "", address: "", img:[{awsimages: ""}]},
        { id:"3", title: "", address: "", img:[{awsimages: ""}]},
        { id:"4", title: "", address: "", img:[{awsimages: ""}]},
      ],
      genderItems: [],
      username: '',
      defaultimg
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
      
      }
    )
    this.$store.dispatch("GET_OTHER_RECOMMEND_AREA")
    const instance2 = createInstance2();
          instance2.get("/tour/route/follow/").then(
            (response) =>{
              this.$store.dispatch("SET_MY_WISH_ROAD", response.data.data).then(()=>{
                
              })
          })

    const randomspot = createInstance2();
    randomspot.get("tour/recommendspot/").then(
      (res)=>{
        this.recom_spot = res.data
      }
    )

  },

  methods: {
    check(){
      console.log(this.my_wish_road);

    },
    setDetailRoad(num){
      this.$store.dispatch("SET_SELECT_ROAD", this.other_road[num]).then(()=>{
        this.$router.push("/otherroad");
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
      for(var j = 0; j < 3; j++){
        lat[j] = 0;
        lng[j] = 0;
      }
      for(var j = 0; j < 3; j++){
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
        level: 12 //지도의 레벨(확대, 축소 정도)
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
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.other_road[0].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
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
    },
    toMap(){
      this.$router.push("satisfactionmap")
    }
  },
};
</script>

<style scoped> 

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

.empty{
  height: 27vw;
  margin-bottom: 3px;
}

.back-ground{
  font-family: 'IBM Plex Sans KR', sans-serif;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #FFF;
  flex-direction: column;
  top: 80px;
  left: 0%;
  width: 100vw;
  height: 30vw;
  background-image:url("../assets/img/1.jpg");
  background-image:url("https://cdn.visitkorea.or.kr/img/call?cmd=VIEW&id=90241173-b88a-4431-841c-b7c20c0b5586&mode=raw");
  background-size: cover;
}
.q{
  font-size: 50px;
  font-weight: 600;
  margin-bottom: 10px;
  letter-spacing: 3px;
  text-shadow: 2px 2px 2px 2px #000;
}
.b{
  position: relative;
  display: inline-flex;
  width: 180px;
  height: 55px;
  margin: 0 15px;
  perspective: 1000px;
  cursor: pointer;
}
.to_map{
  font-size: 19px;
  letter-spacing: 1px;
  transform-style: preserve-3d;
  transform: translateZ(-25px);
  transition: transform .25s;
}
.b .to_map:before,
.b .to_map:after{
  position: absolute;
  content: "지도로 가기";
  height: 55px;
  width: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #4caf50;
  box-sizing: border-box;
  border-radius: 5px;
}
.b .to_map:before{
  color: #fff;
  background: #4caf50;
  transform: rotateY(0deg) translateZ(25px);
}
.b .to_map:after{
  color: #4caf50;
  background-color: #FFF;
  font-weight: 600;
  transform: rotateX(90deg) translateZ(25px);
}
.b .to_map:hover{
  transform: translateZ(-25px) rotateX(-90deg);
}
.vhl-items{
  z-index: 1;
}
</style>


