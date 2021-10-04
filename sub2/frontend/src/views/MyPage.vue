<template>
  <div>
    <br><br>
    <v-layout>
      <h1 data-aos="fade-up"><b>000님의 마이페이지</b></h1>
    </v-layout>
    <br>
    <br>
    <h1><b>내가 직접 만든 여행코스</b></h1>
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
    <h1><b>찜한 여행코스</b></h1>
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
          <PlaceWish
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
import PlaceWish from "@/components/PlaceWish";
import { mapGetters, mapState } from "vuex";

export default {
  name: 'MyPage',
  components: {
    VueHorizontalList,
    PlaceComponent,
    PlaceWish,
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
  computed: {
  ...mapState([
    "wishlist",
    ]),
  },
  created() {
    this.$store.dispatch("GET_WISHLIST")
  },
  methods: {
    goWishList(){
        this.$router.push("/myinteresting");
    }
  },
  }
</script>

<style>

</style>
