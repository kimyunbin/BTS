<template>
    <div>
    <br><br>
    <v-layout>
      <h1 data-aos="fade-up"><b>관심지역</b></h1>
    </v-layout>
    <v-layout col data-aos="fade-up">
      <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
        <div v-if="wishlist.length">
          <WishDetail
            v-for="(wishDetail,key) in wishlist"
            :key = key
            :wishDetail = wishDetail
          />
        </div>
        <div v-else>관심지역이 없습니다</div>
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
