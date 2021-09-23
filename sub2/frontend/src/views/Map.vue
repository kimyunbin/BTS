<template>
    <div>
        <div class="map_wrap">
            <div id="map" style="width:100%;height:100%;position:relative;overflow:hidden;"></div>
            
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

        <div v-if="myRoad.length">
            <v-flex
                v-for="(road, idx) in this.myRoad"
                :key="idx"
                xs12 sm6 md4 lg3 xl3
            >
                <h3>{{road.title}}</h3>
                <h3>{{road.lat}}</h3>
                <h3>{{road.lng}}</h3>
                <br>
            </v-flex>
        </div>
        <v-btn @click="makeLine()"></v-btn>
    </div>
</template>

<script>
export default {
    created(){
        
    },
    computed:{
        
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
            myRoad :[
            
            ],
        };
    },
    methods: {
        makeLine(){
            
            var linePath = [];
            
            for(var i = 0; i< this.myRoad.length; i++){
                linePath.push( new kakao.maps.LatLng(this.myRoad[i].lng,this.myRoad[i].lat));
            }
            
            var polyline = new kakao.maps.Polyline({
                path: linePath, // 선을 구성하는 좌표배열 입니다
                strokeWeight: 5, // 선의 두께 입니다
                strokeColor: '#0000FF', // 선의 색깔입니다
                strokeOpacity: 0.9, // 선의 불투명도 입니다 1에서 0 사이의 값이며 0에 가까울수록 투명합니다
                strokeStyle: 'solid' // 선의 스타일입니다
            });
            polyline.setMap(this.map);  
        },
        check(){
            console.log(this.myRoad);
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

        displayInfowindow(title, infowindow, marker) {
            var content = 
                            '<div class="wrap">' + 
                            '    <div class="info2">' + 
                            '        <div class="title" style="padding:20px;z-index:1;">' + 
                                            title      + 
                            
                            '        </div>' + 
                            '        <div class="body">' + 
                            '        </div>' + 
                            '    </div>' +    
                            '</div>';

                        infowindow.setContent(content);
                        infowindow.open(this.map, marker);


            //console.log("추가되었습니다.");
            //alert("추가되었습니다.");
            //this.myRoad.push(title);
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
            var infowindow =  new kakao.maps.InfoWindow({
                zIndex:1,
            });
            
            var map = this.map;
            var func = this.displayInfowindow;
            var addRoad = this.addMyRoad;
            for ( var i=0; i < places.length; i++ ) {
                
                // 마커를 생성하고 지도에 표시합니다
                var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
                    marker = this.addMarker(placePosition, i), 
                    itemEl = this.getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

                // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
                // LatLngBounds 객체에 좌표를 추가합니다
                bounds.extend(placePosition);

                // 마커와 검색결과 항목에 mouseover 했을때
                // 해당 장소에 인포윈도우에 장소명을 표시합니다
                // mouseout 했을 때는   인포윈도우를 닫습니다
                (function(marker, title, lat, lng) {
                    kakao.maps.event.addListener(marker, 'mouseover', function(){
                        func(title,infowindow,marker);
                    });
                    
                    
                    kakao.maps.event.addListener(marker, 'mouseout', function() {
                        infowindow.close();
                    });

                    kakao.maps.event.addListener(marker, 'click',  function(){
                        console.log(marker);
                        addRoad(title,lat,lng);
                    });

                    itemEl.onmouseover =  function () {
                        var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';
                        infowindow.setContent(content);
                        infowindow.open(map, marker);
                        
                    };
                    itemEl.onclick = function(){
                        func(title, infowindow, marker);
                    }

                    itemEl.onmouseout =  function () {
                        infowindow.close();
                    };
                })(marker, places[i].place_name, places[i].x, places[i].y);
                
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
        },

        addMyRoad(title2, lat2, lng2){
            alert("추가되었습니다.");
            const road ={
                title:title2,
                lat : lat2,
                lng: lng2
            }  
            this.myRoad.push(road);
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


</style>