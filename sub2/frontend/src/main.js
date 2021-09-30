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
import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false
const isProd = process.env.NODE_ENV === "production"

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@babel/polyfill'
import VueHtml2Canvas from 'vue-html2canvas';
import VueSimpleAlert from "vue-simple-alert";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueHtml2Canvas);
Vue.use(StoryblokVue)
library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false
Vue.use(SequentialEntrance);
Vue.use(VueSimpleAlert);

new Vue({
  router,
  store,
  render: h => h(App),
  created() {
    AOS.init();
  },
}).$mount('#app')


Vue.use(VueAnalytics, {
  id: 'UA-139190314-1',
  router,
  debug: {
    enabled: !isProd,
    sendHitTask: isProd
  }
})


