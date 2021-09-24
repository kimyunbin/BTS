import Vue from "vue";
import Vuex from "vuex";
import jwt_decode from "jwt-decode";
import createPersistedState from "vuex-persistedstate";
import { findById } from "@/api/user.js";
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    is_login: false, // 로그인 여부
    user_info: null, //현재 로그인된 유저정보
    token: "",
    select_place: null, //선택 장소
    select_info: null, // 선택 정보(즐길거리, 숙소, 맛집)
    other_road: [], // 다른 사람들의 경로
    select_road: [], // Home.vue에서 선택된 경로
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
    other_road(state) {
      return state.other_road;
    },
    select_road(state) {
      return state.select_road;
    },
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
    },
    SET_SELECT_PLACE(state, data) {
      state.select_place = data;
    },
    SET_SELECT_INFO(state, data) {
      state.select_info = data;
    },
    SET_SELECT_ROAD(state, data) {
      state.select_road = data;
    },
    CLEAR_OTHER_ROAD(state) {
      state.other_road = [];
    },
  },
  actions: {
    async GET_USER_INFO({ commit }, token) {
      let decode = jwt_decode(token);
      await findById(
        decode.memberEmail,
        response => {
          if (response.data.message === "success") {
            commit("SET_IS_LOGIN", response.data.memberInfo);
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
      localStorage.removeItem("access-token");
    },

    SET_SELECT_PLACE(context, payload) {
      this.state.select_place = {};
      context.commit("SET_SELECT_PLACE", payload);
    },
    SET_SELECT_INFO(context, payload) {
      this.state.select_info = {};
      context.commit("SET_SELECT_INFO", payload);
    },
    SET_SELECT_ROAD(context, payload) {
      this.select_road = [];
      context.commit("SET_SELECT_ROAD", payload);
    },
    CLEAR_OTHER_ROAD(context) {
      this.select_road = [];
      context.commit("CLEAR_OTHER_ROAD");
    }
  }
});
