<template>
  <v-container>
    <v-layout>
      <h1 data-aos="fade-up"><b>{{select_place.title}} 관광 추천</b></h1>
    </v-layout>

    <v-layout justify-center align-center wrap class="mt-4 pt-2" data-aos="fade-up">
      <div>
      <p>즐길거리</p>
      
      </div>
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
