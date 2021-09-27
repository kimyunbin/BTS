<template>
  <div>
    <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
      <h2><b>{{select_info.title}}</b></h2>
      <v-layout row justify-end data-aos="fade-right">
        <v-toolbar-title class="headline">
          <div @click="changeLike" style="display:inline-block">
            <img
              class="likeBtn"
              v-if="this.isLike == true"
              src="@/assets/heart.png"
            />
            <img class="likeBtn" v-else src="@/assets/heart_b.png" />
          </div>

        </v-toolbar-title>
        &nbsp;
          <div @click="share()">
              <img
                class="shareBtn"
                src="https://i.ibb.co/syM6w5V/share.png"
              />
            </div>
        <v-btn class="primary" flat to="/reviewwrite" v-b-tooltip.hover title="리뷰 작성"><v-icon>assignment</v-icon></v-btn>
      </v-layout>
    </v-layout>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
    <img :src="select_info.src" width="500" height="500" style="display:inline-block"/>
    &nbsp;&nbsp;&nbsp;
      <div class="map_wrap">
        <div id="map" style="width:900;height:100%;position:relative;overflow:hidden;"></div>
        <div id="menu_wrap" class="bg_white" style="display:none">
          <div class="option"></div>
          <hr>
            <ul id="placesList"></ul>
            <div id="pagination"></div>
        </div>
      </div>
    </v-layout>
    <br><br>
    <v-layout row data-aos="fade-up">
      <h2><b>리뷰</b></h2>

    </v-layout>

    <v-layout col data-aos="fade-up">
      <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
        <div>
          <InfoReview
            v-for="(review,key) in reviews"
            :key = key
            :review = review
          />
        </div>
      </v-layout>
    </v-layout>
  </div>

</template>

<script>
import { mapGetters } from "vuex";
import VueHorizontalList from "vue-horizontal-list";
import PlaceComponent from "@/components/PlaceComponent";
import PlaceFun from "@/components/PlaceFun";
import PlaceStay from "@/components/PlaceStay";
import PlaceFood from "@/components/PlaceFood";
import InfoReview from "@/components/InfoReview";
export default {
  name: "TeamMain",
  computed: {
    ...mapGetters([
      "select_info"
    ]),
  },
  mounted() {
    window.kakao && window.kakao.maps
    ? this.initMap()
    : this.addKakaoMapScript();
    this.searchPlaces();
  },
  components: {
    VueHorizontalList,
    PlaceComponent,
    PlaceFun,
    PlaceStay,
    PlaceFood,
    InfoReview

  },
  created() {
    this.place = this.select_info.title;
  },
  data() {
    return {
      isLike :false,
      markers :[],
      map:{},
      ps : {},
      infowindow : {},
      place: "강남",
      reviews:[
        {
          userid: "abc1234",
          title: "의정부에서 부대찌개를 먹으려면 여기로",
          contents:"맛있어용abcdqwewqewqedsgmdsalgmlsadgadgmsdfasfasfmasdlfgma",
          write_date: "2020-07-20",
          evaluate: 3,
        },
        {
          userid: "def1235",
          title: "부대찌개의 진리",
          contents:"맛없어용",
          write_date: "2021-05-10",
          evaluate: 1,
        },
        {
          userid: "qwe1234",
          title: "나다싶으면 여기로 컴온",
          contents:"맛있어용",
          write_date: "2012-04-20",
          evaluate: 4,
        },
        {
          userid: "sgs123",
          title: "존맛탱구리",
          contents:"맛있어용",
          write_date: "2020-07-20",
          evaluate: 2,
        },
      ]
    };
  },

  methods: {
    check(){
      alert(this.select_place.title);
    },

    changeLike(){
      this.isLike = !this.isLike;
      alert("관심목록에 추가되었습니다.");
    },

    share(){
      var url = '';
      var textarea = document.createElement("textarea");
      document.body.appendChild(textarea);
      url = window.document.location.href;
      textarea.value = url;
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      alert("URL이 복사되었습니다.")
    },

    addKakaoMapScript() {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
          "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=2308e0069ab87daa299bf6d8b3db30e6";
      document.head.appendChild(script);
    },
    initMap() {
      this.markers = [];
      var container = document.getElementById("map"); //지도를 담을 영역의 DOM 레퍼런스
      var options = {
      //지도를 생성할 때 필요한 기본 옵션
      center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
      level: 3 //지도의 레벨(확대, 축소 정도)
      };
      this.map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
      this.ps = new kakao.maps.services.Places();
      this.infowindow = new kakao.maps.InfoWindow({zIndex:3});
      //console.log(this.map);
    },
    searchPlaces() {
      var keyword = this.place;

      if (!keyword.replace(/^\s+|\s+$/g, '')) {
        alert('장소를 입력해주세요!');
        return false;
      }

      // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
      this.ps.keywordSearch( keyword, this.placesSearchCB);
    },

    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {

        // 정상적으로 검색이 완료됐으면
        // 검색 목록과 마커를 표출합니다
            this.displayPlaces(data);

            // 페이지 번호를 표출합니다
            this.displayPagination(pagination);

            } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
                alert('검색 결과가 존재하지 않습니다.');
                return;
            } else if (status === kakao.maps.services.Status.ERROR) {
                alert('검색 결과 중 오류가 발생했습니다.');
                return;
            }
        },
        displayPlaces(places) {
            var listEl = document.getElementById('placesList'),
            menuEl = document.getElementById('menu_wrap'),
            fragment = document.createDocumentFragment(),
            bounds = new kakao.maps.LatLngBounds(),
            listStr = '';

            // 검색 결과 목록에 추가된 항목들을 제거합니다
            this.removeAllChildNods(listEl);
            // 지도에 표시되고 있는 마커를 제거합니다
            this.removeMarker();
            var infowindow =  new kakao.maps.InfoWindow({zIndex:1});
            var map = this.map;
            for ( var i=0; i<1; i++ ) {

                // 마커를 생성하고 지도에 표시합니다
                var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
                    marker = this.addMarker(placePosition, i),
                    itemEl = this.getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

                // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
                // LatLngBounds 객체에 좌표를 추가합니다
                bounds.extend(placePosition);

                // 마커와 검색결과 항목에 mouseover 했을때
                // 해당 장소에 인포윈도우에 장소명을 표시합니다
                // mouseout 했을 때는 인포윈도우를 닫습니다

                (function(marker, title) {

                    kakao.maps.event.addListener(marker, 'mouseover', function() {
                        var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
                        infowindow.setContent(content);
                        infowindow.open(map, marker);
                    });


                    kakao.maps.event.addListener(marker, 'mouseout', function() {
                        infowindow.close();
                    });

                    itemEl.onmouseover =  function () {
                        var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
                        infowindow.setContent(content);
                        infowindow.open(map, marker);
                    };

                    itemEl.onmouseout =  function () {
                        infowindow.close();
                    };
                })(marker, places[i].place_name);

                fragment.appendChild(itemEl);
            }

            // 검색결과 항목들을 검색결과 목록 Elemnet에 추가합니다
            listEl.appendChild(fragment);
            menuEl.scrollTop = 0;
            // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
            this.map.setBounds(bounds);
        },
        getListItem(index, places) {
            var el = document.createElement('li'),
            itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                        '<div class="info">' +
                        '   <h5>' + places.place_name + '</h5>';

            if (places.road_address_name) {
                itemStr += '    <span>' + places.road_address_name + '</span>' +'&nbsp&nbsp'+
                            '   <span class="jibun gray">' +  places.address_name  + '</span>';
            } else {
                itemStr += '    <span>' +  places.address_name  + '</span>';
            }

            itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                        '</div>';

            el.innerHTML = itemStr;
            el.className = 'item';

            return el;
        },
        addMarker(position, idx, title) {
            var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
                imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
                imgOptions =  {
                    spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
                    spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
                    offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
                },
                markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
                marker = new kakao.maps.Marker({
                    position: position, // 마커의 위치
                    image: markerImage
                });
            //console.log(marker);
            marker.setMap(this.map); // 지도 위에 마커를 표출합니다
            this.markers.push(marker);  // 배열에 생성된 마커를 추가합니다

            return marker;
        },
        removeMarker() {
            for ( var i = 0; i < this.markers.length; i++ ) {
                this.markers[i].setMap(null);
            }
            this.markers = [];
        },
        displayPagination(pagination) {
            var paginationEl = document.getElementById('pagination'),
                fragment = document.createDocumentFragment(),
                i;

            // 기존에 추가된 페이지번호를 삭제합니다
            while (paginationEl.hasChildNodes()) {
                paginationEl.removeChild (paginationEl.lastChild);
            }

            for (i=1; i<=pagination.last; i++) {
                var el = document.createElement('a');
                el.href = "#";
                el.innerHTML = i;

                if (i===pagination.current) {
                    el.className = 'on';
                } else {
                    el.onclick = (function(i) {
                        return function() {
                            pagination.gotoPage(i);
                        }
                    })(i);
                }

                fragment.appendChild(el);
            }
            paginationEl.appendChild(fragment);
        },
        removeAllChildNods(el) {
            while (el.hasChildNodes()) {
                el.removeChild (el.lastChild);
            }
        }
  }
};
</script>

<style scoped>
  .likeBtn {
    right: 0;
    width: 30px;
    height: 30px;
    margin: 0.2em 0 0 0;
    z-index: 10;
    background-size: cover;
  }
  .likeBtn:hover {
    cursor: pointer;
    transform: scale(1.1);
  }
  .shareBtn {
    right: 0;
    width: 28px;
    height: 29px;
    margin: 0.4em 0 0 0;
    z-index: 10;
    background-size: cover;
  }
  .shareBtn:hover {
    cursor: pointer;
    transform: scale(1.1);
  }

  .map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
  .map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
  .map_wrap {position:relative;width:500px;height:500px;}
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
  #placesList .item .info{padding:10px 0 10px 55px;}
  #placesList .info .gray {color:#8a8a8a;}
  #placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
  #placesList .info .tel {color:#009900;}
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
</style>
