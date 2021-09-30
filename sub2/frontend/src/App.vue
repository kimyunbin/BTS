<template>
  <v-app>
    <v-content>
      <v-container align-center>
        <TheHeader />

        <transition
          name="router-animation"
          mode="out-in"
          enter-active-class="animated fadeIn fast"
          leave-active-class="animated fadeOut faster"
        >
          <router-view></router-view>
        </transition>
      </v-container>
    </v-content>
    <TheFooter/>
  </v-app>
</template>

<script>
import Vue from "vue";
import TheHeader from "./components/TheHeader";
import TheFooter from "./components/TheFooter";
import Vuex from 'vuex'
import Vuetify from 'vuetify'
import Vuetify2 from 'vuetify/lib'
Vue.use(Vuex);
Vue.use(Vuetify);
Vue.use(Vuetify2);

export default {
  name: "App",
  
  components: {
    TheHeader,
    TheFooter
  },
  data() {
    return { 

    };
  },
  methods: {
    
  }
};
</script>
<style>
@import "https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css";
</style>
