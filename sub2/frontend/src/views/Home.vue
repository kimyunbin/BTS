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
    </v-layout>
    <br><br><br>
    <h1><b>차범희님을 위한 추천 여행지역</b></h1>
    <br>
    <section>
      
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
    <h1><b>다른 유저가 갔던 여행 경로 추천</b></h1>
    <br>
    <section style="">
      <v-btn round dark @click="move('최신')" v-b-tooltip.hover title="click!" >
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
      </v-btn>
      
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
export default{
  name: "ServeDev",
  components: {
    VueHorizontalList,
    PlaceComponent
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
    };
  },
  methods: {
    move(subject){
      alert(subject);
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
  

</style>