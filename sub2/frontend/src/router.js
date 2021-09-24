import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Meta from 'vue-meta'
import { mapGetters } from "vuex";
Vue.use(Router);
Vue.use(Meta)

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
  routes: [{
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/myinteresting",
      name: "myinteresting",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/MyInteresting.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Login.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/SignUp.vue")
    },
    {
      path: "/signup2",
      name: "signup2",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/signup/SignUp2.vue")
    },
    {
      path: "/signupquestion",
      name: "signupquestion",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/SignUpQuestion.vue")
    },
    {
      path: "*",
      name: "Error",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Error.vue")
    },
    {
      path: "/placedetail",
      name: "placedetail",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/PlaceDetail.vue")
    },
    {
      path: "/keyword",
      name: "keyword",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Keyword.vue")
    },
    {
      path: "/map",
      name: "map",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/Map.vue")
    },
    {
      path: "/infodetail",
      name: "infodetail",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/InfoDetail.vue")
    },
    {
      path: "/reviewwrite",
      name: "reviewwrite",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/ReviewWrite.vue")
    },
    {
      path: "/jeju",
      name: "jeju",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Jeju.vue")
    },
    {
      path: "/busan",
      name: "busan",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Busan.vue")
    },
    {
      path: "/gangwon",
      name: "gangwon",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Gangwon.vue")
    },
    {
      path: "/gyeonggi",
      name: "gyeonggi",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Gyeonggi.vue")
    },
    {
      path: "/seoul",
      name: "seoul",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Seoul.vue")
    },
    {
      path: "/incheon",
      name: "incheon",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Incheon.vue")
    },
    {
      path: "/gyeongbuk",
      name: "gyeongbuk",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Gyeongbuk.vue")
    },
    {
      path: "/chungbuk",
      name: "chungbuk",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Chungbuk.vue")
    },
    {
      path: "/sejong",
      name: "sejong",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Sejong.vue")
    },
    {
      path: "/daejeon",
      name: "daejeon",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Daejeon.vue")
    },
    {
      path: "/chungnam",
      name: "chungnam",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Chungnam.vue")
    },
    {
      path: "/daegu",
      name: "daegu",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Daegu.vue")
    },
    {
      path: "/ulsan",
      name: "ulsan",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Ulsan.vue")
    },
    {
      path: "/gyeongnam",
      name: "gyeongnam",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Gyeongnam.vue")
    },
    {
      path: "/jeonbuk",
      name: "jeonbuk",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Jeonbuk.vue")
    },
    {
      path: "/gwangju",
      name: "gwangju",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Gwangju.vue")
    },
    {
      path: "/jeonnam",
      name: "jeonnam",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/satisfaction/Jeonnam.vue")
    },
    {
      path: "/otherroad",
      name: "otherroad",
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/OtherRoad.vue")
    },
  ]
});
