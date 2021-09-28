<template>
  <div>
    <br><br>
    <v-layout>
      <h1 data-aos="fade-up"><b>{{select_place}} 관광 추천</b></h1>
    </v-layout>

    <br>
    <br>
    <h1><b>즐길거리</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="touristSpots" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceFun
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>숙소</b></h1>
    <br>
    <section style="">
      <vue-horizontal-list :items="stays" :options="options" >
        <template v-slot:nav-prev>
          <div><v-icon>arrow_back_ios</v-icon></div>
        </template>

        <template v-slot:nav-next>
          <div><v-icon>arrow_forward_ios</v-icon></div>
        </template>

        <template v-slot:default="{ item }">
          <PlaceStay
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>

    <br>
    <br>
    <h1><b>맛집</b></h1>
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
          <PlaceFood
            :item="item"
          />
        </template>
      </vue-horizontal-list>
    </section>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import VueHorizontalList from "vue-horizontal-list";
import PlaceComponent from "@/components/PlaceComponent";
import PlaceFun from "@/components/PlaceFun";
import PlaceStay from "@/components/PlaceStay";
import PlaceFood from "@/components/PlaceFood";

export default {
  name: "TeamMain",
  computed: {
    ...mapGetters([
      "select_place"
    ]),
  },
  components: {
    VueHorizontalList,
    PlaceComponent,
    PlaceFun,
    PlaceStay,
    PlaceFood
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
      stays: [
        { id:"1", title: "Item 8", content: "Content item with description", src: "https://i.ibb.co/sv0Cqg1/image.jpg"},
        { id:"2", title: "Item 7", content: "Content item with description", src: "https://i.ibb.co/KmtrYTf/image.jpg"},
        { id:"3", title: "Item 6", content: "Content item with description", src: "https://i.ibb.co/w6cC5MT/image.jpg"},
        { id:"4", title: "Item 5", content: "Content item with description", src: "https://i.ibb.co/60yjckh/image.jpg"},
        { id:"5", title: "Item 4", content: "Content item with description", src: "https://i.ibb.co/Z24FjMD/image.jpg"},
        { id:"6", title: "Item 3", content: "Content item with description", src: "https://i.ibb.co/0V3grZZ/image.jpg"},
        { id:"7", title: "Item 2", content: "Content item with description", src: "https://i.ibb.co/kBjW0Wg/image.jpg"},
        { id:"8", title: "Item 1", content: "Content item with description", src: "https://i.ibb.co/StjhL5X/image.png"},
        { id:"9", title: "Item 0", content: "Content item with description", src: "https://i.ibb.co/gWBNgwm/image.jpg"},
      ],
      touristSpots: [],
    };
  },
  created() {
    this.touristSpots =  this.$store.state.select_info.관광지
  },
  methods: {
    check(){
      alert(this.select_place.title);
    }
  }
};
</script>

<style scoped>

</style>
