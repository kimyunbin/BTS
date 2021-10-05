import Vue from "vue";
import Vuex from "vuex";
import jwt_decode from "jwt-decode";
import createPersistedState from "vuex-persistedstate";
import { findById } from "@/api/user.js";
import { createInstance2 } from "@/api/index.js";
import { createInstance3 } from "@/api/index.js";

import thumbnail from '../assets/json/thumbnail.json'

Vue.use(Vuex);

// const BASE_URL = "http://j5c203.p.ssafy.io/api/"

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    is_login: false, // 로그인 여부
    user_info: null, // 현재 로그인된 유저정보
    token: "",
    select_place: null, //선택 지역장소 이름
    select_info: null, // 선택 정보(즐길거리, 숙소, 맛집) 들이 들어가 있는 것들
    select_detail:null, //선택 spot장소의 좌표 등 세부정보
    other_road: [], // 다른 사람들의 경로
    select_road: {}, // Home.vue에서 선택된 경로
    select_map: null, //svg에서 선택된 경로
    tour_detail: [],
    tour_image:[],
    recom_area: [], // Home.vue에서 보여주는 추천지역
    satis_area: [], // 만족도 높은 순 지역 결과
    gender_recom_area: [], // Home.vue에서 보여주는 성별 별 추천지역
    traveler_recom_area: [], //Home.vue에서 보여주는 다른유저가 추천하는 추천지역
    budget_recom_area: [],//Home.vue에서 보여주는 예산 별 추천지역
    companion_recom_area: [],//Home.vue에서 보여주는 동행자별 추천지역
    reviews: [],
    select_like: Boolean,
    wishlist: [],
    my_road: [],
    my_wish_road:[],
  },

  getters: {
    user_info(state) {
      return state.user_info;
    },
    token(state) {
      return state.token;
    },
    select_place(state) {
      return state.select_place;
    },
    select_info(state) {
      return state.select_info;
    },
    select_detail(state) {
      return state.select_detail;
    },
    other_road(state) {
      return state.other_road;
    },
    my_road(state) {
      return state.my_road;
    },
    my_wish_road(state) {
      return state.my_wish_road;
    },
    select_road(state) {
      return state.select_road;
    },
    select_budget(state) {index
      return state.budget;
    },
    select_travelers(state) {
      return state.travelers;
    },
    select_companion(state) {
      return state.companion;
    },
    select_transportations(state) {
      return state.transportations;
    },
    select_selection(state) {
      return state.selection;
    },
    select_activity(state) {
      return state.activity;
    },
    select_user_signup(state) {
      return state.user_signup;
    },
    select_map(state) {
      return state.select_map;
    },
    tour_detail(state) {
      return state.tour_detail;
    },
    tour_imaget(state) {
      return state.tour_image;
    },
    get_recommend_area(state) {
      return state.recom_area;
    },
    get_satis_area(state) {
      return  state.satis_area;
    },
    get_gender_recom_area(state) {
      return state.gender_recom_area;
    },
    get_traveler_recom_area(state) {
      return state.traveler_recom_area;
    },
    get_budget_recom_area(state) {
      return state.budget_recom_area;
    },
    get_companion_recom_area(state) {
      return state.companion_recom_area;
    },
    get_review(state) {
      return state.reviews;
    },
    get_select_like(state) {
      return state.select_like;
    },
    get_wishlist(state) {
      return state.wishlist
    }
  },
  mutations: {
    SET_IS_LOGIN(state, is_login) {
      state.is_login = is_login;
    },
    SET_USER_INFO(state, user_info) {
      state.is_login = true;
      state.user_info = null;
      state.user_info = user_info;
    },
    SET_TOKEN(state, token) {
      state.token = token;
    },
    SET_IS_LOGOUT(state) {
      state.is_login = false;
      state.user_info = null;
      state.my_road = [];
      state.my_wish_road = [];
    },
    SET_SELECT_PLACE(state, data) {
      state.select_place = data;
    },
    SET_SELECT_INFO(state, data) {
      state.select_info = data;
    },
    SET_SELECT_DETAIL(state, data) {
      state.select_detail = data;
    },
    SET_SELECT_ROAD(state, data) {
      state.select_road = data;
    },
    CLEAR_OTHER_ROAD(state) {
      state.other_road = [];
    },
    SET_SELECT_BUDGET(state, data) {
      state.budget = data;
    },
    SET_SELECT_TRAVELERS(state, data) {
      state.travelers = data;
    },
    SET_SELECT_COMPANION(state, data) {
      state.companion = data;
    },
    SET_SELECT_TRANSPORTATIONS(state, data) {
      state.transportations = data;
    },
    SET_SELECT_SELECTION(state, data) {
      state.selection = data;
    },
    SET_SELECT_ACTIVITY(state, data) {
      state.activity = data;
    },
    SET_SELECT_USERSIGNUP(state, data) {
      state.user_signup = data;
    },
    SET_SELECT_MAP(state, data) {
      state.select_map = data;
    },
    SET_TOUR_DETAIL(state, data) {
      state.tour_detail = data;
    },
    SET_TOUR_IMAGE(state, data) {
      state.tour_image = data;
    },
    GET_RECOMMEND_AREA(state, data) {
      state.recom_area = data;
    },
    SATIS_AREA(state, data) {
      state.satis_area = data;
    },
    SET_OTHER_ROAD(state, data) {
      state.other_road = data;
    },
    SET_MY_ROAD(state, data) {
      state.my_road = data;
    },
    SET_MY_WISH_ROAD(state, data) {
      state.my_wish_road = data;
    },
    GET_GENDER_RECOMMEND_AREA(state, data) {
      state.gender_recom_area = data;
    },
    GET_TRAVELER_RECOMMEND_AREA(state, data) {
      state.traveler_recom_area = data;
    },
    GET_BUDGET_RECOMMEND_AREA(state, data) {
      state.budget_recom_area = data;
    },
    GET_COMPANION_RECOMMEND_AREA(state, data) {
      state.companion_recom_area = data;
    },
    GET_REVIEW(state, data) {
      state.reviews = data;
    },
    SET_SELECT_LIKE(state, data) {
      state.select_like = data;
    },
    GET_WISHLIST(state, data) {
      state.wishlist = data;
    }
  },
  //////////////////////////////////////////
  actions: {
    async GET_USER_INFO({ commit }, token) {
      let decode = jwt_decode(token);
      await findById(
        decode.username,
        response => {
          if (response.data.message === "success") {
            commit("SET_IS_LOGIN", true);
            commit("SET_TOKEN", token);
          } else {
            console.log("유저 정보 없음!!");
          }
        },
        error => {
          console.log(error);
        }
      );
    },

    LOGOUT({ commit }) {
      commit("SET_IS_LOGOUT");
      localStorage.removeItem("token");
    },

    SET_SELECT_PLACE(context, payload) {
      this.state.select_place = {};
      context.commit("SET_SELECT_PLACE", payload);
    },
    async SET_SELECT_INFO(context, payload) {
      // this.state.select_info = {};
      const instance = createInstance3()
      const response = await instance.get(`/tour/detail/?code=${payload}`)
      // console.log(response.data)
      context.commit("SET_SELECT_INFO", response.data);
    },
    SET_SELECT_DETAIL(context, payload) {
      // this.state.select_detail = {};
      context.commit("SET_SELECT_DETAIL", payload);
    },
    SET_SELECT_ROAD(context, payload) {
      this.select_road = {};
      context.commit("SET_SELECT_ROAD", payload);
    },
    CLEAR_OTHER_ROAD(context) {
      this.select_road = {};
      context.commit("CLEAR_OTHER_ROAD");
    },
    SET_SELECT_USERSIGNUP(context, payload) {
      this.state.user_signup = {};
      context.commit("SET_SELECT_USERSIGNUP", payload);
    },
    SET_SELECT_BUDGET(context, payload) {
      this.state.budget = {};
      context.commit("SET_SELECT_BUDGET", payload);
    },
    SET_SELECT_TRAVELERS(context, payload) {
      this.state.travelers = {};
      context.commit("SET_SELECT_TRAVELERS", payload);
    },
    SET_SELECT_COMPANION(context, payload) {
      this.state.companion = {};
      context.commit("SET_SELECT_COMPANION", payload);
    },
    SET_SELECT_TRANSPORTATIONS(context, payload) {
      this.state.transportations = {};
      context.commit("SET_SELECT_TRANSPORTATIONS", payload);
    },
    SET_SELECT_SELECTION(context, payload) {
      this.state.selection = {};
      context.commit("SET_SELECT_SELECTION", payload);
    },
    SET_SELECT_ACTIVITY(context, payload) {
      this.state.activity = {};
      context.commit("SET_SELECT_ACTIVITY", payload);
    },
    SET_SELECT_MAP(context, payload) {
      this.state.select_map = null;
      context.commit("SET_SELECT_MAP", payload);
    },
    SET_TOUR_DETAIL(context, payload) {
      this.state.tour_detail = null;
      context.commit("SET_TOUR_DETAIL", payload);
    },
    SET_TOUR_IMAGE(context, payload) {
      this.state.tour_image = null;
      context.commit("SET_TOUR_IMAGE", payload);
      // 메인페이지 추천지역 불러오기
    },
    SET_OTHER_ROAD(context, paylaod) {
      this.state.other_road = [];
      context.commit("SET_OTHER_ROAD", paylaod);
    },
    SET_MY_ROAD(context, paylaod) {
      this.state.my_road = [];
      context.commit("SET_MY_ROAD", paylaod);
    },
    SET_MY_WISH_ROAD(context, paylaod) {
      this.state.my_road = [];
      context.commit("SET_MY_WISH_ROAD", paylaod);
    },
    async GET_RECOMMEND_AREA(context) {
      const instance = createInstance2()
      const response = await instance.get("/accounts/recommendcity/")
      // console.log(response.data.main[0].country, 'axios')
      const satis_area = response.data.main[0].country
      context.commit("SATIS_AREA" ,satis_area)
      let data = []
      for (let i = 0; i < 10; i++) {
        const state = response.data.main[0].country[i].state;
        const name = response.data.main[0].country[i].city;
        var imgurl = null
        // 여기서 지역 확인 후 imgurl 넣어줘야함
        for (let index = 0; index < thumbnail.data.length; index++) {
          const state_ch = thumbnail.data[index].state;
          if (state_ch == state) {
            // console.log(state,'state')
            for (let index2 = 0; index2 < thumbnail.data[index].city.length; index2++) {
              const city_ch = thumbnail.data[index].city[index2].name;

              if (city_ch == name) {
                imgurl = thumbnail.data[index].city[index2].url
                // console.log(imgurl,'img')
                break
              }
            }
            break
          }
        }
        const input =
        {
          'state': state,
          'name' : name,
          'imgurl' : imgurl
        }
        // console.log(input, 'input')
        data.push(input)
      }
      // console.log(data, '3')
      context.commit("GET_RECOMMEND_AREA", data);
    },
    async GET_OTHER_RECOMMEND_AREA(context) {
      const instance = createInstance2()
      const response = await instance.get("/tour/city/")
      console.log(response.data)
      // 여기가 gender부분
      // console.log(response.data.gender,'gender')
      let gender_data = []
      for (let i = 0; i < 10; i++) {
        const gender_state = response.data.gender[i].state;
        const gender_name = response.data.gender[i].city;
        var g_imgurl = null
        for (let index = 0; index < thumbnail.data.length; index++) {
          const state_ch = thumbnail.data[index].state;
          if (state_ch == gender_state) {
            // console.log(state,'state')
            for (let index2 = 0; index2 < thumbnail.data[index].city.length; index2++) {
              const city_ch = thumbnail.data[index].city[index2].name;

              if (city_ch == gender_name) {
                g_imgurl = thumbnail.data[index].city[index2].url
                // console.log(imgurl,'img')
                break
              }
            }
            break
          }
        }
        const gender_input =
        {
          'state': gender_state,
          'name' : gender_name,
          'imgurl' : g_imgurl
        }
        // console.log(gender_input, 'gender_input')
        gender_data.push(gender_input)
      }
      context.commit("GET_GENDER_RECOMMEND_AREA", gender_data);

      // 여기가 traveler부분
      // console.log(response.data.traveler,'traveler')
      let traveler_data = []
      for (let i = 0; i < 10; i++) {
        const traveler_state = response.data.traveler[i].state;
        const traveler_name = response.data.traveler[i].city;
        var t_imgurl = null
        for (let index = 0; index < thumbnail.data.length; index++) {
          const state_ch = thumbnail.data[index].state;
          if (state_ch == traveler_state) {
            // console.log(state,'state')
            for (let index2 = 0; index2 < thumbnail.data[index].city.length; index2++) {
              const city_ch = thumbnail.data[index].city[index2].name;

              if (city_ch == traveler_name) {
                t_imgurl = thumbnail.data[index].city[index2].url
                // console.log(imgurl,'img')
                break
              }
            }
            break
          }
        }
        const traveler_input =
        {
          'state': traveler_state,
          'name' : traveler_name,
          'imgurl' : t_imgurl
        }
        // console.log(traveler_input, 'traveler_input')
        traveler_data.push(traveler_input)
      }
      context.commit("GET_TRAVELER_RECOMMEND_AREA", traveler_data);

      // 여기가 budget 부분
      let budget_data = []
      for (let i = 0; i < 10; i++) {
        const budget_state = response.data.budget[i].state;
        const budget_name = response.data.budget[i].city;
        var b_imgurl = null
        for (let index = 0; index < thumbnail.data.length; index++) {
          const state_ch = thumbnail.data[index].state;
          if (state_ch == budget_state) {
            // console.log(state,'state')
            for (let index2 = 0; index2 < thumbnail.data[index].city.length; index2++) {
              const city_ch = thumbnail.data[index].city[index2].name;

              if (city_ch == budget_name) {
                b_imgurl = thumbnail.data[index].city[index2].url
                // console.log(imgurl,'img')
                break
              }
            }
            break
          }
        }
        const budget_input =
        {
          'state': budget_state,
          'name' : budget_name,
          'imgurl' : b_imgurl
        }
        // console.log(traveler_input, 'traveler_input')
        budget_data.push(budget_input)
      }
      context.commit("GET_BUDGET_RECOMMEND_AREA", budget_data);

      // 여기가 companinon 부분
      let companion_data = []
      for (let i = 0; i < 10; i++) {
        const companion_state = response.data.companion[i].state;
        const companion_name = response.data.companion[i].city;
        var c_imgurl = null
        for (let index = 0; index < thumbnail.data.length; index++) {
          const state_ch = thumbnail.data[index].state;
          if (state_ch == companion_state) {
            // console.log(state,'state')
            for (let index2 = 0; index2 < thumbnail.data[index].city.length; index2++) {
              const city_ch = thumbnail.data[index].city[index2].name;

              if (city_ch == companion_name) {
                c_imgurl = thumbnail.data[index].city[index2].url
                // console.log(imgurl,'img')
                break
              }
            }
            break
          }
        }
        const companion_input =
        {
          'state': companion_state,
          'name' : companion_name,
          'imgurl' : c_imgurl
        }
        // console.log(traveler_input, 'traveler_input')
        companion_data.push(companion_input)
      }
      context.commit("GET_COMPANION_RECOMMEND_AREA", companion_data);
    },
    // 해당 spot 리뷰데이터 불러오기
    async GET_REVIEW(context, Spok_pk) {
      const instance = createInstance2()
      const response = await instance.get(`/tour/detail/${Spok_pk}/`)
      console.log(response.data,'review')
      context.commit("GET_REVIEW", response.data.review)
      context.commit("SET_SELECT_LIKE",response.data.follow)
    },
    // 해당 spot 리뷰데이터 작성하기
    async WRITE_REVIEW(context, data) {
      const instance = createInstance2()
      const response = await instance.post(`/tour/detail/${data.Spok_pk}/`, data.data)
      console.log(response.data)
    },
    // Spot 좋아요
    async SPOT_LIKE(context, Spok_pk) {
      const instance = createInstance2()
      const response = await instance.post(`/accounts/follow/${Spok_pk}/`)
      console.log(response.data)
      context.commit("SET_SELECT_LIKE",response.data.status)
    },
    // 위시리스트(관심Spot) 불러오기
    async GET_WISHLIST(context) {
      const instance = createInstance2()
      const response = await instance.get("/accounts/wishlist/")
      //console.log(response.data)
      context.commit("GET_WISHLIST",response.data.data)
    }
  }
});
