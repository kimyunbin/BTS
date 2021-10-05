<template>
  <div>
    <br><br>
    <v-layout>
      <h1 data-aos="fade-up"><b>My Page</b></h1>
    </v-layout>
    <br>
    <br>
    <!-- <v-btn @click="check()"></v-btn> -->
    <h1><b>내가 직접 만든 여행코스</b></h1>
    <br>
    <section v-if="my_road.length>0">
      <v-layout row justify-center align-center wrap class="mt-4 pt-2" >
        <v-card @click="setDetailRoad(0)" hover v-if="my_road.length>2">
          <div id="amap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_road[0].title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover v-if="my_road.length>1">
          <div id="bmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_road[1].title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover v-if="my_road.length>2">
          <div id="cmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_road[2].title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;
      </v-layout>  
    </section>
    <br>
    <br>
    <h1><b>찜한 여행코스</b></h1>
    <br>
    <section>

      <section v-if="my_wish_road.length>0">
      <v-layout row justify-center align-center wrap class="mt-4 pt-2" >
        <v-card @click="setDetailRoad(0)" hover >
          <div id="dmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_wish_road[0].route.title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(1)" hover v-if="my_wish_road.length>1">
          <div id="emap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_wish_road[1].route.title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;&nbsp;&nbsp;

        <v-card @click="setDetailRoad(2)" hover v-if="my_wish_road.length>2">
          <div id="fmap" class="map" style="display:inline-block"></div>
          <div>
            <p class="headline mb-0" style="text-align:center"><b>{{my_wish_road[2].route.title}} </b></p>
          </div>
        </v-card>&nbsp;&nbsp;
      </v-layout>  
    </section>
    </section>

    <br>
    <br>
    <h1>
      <b>관심지역</b>
      </h1>

    <br>
    <section style="">

      <vue-horizontal-list :items="wishlist" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>
        <template v-slot:default="{ item }">
          <SpotComponent
            :item="item.Touristspot"
          />
        </template>
      </vue-horizontal-list>
    </section>
  </div>
</template>

<script>
import VueHorizontalList from "vue-horizontal-list";
import PlaceComponent from "@/components/PlaceComponent";
import SpotComponent from "@/components/SpotComponents";
import PlaceWish from "@/components/PlaceWish";
import { mapGetters, mapState } from "vuex";

export default {
  name: 'MyPage',
  components: {
    VueHorizontalList,
    PlaceComponent,
    PlaceWish,
    SpotComponent
  },
  computed:{
    ...mapGetters([
      "my_road","other_road","my_wish_road"
    ]),
    ...mapState([
      "is_login", "user_info","wishlist"
    ])
  },
  created() {
    this.$store.dispatch("GET_WISHLIST")
  },
  mounted(){
      window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
      
  },
  data() {
    return {
      options: {
        item: {
          padding: 10
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
        autoplay: { play: true, repeat: true, speed: 3600 },
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
      wishes: [
        { id:"1", title: "해운대 해수욕장", content: "Content item with description", src: "https://i.ibb.co/sv0Cqg1/image.jpg"},
        { id:"2", title: "대구 구공탄막창", content: "Content item with description", src: "https://i.ibb.co/KmtrYTf/image.jpg"},
        { id:"3", title: "제2롯데타워", content: "Content item with description", src: "https://i.ibb.co/w6cC5MT/image.jpg"},
        { id:"4", title: "여수", content: "Content item with description", src: "https://i.ibb.co/60yjckh/image.jpg"},
        { id:"5", title: "의정부역", content: "Content item with description", src: "https://i.ibb.co/Z24FjMD/image.jpg"},
        { id:"6", title: "전주한옥마을", content: "Content item with description", src: "https://i.ibb.co/0V3grZZ/image.jpg"},
        { id:"7", title: "연천", content: "Content item with description", src: "https://i.ibb.co/kBjW0Wg/image.jpg"},
        { id:"8", title: "수원화성", content: "Content item with description", src: "https://i.ibb.co/StjhL5X/image.png"},
        { id:"9", title: "Item 8", content: "Content item with description", src: "https://i.ibb.co/gWBNgwm/image.jpg"},
      ],
    }
  },
 
  
  methods: {
    check(){
      console.log(this.my_road);
      console.log(this.other_road);
      console.log(this.my_wish_road);
    },
    goWishList(){
        this.$router.replace("/myinteresting");
    },
    setDetailRoad(num){
      this.$store.dispatch("SET_SELECT_ROAD", this.my_road[num]).then(()=>{
        this.$router.replace("/otherroad");
      });
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
      var container4 = document.getElementById("dmap");
      var container5 = document.getElementById("emap");
      var container6 = document.getElementById("fmap");
      var lat = [];
      var lng = [];
      var lat2 = [];
      var lng2 = [];
      if(this.my_road){
        for(var j = 0; j < this.my_road.length; j++){
          lat[j] = 0;
          lng[j] = 0;
        }
        for(var j = 0; j < this.my_wish_road.length; j++){
          lat2[j] = 0;
          lng2[j] = 0;
        }
        for(var j = 0; j < this.my_road.length; j++){
          for (var i = 0; i < this.my_road[j].spots.length; i++) {
            lat[j] +=  parseFloat(this.my_road[j].spots[i].touristspot.latitude);
            lng[j] +=  parseFloat(this.my_road[j].spots[i].touristspot.longitude);
          }
          lat[j] /= this.my_road[j].spots.length;
          lng[j] /= this.my_road[j].spots.length;
        }
      }
      for(var j = 0; j < this.my_wish_road.length; j++){
        for (var i = 0; i < this.my_wish_road[j].route.spots.length; i++) {
          lat2[j] +=  parseFloat(this.my_wish_road[j].route.spots[i].touristspot.latitude);
          lng2[j] +=  parseFloat(this.my_wish_road[j].route.spots[i].touristspot.longitude);
        }
        lat2[j] /= this.my_wish_road[j].route.spots.length;
        lng2[j] /= this.my_wish_road[j].route.spots.length;
      }
      if(this.my_road){
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
      }

      var options4 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng2[0], lat2[0]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };

      var options5 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng2[1], lat2[1]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };

      var options6 = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng2[2], lat2[2]), //지도의 중심좌표.
        level: 10 //지도의 레벨(확대, 축소 정도)
      };
      if(this.my_road){
        var map = new kakao.maps.Map(container, options);
        var map2 = new kakao.maps.Map(container2, options2);
        var map3 = new kakao.maps.Map(container3, options3);
      }
      var map4 = new kakao.maps.Map(container4, options4);
      if(lat2.length>1){
        var map5 = new kakao.maps.Map(container5, options5);
      }
      if(lat2.length>2){
        var map6 = new kakao.maps.Map(container6, options6);
      }
      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
      for (var i = 0; i < this.my_road[0].spots.length; i++) {
          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.my_road[0].spots[i].touristspot.longitude, this.my_road[0].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.my_road[0].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      for (var i = 0; i < this.my_road[1].spots.length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.my_road[1].spots[i].touristspot.longitude, this.my_road[1].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map2, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.my_road[1].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      for (var i = 0; i < this.my_road[2].spots.length; i++) {

          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35);

          // 마커 이미지를 생성합니다
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
          var latlng = new kakao.maps.LatLng(this.my_road[2].spots[i].touristspot.longitude, this.my_road[2].spots[i].touristspot.latitude);
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map3, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.my_road[2].spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지
          });
      }
      if(this.my_wish_road.length>0){
        for (var i = 0; i < this.my_wish_road[0].route.spots.length; i++) {
            // 마커 이미지의 이미지 크기 입니다
            var imageSize = new kakao.maps.Size(24, 35);

            // 마커 이미지를 생성합니다
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
            var latlng = new kakao.maps.LatLng(this.my_wish_road[0].route.spots[i].touristspot.longitude, this.my_wish_road[0].route.spots[i].touristspot.latitude);
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map4, // 마커를 표시할 지도
                position: latlng, // 마커를 표시할 위치
                title : this.my_wish_road[0].route.spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                image : markerImage // 마커 이미지
            });
        }
      }
      if(this.my_wish_road.length>1){
        for (var i = 0; i < this.my_wish_road[1].route.spots.length; i++) {

            // 마커 이미지의 이미지 크기 입니다
            var imageSize = new kakao.maps.Size(24, 35);

            // 마커 이미지를 생성합니다
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
            var latlng = new kakao.maps.LatLng(this.my_wish_road[1].route.spots[i].touristspot.longitude, this.my_wish_road[1].route.spots[i].touristspot.latitude);
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map5, // 마커를 표시할 지도
                position: latlng, // 마커를 표시할 위치
                title : this.my_wish_road[1].route.spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                image : markerImage // 마커 이미지
            });
        }
      }
      if(this.my_wish_road.length>2){
        for (var i = 0; i < this.my_wish_road[2].route.spots.length; i++) {

            // 마커 이미지의 이미지 크기 입니다
            var imageSize = new kakao.maps.Size(24, 35);

            // 마커 이미지를 생성합니다
            var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
            var latlng = new kakao.maps.LatLng(this.my_wish_road[2].route.spots[i].touristspot.longitude, this.my_wish_road[2].route.spots[i].touristspot.latitude);
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map6, // 마커를 표시할 지도
                position: latlng, // 마커를 표시할 위치
                title : this.my_wish_road[2].route.spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
                image : markerImage // 마커 이미지
            });
        }
      }
      this.makePolyLine(map, 0);
      this.makePolyLine(map2, 1);
      this.makePolyLine(map3, 2);
      if(lat2.length>0){
        this.makePolyLine2(map4, 0);
      }
      if(lat2.length>1){
        this.makePolyLine2(map5, 1);
      }
      if(lat2.length>2){
        this.makePolyLine2(map6, 2);
      }
    },
    makePolyLine(map, n){

      var linePath = [];

      for(var i = 0; i< this.my_road[n].spots.length; i++){
        linePath.push( new kakao.maps.LatLng(this.my_road[n].spots[i].touristspot.longitude, this.my_road[n].spots[i].touristspot.latitude));
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
    makePolyLine2(map, n){

      var linePath = [];

      for(var i = 0; i< this.my_wish_road[n].route.spots.length; i++){
        linePath.push( new kakao.maps.LatLng(this.my_wish_road[n].route.spots[i].touristspot.longitude, this.my_wish_road[n].route.spots[i].touristspot.latitude));
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
  }
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
