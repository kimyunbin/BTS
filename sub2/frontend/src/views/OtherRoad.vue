<template>
  <div>
    <br>
    <h1 data-aos="fade-up"><b>OOO님의 여행 경로입니다.</b></h1>
    <div id="map" class="map"></div>
    <v-btn @click="check()"></v-btn>
  </div>      
</template>

<script>
import { mapGetters } from "vuex";
export default {
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
  },
  computed:{
    ...mapGetters(["select_road"]),
  },
  methods: {
    check(){
      console.log(this.select_road);
    },
    addKakaoMapScript() {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=2308e0069ab87daa299bf6d8b3db30e6";
      document.head.appendChild(script);
    },
    initMap() {
      var container = document.getElementById("map"); //지도를 담을 영역의 DOM 레퍼런스
      var lat = 0;
      var lng = 0;
    
      for (var i = 0; i < this.select_road.length; i++) {
        lat +=  parseFloat(this.select_road[i].lat);
        lng +=  parseFloat(this.select_road[i].lng);
      
      }
      lat /= this.select_road.length;
      lng /= this.select_road.length;
    
      var options = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng, lat), //지도의 중심좌표.
        level: 8 //지도의 레벨(확대, 축소 정도)
      };

      var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
    
      for (var i = 0; i < this.select_road.length; i++) {
          
          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35); 
          
          // 마커 이미지를 생성합니다    
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
          var latlng = new kakao.maps.LatLng(this.select_road[i].lng, this.select_road[i].lat); 
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.select_road[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지 
          });
      }
      this.makePolyLine(map);
      this.displayInfo(map);
    },
    makePolyLine(map){

      var linePath = [];
            
      for(var i = 0; i< this.select_road.length; i++){
        linePath.push( new kakao.maps.LatLng(this.select_road[i].lng,this.select_road[i].lat));
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
    displayInfo(map){
      for (var i = 0; i < this.select_road.length; i ++) {
    // 마커를 생성합니다
        var latlng = new kakao.maps.LatLng(this.select_road[i].lng, this.select_road[i].lat); 
        var marker = new kakao.maps.Marker({
            map: map, // 마커를 표시할 지도
            position:latlng // 마커의 위치
        });

        // 마커에 표시할 인포윈도우를 생성합니다 
        var infowindow = new kakao.maps.InfoWindow({
            content: '<div class="wrap3">' + 
                            '    <div class="info3">' + 
                            '        <div class="title3">' + 
                                            this.select_road[i].title      + 
                            
                            '        </div>' + 
                            '        <div class="body3">' +
                            '            <div class="img3">' +
                            '                <img src="https://i.ibb.co/gWBNgwm/image.jpg" width="73" height="70">' +
                            '           </div>' + 
                            '            <div class="desc3">' + 
                            '                <div class="ellipsis3">'+
                                            this.select_road[i].lat+
                            '</div>' + 
                            '                <div class="jibun3 ellipsis3">(우) 63309 (지번) 영평동 2181</div>' + 
                            '                <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>' + 
                            '            </div>' + 
                            '        </div>' + 
                            '    </div>' +    
                            '</div>'
        });

        // 마커에 mouseover 이벤트와 mouseout 이벤트를 등록합니다
        // 이벤트 리스너로는 클로저를 만들어 등록합니다 
        // for문에서 클로저를 만들어 주지 않으면 마지막 마커에만 이벤트가 등록됩니다
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListener(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
      }

      // 인포윈도우를 표시하는 클로저를 만드는 함수입니다 
      function makeOverListener(map, marker, infowindow) {
          return function() {
              infowindow.open(map, marker);
          };
      }

      // 인포윈도우를 닫는 클로저를 만드는 함수입니다 
      function makeOutListener(infowindow) {
          return function() {
              infowindow.close();
          };
      }
    }
  },
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 600px;
}
</style>