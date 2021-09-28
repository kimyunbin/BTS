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

      <v-btn @click="check()">
      </v-btn>
    </v-layout>
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
      <v-layout row justify-center align-center wrap class="mt-4 pt-2">
        <v-card @click="setDetailRoad(0)" hover>
          <div id="map" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>테스트</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0][0].name}}의 경로</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover>
          <div id="map2" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>서울 구경 가즈아</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0][0].name}}의 경로</b></p>
          </div>
        </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover>
          <div id="map3" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0"><b>테스트</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{other_road[0][0].name}}의 경로</b></p>
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
      <vue-horizontal-list :items="items" :options="options" >
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
    <h1><b>저희가 추천하는 여행지역</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="items" :options="options" >
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
      "is_login", "user_info"
    ])
  },
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
  },
  data() {
    return {
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
      items2: []
    };
  },
  created() {
    this.$store.dispatch("GET_RECOMMEND_AREA")
    .then(()=>{
     this.items2 =  this.$store.state.recom_area
    })
  },

  methods: {
    check(){
      console.log(this.is_login);
      console.log(this.user_info);
    },
    setDetailRoad(num){
      this.$store.dispatch("SET_SELECT_ROAD", this.other_road[num]).then(()=>{
        this.$router.replace("/otherroad");
      });
    },
    checkOtherRoad(){
      console.log(this.other_road);
      console.log(this.other_road[1].length);
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

<style>

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
