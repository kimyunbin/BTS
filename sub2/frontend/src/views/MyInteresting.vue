<template>
    <div>
    <br><br>
    <v-layout>
      <h1 data-aos="fade-up"><b>관심spot 리스트</b></h1>
    </v-layout>
    <v-layout col data-aos="fade-up">
      <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
        <div>
          <WishDetail
            v-for="(wishDetail,key) in wishlist"
            :key = key
            :wishDetail = wishDetail
          />
        </div>
      </v-layout>
    </v-layout>
    </div>
</template>

<script>
import WishDetail from "@/components/WishDetail";
import { mapGetters, mapState } from "vuex";


export default {
  name:'MyInteresting',
  components: {
    WishDetail,
  },
  data() {
    return {
      wishDetails: [
        {
          title: '지도 왜 마커 안찍힘?',
          img: 'https://i.ibb.co/StjhL5X/image.png',
          reviewCnt: 5,
          rating: 3,
          address:'광주 수완지구 싸피-26번지',
          tel:'062-4533-0093'
        },
        {
          title: '조순님 살려주세요',
          img: 'https://i.ibb.co/gWBNgwm/image.jpg',
          reviewCnt: 10,
          rating: 4,
          address:'의정부 부대찌개구 싸피-27번지',
          tel:'031-8724-4774'
        },
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
  }
};
</script>

<style scoped>
</style>
