import Vue from "vue";
import Vuex from "vuex";
import jwt_decode from "jwt-decode";
import createPersistedState from "vuex-persistedstate";
import { findById } from "@/api/user.js";
import { createInstance } from "../api/index";
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    is_login: false, // 로그인 여부
    user_info: null, // 현재 로그인된 유저정보
    token: "",
  },

  getters: {
    userInfo(state) {
      return state.user_info;
    },
    getToken(state) {
      return state.token;
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
  }
});
