<template>
  <div>
    <br>
    <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
      <h1 data-aos="fade-up"><b>{{select_wish_road.route.user.nickname}} 님의 여행 경로입니다.</b><v-btn large @click="back()" flat class="blue--text">
          <v-icon>arrow_back</v-icon>뒤로가기
      </v-btn></h1>
      <v-layout justify-end align-end wrap class="mt-4 pt-2" data-aos="fade-up">
        <!-- <v-btn @click="storeMyRoad()" color="red" class = "white--text"><v-icon>favorite</v-icon></v-btn> -->
      </v-layout>
    </v-layout>
    
    <div id="map" class="map"></div>
    
  </div>      
</template>

<script>
import { mapGetters } from "vuex";
import { createInstance2 } from "@/api/index.js";

export default {
  mounted() {
    window.kakao && window.kakao.maps
      ? this.initMap()
      : this.addKakaoMapScript();
  },
  computed:{
    ...mapGetters(["select_wish_road","user_info"]),
  },
  methods: {
    check(){
      console.log(this.select_wish_road);
    },
    back(){
      this.$router.go(-1);
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
    
      for (var i = 0; i < this.select_wish_road.route.spots.length; i++) {
        lat +=  parseFloat(this.select_wish_road.route.spots[i].touristspot.latitude);
        lng +=  parseFloat(this.select_wish_road.route.spots[i].touristspot.longitude);
      
      }
      lat /= this.select_wish_road.route.spots.length;
      lng /= this.select_wish_road.route.spots.length;
      
      var options = {
        //지도를 생성할 때 필요한 기본 옵션
        center: new kakao.maps.LatLng(lng, lat), //지도의 중심좌표.
        level: 8 //지도의 레벨(확대, 축소 정도)
      };

      var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
    
      for (var i = 0; i < this.select_wish_road.route.spots.length; i++) {
          
          // 마커 이미지의 이미지 크기 입니다
          var imageSize = new kakao.maps.Size(24, 35); 
          
          // 마커 이미지를 생성합니다    
          var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
          var latlng = new kakao.maps.LatLng(this.select_wish_road.route.spots[i].touristspot.longitude,this.select_wish_road.route.spots[i].touristspot.latitude); 
          // 마커를 생성합니다
          var marker = new kakao.maps.Marker({
              map: map, // 마커를 표시할 지도
              position: latlng, // 마커를 표시할 위치
              title : this.select_wish_road.route.spots[i].touristspot.title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
              image : markerImage // 마커 이미지 
          });
      }
      this.makePolyLine(map);
      this.displayInfo(map);
    },
    makePolyLine(map){

      var linePath = [];
            
      for(var i = 0; i< this.select_wish_road.route.spots.length; i++){
        linePath.push( new kakao.maps.LatLng(this.select_wish_road.route.spots[i].touristspot.longitude,this.select_wish_road.route.spots[i].touristspot.latitude));
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
      for (var i = 0; i < this.select_wish_road.route.spots.length; i ++) {
    // 마커를 생성합니다
        var latlng = new kakao.maps.LatLng(this.select_wish_road.route.spots[i].touristspot.longitude,this.select_wish_road.route.spots[i].touristspot.latitude); 
        var marker = new kakao.maps.Marker({
            map: map, // 마커를 표시할 지도
            position:latlng // 마커의 위치
        });

        // 마커에 표시할 인포윈도우를 생성합니다 

        var url ="";
        if(this.select_wish_road.route.spots[i].touristspot.img.length==0){
          url = "noimage.png";
        }else{
          url = this.select_wish_road.route.spots[i].touristspot.img[0].awsimages;
        }
        var infowindow = new kakao.maps.InfoWindow({
            content: '<div class="wrap3">' + 
                            '    <div class="info3">' + 
                            '        <div class="title3">' + 
                                            this.select_wish_road.route.spots[i].touristspot.title      + 
                            
                            '        </div>' + 
                            '        <div class="body3">' +
                            '            <div class="img3">' +
                            '                <img src="https://go-test-buket.s3.ap-northeast-2.amazonaws.com/'+url +'" width="73" height="70">' +
                            '           </div>' + 
                            '            <div class="desc3">' + 
                            '                <div class="ellipsis3">'+
                                                this.select_wish_road.route.spots[i].touristspot.address+
                                            '</div>' + 
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
    },
    storeMyRoad() {
            const instance = createInstance2();
            var title='';
            
                console.log(this.select_road.id);
                instance.post("/tour/route/follow/"+this.select_road.id+"/")
                    .then(
                        (response) => {
                            console.log(response);
                            this.$alert("저장이 완료되었습니다.").then(() => {
                                this.$router.push("/home");
                            })
                        }
                    )
                    .catch(() => {
                    
                    });
            },
  },
};
</script>

<style scoped>
.map {
  width: 100%;
  height: 600px;
}

.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:800px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info2{padding:10px 0 10px 55px;}
#placesList .info2 .gray {color:#8a8a8a;}
#placesList .info2 .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info2 .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}
.info2 .close {position: absolute;top: 10px;right: 10px;color: #888;width: 17px;height: 17px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/overlay_close.png');}


</style>