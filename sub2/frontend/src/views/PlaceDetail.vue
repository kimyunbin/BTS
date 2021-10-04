<template>
  <div>
    <br><br>
    <v-layout class="title">
      <h6 data-aos="fade-up"><b>{{select_place}} 관광지</b></h6>
    </v-layout>

    <div v-if="touristSpots.length">
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
            <SpotComponents
              :item="item"
            />
          </template>
        </vue-horizontal-list>
      </section>
    </div>
    
    <div v-if="Accommodation.length">
      <br>
      <br>
      <h1 ><b>숙소</b></h1>
      <br>
      <section style="">
        <vue-horizontal-list :items="Accommodation" :options="options" >
          <template v-slot:nav-prev>
            <div><v-icon>arrow_back_ios</v-icon></div>
          </template>

          <template v-slot:nav-next>
            <div><v-icon>arrow_forward_ios</v-icon></div>
          </template>

          <template v-slot:default="{ item }">
            <SpotComponents
              :item="item"
            />
          </template>
        </vue-horizontal-list>
      </section>
    </div>

    <div v-if="Food.length">
      <br>
      <br>
      <h1><b>맛집</b></h1>
      <br>
      <section style="">
        <vue-horizontal-list :items="Food" :options="options" >
          <template v-slot:nav-prev>
            <div><v-icon>arrow_back_ios</v-icon></div>
          </template>

          <template v-slot:nav-next>
            <div><v-icon>arrow_forward_ios</v-icon></div>
          </template>

          <template v-slot:default="{ item }">
            <SpotComponents
              :item="item"
            />
          </template>
        </vue-horizontal-list>
      </section>
    </div>

    <div v-if="Sport.length">
      <br>
      <br>
      <h1><b>레포츠</b></h1>
      <br>
      <section style="">
        <vue-horizontal-list :items="Sport" :options="options" >
          <template v-slot:nav-prev>
            <div><v-icon>arrow_back_ios</v-icon></div>
          </template>

          <template v-slot:nav-next>
            <div><v-icon>arrow_forward_ios</v-icon></div>
          </template>

          <template v-slot:default="{ item }">
            <SpotComponents
              :item="item"
            />
          </template>
        </vue-horizontal-list>
      </section>
    </div>

    <div v-if="Culture.length">
      <br>
      <br>
      <h1><b>문화시설</b></h1>
      <br>
      <section style="">
        <vue-horizontal-list :items="Culture" :options="options" >
          <template v-slot:nav-prev>
            <div><v-icon>arrow_back_ios</v-icon></div>
          </template>

          <template v-slot:nav-next>
            <div><v-icon>arrow_forward_ios</v-icon></div>
          </template>

          <template v-slot:default="{ item }">
            <SpotComponents
              :item="item"
            />
          </template>
          </vue-horizontal-list>
        </section>
    </div>

  </div>
</template>

<script>
import { mapGetters } from "vuex";
import VueHorizontalList from "vue-horizontal-list";
import PlaceComponent from "@/components/PlaceComponent";
import SpotComponents from "@/components/SpotComponents";

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
    SpotComponents,
  },
  data() {
    return {
      options: {
        item: {
          padding: 10
        },
        map:{
          padding: 10
        },
        responsive: [
          { end: 576, size: 1 },
          { start: 576, end: 768, size: 2 },
          { start: 768, end: 992, size: 3 },
          { size: 4 },
        ],
        list: {
          windowed: 1200,
          padding: 10,
        },
        position: {
          start: 4,
        },
        autoplay: { play: true, repeat: true, speed: 2400 },
        hover:{
          cursor:"pointer"
        }
      },
      touristSpots: [],
      Accommodation: [],
      Food: [],
    };
  },
  created() {
    this.touristSpots =  this.$store.state.select_info.관광지
    this.Accommodation =  this.$store.state.select_info.숙박
    this.Food =  this.$store.state.select_info.음식
    this.Sport =  this.$store.state.select_info.레포츠
    this.Culture =  this.$store.state.select_info.문화시설
  },
  methods: {
  }
};
</script>

<style scoped>
h6{
  font-size: 50px;
}
.title{
  justify-content: center;
  align-items: center;

}
</style>
