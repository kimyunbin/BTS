<template>
  <v-container>
    <v-layout>
      <h1>키워드 검색 페이지</h1>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";


export default {
  name: "TeamMain",
  computed: {
    ...mapGetters([
      "select_place"
    ]),
  },
  mounted() {},
  
  created() {
    
  },
  data() {
    return {
      
    };
  },
  components: {
    
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
