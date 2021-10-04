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
      <v-toolbar-items class="hidden-sm-and-down" v-if="is_login===false">
      
      </v-toolbar-items>

      <v-toolbar-items class="hidden-sm-and-down" v-else>
        <v-btn flat to="/home" active-class="blue--text headline"><b>메인</b></v-btn>
        <v-btn flat @click.prevent="onClickMypage" active-class="blue--text headline"><b>마이페이지</b></v-btn>
        <v-btn flat to="/myinteresting" active-class="blue--text headline"><b>관심지역</b></v-btn>
        <v-btn flat to="/satisfactionmap" active-class="blue--text headline"><b>전국 만족도</b></v-btn>
        <v-btn flat @click.prevent="onClickLogout" active-class="blue--text headline"><b>로그아웃</b></v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { createInstance2} from "@/api/index.js";

export default {
  props: {
    goDark: {
      type: Boolean
    }
  },
  computed:{
    ...mapState([
      "is_login", "user_info"
    ])
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
      this.$confirm("로그아웃 하시겠습니까?").then(() => {
        this.$store
        .dispatch("LOGOUT")
        .then(() => {
          if (this.$route.path !== "/") this.$router.replace("/");
        })
        .catch(() => {
          console.log("로그아웃 에러입니다.");
        });
      })
    },
    onClickMypage(){
      const instance = createInstance2();

      instance.get("/tour/route/").then(
        (response) =>{
          console.log(response);
          this.$store.dispatch("SET_MY_ROAD", response.data).then(()=>{
            this.$router.replace("/mypage");
          
        })
      })
    }
  }
  
};
</script>

<style >
</style>
