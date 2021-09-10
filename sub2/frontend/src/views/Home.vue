<template>
  <div id="app">
    <br>
    <br>
    <h1><b>차범희님을 위한 추천 여행지역</b></h1>
    <br>
    <section >
      <vue-horizontal-list :items="items" :options="options" >
        <template v-slot:nav-prev>
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <div class="item">
            <img
              :src="item.src"
              width="200"
              height="200"
              object-fit: cover
              style="cursor:pointer;"
            />
            <h5>{{ item.title }}</h5>
            <p>{{ item.content }}</p>
          </div>
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
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <div class="item">
            <img
              :src="item.src"
              width="200"
              height="200"
              object-fit: cover
              style="cursor:pointer;"
            />
            <h5>{{ item.title }}</h5>
            <p>{{ item.content }}</p>
          </div>
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
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <div class="item">
            <img
              :src="item.src"
              width="200"
              height="200"
              object-fit: cover
              style="cursor:pointer;"
            />
            <h5>{{ item.title }}</h5>
            <p>{{ item.content }}</p>
          </div>
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
          <div>👈</div>
        </template>

        <template v-slot:nav-next>
          <div>👉</div>
        </template>

        <template v-slot:default="{ item }">
          <div class="item">
            <img
              :src="item.src"
              width="200"
              height="200"
              object-fit: cover
              style="cursor:pointer;"
            />
            <h5>{{ item.title }}</h5>
            <p>{{ item.content }}</p>
          </div>
        </template>
      </vue-horizontal-list>
    </section>
  </div>
</template>

<script>
import VueHorizontalList from "vue-horizontal-list";

export default{
  name: "ServeDev",
  components: {
    VueHorizontalList,
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
        { title: "Item 0", content: "Content item with description", src: "https://i.ibb.co/sv0Cqg1/image.jpg"},
        { title: "Item 1", content: "Content item with description", src: "https://i.ibb.co/KmtrYTf/image.jpg"},
        { title: "Item 2", content: "Content item with description", src: "https://i.ibb.co/w6cC5MT/image.jpg"},
        { title: "Item 3", content: "Content item with description", src: "https://i.ibb.co/60yjckh/image.jpg"},
        { title: "Item 4", content: "Content item with description", src: "https://i.ibb.co/Z24FjMD/image.jpg"},
        { title: "Item 5", content: "Content item with description", src: "https://i.ibb.co/0V3grZZ/image.jpg"},
        { title: "Item 6", content: "Content item with description", src: "https://i.ibb.co/kBjW0Wg/image.jpg"},
        { title: "Item 7", content: "Content item with description", src: "https://i.ibb.co/StjhL5X/image.png"},
        { title: "Item 8", content: "Content item with description", src: "https://i.ibb.co/gWBNgwm/image.jpg"},
      ],

      maps: [
        { title: "map 0", content: "Content item with description", src: "https://i.ibb.co/y6M6JfT/map3.jpg"},
        { title: "map 1", content: "Content item with description", src: "https://i.ibb.co/0Y8M9jV/1.png"},
        { title: "map 2", content: "Content item with description", src: "https://i.ibb.co/PCqpd64/map4.jpg"},
        { title: "map 3", content: "Content item with description", src: "https://i.ibb.co/8YWZzfn/map2.jpg"},
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
      padding-left: 120px;
      padding-right: 120px;
    }
  }
  

</style>