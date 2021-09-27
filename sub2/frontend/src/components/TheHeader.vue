<template>
  <div>
    <v-navigation-drawer v-model="drawer" absolute temporary app width="150" height="340">
      <v-list class="pt-4">
        <v-list-tile active-class="blue--text" to="/">
          <v-list-tile-content>
            <v-list-tile-title>메인</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile active-class="blue--text" to="/mypage">
          <v-list-tile-content>
            <v-list-tile-title>마이페이지</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile active-class="blue--text" to="/myinteresting">
          <v-list-tile-content>
            <v-list-tile-title>관심지역</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile active-class="blue--text" to="/login">
          <v-list-tile-content>
            <v-list-tile-title>로그인</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile active-class="blue--text" to="/signup">
          <v-list-tile-content>
            <v-list-tile-title>회원가입</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile active-class="blue--text" to="/contact">
          <v-list-tile-content>
            <v-list-tile-title></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar flat dense color="transparent">
      <v-toolbar-side-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title class="headline">
        <span class="font-weight-bold"><b>Best Trip Service</b></span>

      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn @click="changeTheme" depressed small icon class="hidden-md-and-up">
        <v-icon v-if="goDark==true">fas fa-sun</v-icon>
        <v-icon v-else>fas fa-moon</v-icon>
      </v-btn>
      <v-toolbar-items class="hidden-sm-and-down"  v-if="is_login === false">
        <v-btn flat to="/" active-class="blue--text headline"><b>메인</b></v-btn>
        <v-btn flat to="/mypage" active-class="blue--text headline"><b>마이페이지</b></v-btn>
        <v-btn flat to="/myinteresting" active-class="blue--text headline"><b>관심지역</b></v-btn>
        <v-btn flat to="/map" active-class="blue--text headline"><b>지도(임시)</b></v-btn>
        <v-btn flat to="/satisfactionmap" active-class="blue--text headline"><b>만족도(임시)</b></v-btn>
        <v-btn flat to="/login" active-class="blue--text headline"><b>로그인</b></v-btn>
        <v-btn flat to="/signup" active-class="blue--text headline"><b>회원가입</b></v-btn>
      </v-toolbar-items>

      <v-toolbar-items class="hidden-sm-and-down"  v-else>
        <v-btn flat to="/" active-class="blue--text headline"><b>메인</b></v-btn>
        <v-btn flat to="/mypage" active-class="blue--text headline"><b>마이페이지</b></v-btn>
        <v-btn flat to="/myinteresting" active-class="blue--text headline"><b>관심지역</b></v-btn>
        <v-btn flat to="/map" active-class="blue--text headline"><b>지도(임시)</b></v-btn>
        <v-btn flat to="/satisfactionmap" active-class="blue--text headline"><b>만족도(임시)</b></v-btn>
        <v-btn flat to="/" @click.prevent="onClickLogout" active-class="blue--text headline"><b>로그아웃</b></v-btn>
       
      </v-toolbar-items>

    </v-toolbar>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  props: {
    goDark: {
      type: Boolean
    }
  },
  computed:{
    ...mapState(["user_info", "is_login"])
  },
  data() {
    return {
      drawer: null
    };
  },
  methods: {
    changeTheme() {
      this.$emit("changeTheme", this.goDark);
    },
    onClickLogout() {
      let checkLogout = confirm("로그아웃 하시겠습니까?");
      console.log(checkLogout);
      if(checkLogout){
      this.$store
        .dispatch("LOGOUT")
        .then(() => {
          if (this.$route.path !== "/") this.$router.replace("/");
        })
        .catch(() => {
          console.log("로그아웃 에러입니다.");
        });
      }
    }
  }
};
</script>

<style >
</style>
