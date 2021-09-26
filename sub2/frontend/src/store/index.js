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
    user_info: null, // 현재 로그인된 유저정보
    token: "",
    select_place: null, //선택 장소
    select_info: null , // 선택 정보(즐길거리, 숙소, 맛집)
    budget: '',
    travelers: '',
    companion: '',
    transportations: '',
    selection: '',
    activity: '',
    user_signup: null,
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
    select_budget(state) {
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
    SET_SELECT_BUDGET(state, data) {
      alert(data);
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
    SET_SELECT_USERSIGNUP(context, payload) {
      this.state.user_signup = {};
      context.commit("SET_SELECT_USERSIGNUP", payload);
    },
    SET_SELECT_BUDGET(context, payload) {
      this.state.budget = {};
      alert(payload)
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
  }
});
