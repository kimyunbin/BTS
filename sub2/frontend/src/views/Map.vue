<template>
    <div>
        <div class="map_wrap" ref="printMe">
            <div id="map"  style="width:100%;height:100%;position:relative;overflow:hidden;"></div>

            <div id="menu_wrap" class="bg_white">
                <div class="option">
                    <div>
                        <form>
                            <v-layout row wrap justify-center align-center>
                            장소 :

                            <v-text-field
                                color="green"
                                background-color="transparent"
                                name="value"
                                v-model=place
                                label="장소입력"
                                width="20px"
                                @keydown.enter.prevent="searchPlaces()"
                            ></v-text-field>

                            <v-btn dark small @click="searchPlaces()">검색</v-btn>
                            </v-layout>
                        </form>
                    </div>
                </div>
                <hr>
                <ul id="placesList"></ul>
                <div id="pagination"></div>
            </div>
        </div>
        <br><br>
        <div  v-if="my_road.length">
            <v-layout row justify-center align-center wrap class="mt-0 pt-0">
            <v-flex
                v-for="(road, idx) in this.my_road"
                :key="idx"
                xs12 sm6 md4 lg3 xl3
            >

            <v-layout row>
                <v-card row hover flat width="220" height="230">
                    <v-card-title primary-title class="justify-center">
                        <v-flex text-xs-center subheading font-weight-bold>{{road.title}}</v-flex>
                        <v-btn  elevation="0" icon @click="deleteRoad(idx)"  color="pink white--text" ><v-icon>delete</v-icon></v-btn>
                    </v-card-title>
                    <div v-if="road.src === null">
                        <v-img v-bind:src="thumbnail" width=100% height="100%" object-fit: cover></v-img>
                    </div>
                    <div v-else>
                        <v-img :src="road.src" width=100% height="130" object-fit: cover></v-img>
                    </div>
                    <v-card-title primary-title class="justify-center">
                        <div class="txt_line">위도: {{road.lat}}</div>
                    </v-card-title>
                </v-card>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <v-icon>arrow_right_alt</v-icon>
            </v-layout>

            </v-flex>
            </v-layout>
        </div>

        <!-- <v-btn @click="makeLine()"></v-btn> -->
        <v-btn @click="clearAllRoad()">저장된 경로 전체 삭제</v-btn>

        <v-btn @click="storeMyRoad()">내 경로 저장하기</v-btn>
        <v-btn @click="clearRoad()">경로 초기화</v-btn>
    </div>
</template>

<script>
import { mapGetters } from "vuex";


export default {
    created(){

    },
    computed:{
        ...mapGetters([
            "other_road","CLEAR_OTHER_ROAD"
        ])
    },
    mounted() {
        window.kakao && window.kakao.maps
        ? this.initMap()
        : this.addKakaoMapScript();
        this.searchPlaces();
    },
    data() {
        return{
            markers :[],
            map:{},
            ps : {},
            infowindow : {},
            place: "강남",
            my_road :[

            ],
            my_road_title :[

            ],
            output: null,
            polyline :null,
            linePath :[],
        };
    },
    methods: {
        clearAllRoad(){
            this.$store.dispatch("CLEAR_OTHER_ROAD");
        },
        deleteRoad(idx){
            this.my_road.splice(idx,1);
        },
        clearRoad(){
            this.my_road= [];
        },
        storeMyRoad() {
            this.other_road.push(this.my_road);
            this.makeLine();
            alert("저장이 완료되었습니다.");
            this.my_road = [];
            this.my_road_title = [];
        },

        makeLine(){
            this.linePath = [];
            for(var i = 0; i< this.my_road.length; i++){
                this.linePath.push( new kakao.maps.LatLng(this.my_road[i].lng,this.my_road[i].lat));
            }
            this.polyline = new kakao.maps.Polyline({
                path: this.linePath, // 선을 구성하는 좌표배열 입니다
                strokeWeight: 5, // 선의 두께 입니다
                strokeColor: '#0000FF', // 선의 색깔입니다
                strokeOpacity: 0.9, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
                strokeStyle: 'solid' // 선의 스타일입니다
            });

            this.polyline.setMap(this.map);
        },
        check(){
            this.print();
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
            this.infowindow = new kakao.maps.InfoWindow({zIndex:1});

            // 선을 구성하는 좌표 배열입니다. 이 좌표들을 이어서 선을 표시합니다
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

        displayInfowindow(title, infowindow, marker, address, src) {
            var content =
                            '<div class="wrap3">' +
                            '    <div class="info3">' +
                            '        <div class="title3">' +
                                            title      +

                            '        </div>' +
                            '        <div class="body3">' +
                            '            <div class="img3">' +
                            '                <img src="https://i.ibb.co/gWBNgwm/image.jpg" width="73" height="70">' +
                            '           </div>' +
                            '            <div class="desc3">' +
                            '                <div class="ellipsis3">'+
                                            address
                            '</div>' +
                            '                <div class="jibun3 ellipsis3">(우) 63309 (지번) 영평동 2181</div>' +
                            '                <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>' +
                            '            </div>' +
                            '        </div>' +
                            '    </div>' +
                            '</div>';

            infowindow.setContent(content);
            infowindow.open(this.map, marker);
        },

        displayPlaces(places) {
            var listEl = document.getElementById('placesList'),
            menuEl = document.getElementById('menu_wrap'),
            fragment = document.createDocumentFragment(),
            bounds = new kakao.maps.LatLngBounds();

            // 검색 결과 목록에 추가된 항목들을 제거합니다
            this.removeAllChildNods(listEl);

            // 지도에 표시되고 있는 마커를 제거합니다
            this.removeMarker();
            var infowindow =  new kakao.maps.InfoWindow({
                zIndex:1,
            });

            var map = this.map;
            var func = this.displayInfowindow;
            var addRoad = this.addmy_road;
            for ( var i=0; i < places.length; i++ ) {

                // 마커를 생성하고 지도에 표시합니다
                var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
                    marker = this.addMarker(placePosition, i),
                    itemEl = this.getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다
                    console.log(itemEl)
                // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
                // LatLngBounds 객체에 좌표를 추가합니다
                bounds.extend(placePosition);

                // 마커와 검색결과 항목에 mouseover 했을때
                // 해당 장소에 인포윈도우에 장소명을 표시합니다
                // mouseout 했을 때는   인포윈도우를 닫습니다
                (function(marker, title, lat, lng, address) {
                    kakao.maps.event.addListener(marker, 'mouseover', function(){
                        func(title,infowindow,marker,address);

                    });


                    kakao.maps.event.addListener(marker, 'mouseout', function() {
                        infowindow.close();
                    });

                    kakao.maps.event.addListener(marker, 'click',  function(){
                        addRoad(title,lat,lng, "abc");
                    });

                    itemEl.onmouseover =  function () {
                        var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
                        infowindow.setContent(content);
                        infowindow.open(map, marker);

                    };
                    // itemEl.onclick = function(){
                    //     func(title, infowindow, marker);
                    // }

                    itemEl.onmouseout =  function () {
                        infowindow.close();
                    };
                })(marker, places[i].place_name, places[i].x, places[i].y, places[i].address_name);

                fragment.appendChild(itemEl);
            }
            // 검색결과 항목들을 검색결과 목록 Elemnet에 추가합니다
            listEl.appendChild(fragment);
            menuEl.scrollTop  =0;
            // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
            this.map.setBounds(bounds);
        },

        getListItem(index, places) {
            var el = document.createElement('li'),
            itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                        '<div class="info2">' +
                        '   <h5>' + places.place_name + '</h5>';

            if (places.road_address_name) {
                itemStr += '    <span>' + places.road_address_name + '</span>' +'&nbsp&nbsp'+
                            '   <span class="jibun gray">' +  places.address_name  + '</span>';
            } else {
                itemStr += '    <span>' +  places.address_name  + '</span>';
            }

            itemStr += '  <span class="tel">' + places.phone  + '</span>'+
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
                    image: markerImage,
                    title : title
                });
            marker.setMap(this.map); // 지도 위에 마커를 표출합니다
            this.markers.push(marker);  // 배열에 생성된 마커를 추가합니다
            console.log(this.markers)
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
        },

        addmy_road(title2, lat2, lng2, src){
            if(this.my_road_title.indexOf(title2)>0){
                alert("이미 경로에 포함되어있습니다.");
                return;
            }
            alert("추가되었습니다.");
            const road ={
                name: "sgs1159",
                title:title2,
                lat : lat2,
                lng: lng2,
                src: "https://i.ibb.co/gWBNgwm/image.jpg"
            }
            this.my_road_title.push(road.title);
            this.my_road.push(road);
            //this.makeLine();
        },
    }
};
</script>

<style>
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


/* .wrap3 {position: absolute;left: 0;bottom: 40px;width: 288px;height: 132px;margin-left: -144px;text-align: left;overflow: hidden;font-size: 12px;font-family: 'Malgun Gothic', dotum, '돋움', sans-serif;line-height: 1.5;} */
.wrap3 * {padding: 0;margin: 0;}
.wrap3 .info3 {width: 286px;height: 120px;border-radius: 5px;border-bottom: 2px solid #ccc;border-right: 1px solid #ccc;overflow: hidden;background: #fff;}
/* .wrap3 .info3:nth-child(1) {border: 0;box-shadow: 0px 1px 2px #888;} */
.info3 .title3 {height: 32px;background: #eee;border-bottom: 1px solid #ddd;text-align: center; font-size: 20px;font-weight: bold;}
.info3 .body3 {position: relative;overflow: hidden;}
.info3 .desc3 {position: relative;margin: 13px 0 0 90px;height: 75px;}
.desc2 .ellipsis3 {overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}
.desc2 .jibun3 {font-size: 11px;color: #888;margin-top: -2px;}
.info3 .img3 {position: absolute;top: 6px;left: 5px;width: 73px;height: 71px;border: 1px solid #ddd;color: #888;overflow: hidden;}
.info3:after {content: '';position: absolute;margin-left: -12px;left: 50%;bottom: 0;width: 22px;height: 12px;background: url('https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/vertex_white.png')}
.info3 .link3 {color: #5085BB;}
</style>
