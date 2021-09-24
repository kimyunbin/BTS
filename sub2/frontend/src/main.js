import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import StoryblokVue from 'storyblok-vue'
import VueAnalytics from 'vue-analytics'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import store from './store';
import AOS from 'aos';
import "aos/dist/aos.css";
import VueStar from 'vue-star'
Vue.config.productionTip = false
const isProd = process.env.NODE_ENV === "production"

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@babel/polyfill'
import VueHtml2Canvas from 'vue-html2canvas';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueHtml2Canvas);

new Vue({
  router,
  store,
  render: h => h(App),
  created() {
    AOS.init();
  },
}).$mount('#app')

Vue.use(StoryblokVue)
Vue.use(VueAnalytics, {
  id: 'UA-139190314-1',
  router,
  debug: {
    enabled: !isProd,
    sendHitTask: isProd
  }
})
