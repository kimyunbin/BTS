<template>
  <div>
    
    <full-page ref="fullpage" :options="options">
      <div class="section">
        
        <v-container grid-list-xl>
          <br><br><br>
          <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-img
              lazy-src="https://picsum.photos/id/11/10/6"
              aspect-ratio="0.5" height="700" contain
              src="https://i.ibb.co/ZTgRrdG/image.png"
            ></v-img>
            <div>
              <h1 data-aos="fade-left"><b>당신이 찾는</b></h1><br>
              <h1 data-aos="fade-right"><b>당신이 만족하는</b></h1><br>
              <h1 data-aos="fade-left"><b>당신을 위한 서비스</b></h1>
            </div>
          </v-layout>

          <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <div class="s1_arrow">
              <div class="scroll-arrow"></div>
              <div class="scroll-arrow"></div>
              <div class="scroll-arrow"></div>
            </div>
          </v-layout>
        </v-container>
      </div>
      <div class="section">
        <v-container grid-list-xl>
          
          <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-img
              lazy-src="https://picsum.photos/id/11/10/6"
              aspect-ratio="0.5" height="700" contain
              src="https://i.ibb.co/whWcmfX/1.png"
            ></v-img>
            
              
          </v-layout>
          <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <div>
              <h1><b>원하는 지역을 찾아 자신만의 길로</b></h1>
            </div>
          </v-layout>
          <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <div class="s1_arrow">
              <div class="scroll-arrow"></div>
              <div class="scroll-arrow"></div>
              <div class="scroll-arrow"></div>
            </div>
          </v-layout>
        </v-container>
      </div>

      
        
      
      <div class="section">
        <div class="flex-container">
        <v-container>
          <v-layout row justify-center align-center wrap >
            <v-flex xs12 sm12 md6 lg6 xl6>
              <h2 class="pb-4 mb-4">
                <span><b>로그인</b></span>
              </h2>

              <v-text-field
                type="email"
                color="blue"
                background-color="transparent"
                name="email"
                v-model="member.username"
                label="E-mail"
                required
                @blur="$v.email.$touch()"
              ></v-text-field>
              <v-text-field
                :type="'password'"
                name="password"
                color="blue"
                background-color="transparent"
                v-model="member.password"
                label="비밀번호"
                @keyup.enter="confirm"
              ></v-text-field>
              <v-btn
                @click="confirm"
                type="submit"
                color="blue"
                class="white--text"
                :disabled="(member.username==''||member.password=='')"
                
              >로그인</v-btn>
              
              <v-btn to="/signup" color="green" class="white--text">회원가입</v-btn>
              <v-btn @click="clear" color="red" class="white--text">초기화</v-btn>
              
            </v-flex>
          </v-layout>
          
        </v-container>
          
        </div>
      </div>

      
    </full-page>
  </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import { validationMixin } from "vuelidate";
import { createInstance} from "@/api/index.js";
import { mapState } from "vuex";
import {
  required,
  maxLength,
  username,
} from "vuelidate/lib/validators";

  export default {
    mixins: [validationMixin],
  validations: {
    name: { required, maxLength: maxLength(8) },
    username: { required, username },
  },
  computed:{
    ...mapState(["user_info","is_login"]),
  },
  data() {
    return {
      name: "",
      member:{
        username: "",
        password: "",
      },
      options:{

      }
    };
  },
  methods: {
    submit() {
      
    },
    clear() {
      this.$v.$reset();
      this.member.username = "";
      this.member.password ="";
    },
    confirm() {
      localStorage.setItem("token", "");
      const instance = createInstance();
      instance.post("/accounts/login/", JSON.stringify(this.member))
        .then(
          (response) => {
            console.log(response);
            const decoded = jwt_decode(response.data.token);
            console.log(decoded);
            let token = response.data["token"];
            localStorage.setItem("token", token);
            this.$store.commit("SET_IS_LOGIN", true);
            this.$store.commit("SET_TOKEN", token);
            
            this.$store.commit("SET_USER_INFO", response.data.nickname);
            //const token2 = localStorage.getItem('token')
            //console.log(token2);
            this.$router.push("/home");
            
          }
        )
        .catch(() => {
          alert("에러발생!");
          //this.$router.push("/");
        });
      
    },
  },
  }
</script>

<style scoped>
/* body{background:#000; text-align:center;} */
.s1_arrow{display:inline-block; position:relative; top:28px; margin-left:-10px; text-align:center; animation:arrow_down 1.5s infinite;}
.scroll-arrow {width:25px; height:25px; border-right: 3px solid blue; border-bottom: 3px solid blue;
transform: rotate(45deg); -webkit-transform: rotate(45deg); -moz-transform: rotate(45deg); -o-transform: rotate(45deg);  -ms-transform: rotate(45deg);
animation: arrow-wave 1s infinite; animation-direction: alternate;}
.scroll-arrow:nth-child(1) {animation-delay: 0.1s;}
.scroll-arrow:nth-child(2) {margin-top:6px; animation-delay: 0.2s;}
.scroll-arrow:nth-child(3) {margin-top:6px; animation-delay: 0.3s;}
@keyframes arrow-wave {
0% {opacity: 0;}
50% {opacity: .5;}
100% {opacity: 1;}
}
@keyframes arrow_down{
0%{top:28px;}
50%{top:40px;}
100%{top:28px;}
}

.flex-container{
  width: 100%;
  height: 80vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-pack: center;
      -ms-flex-pack: center;
          justify-content: center;
}

html, body { height: 100%; }
body {
  background:radial-gradient(ellipse at center, rgba(255,254,234,1) 0%, rgba(255,254,234,1) 35%, #B7E8EB 100%);
  overflow: hidden;
}
body {
  background-image: #34495e;
}
.ocean { 
  height: 5%;
  width:100%;
  position:absolute;
  bottom:0;
  left:0;
  background: #015871;
}

.wave {
  background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/85486/wave.svg) repeat-x; 
  position: absolute;
  top: -198px;
  width: 6400px;
  height: 198px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) infinite;
  transform: translate3d(0, 0, 0);
}

.wave:nth-of-type(2) {
  top: -175px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) -.125s infinite, swell 7s ease -1.25s infinite;
  opacity: 1;
}

@keyframes wave {
  0% {
    margin-left: 0;
  }
  100% {
    margin-left: -1600px;
  }
}

@keyframes swell {
  0%, 100% {
    transform: translate3d(0,-25px,0);
  }
  50% {
    transform: translate3d(0,5px,0);
  }
}

</style>