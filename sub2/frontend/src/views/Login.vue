<template>
  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

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
          ></v-text-field>
          <v-btn
            @click="confirm"
            type="submit"
            color="blue"
            class="white--text"
            :disabled="(member.username==''||member.password=='')"
          >로그인</v-btn>
          <v-btn @click="clear">초기화</v-btn>
        
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import jwt_decode from "jwt-decode";
import { validationMixin } from "vuelidate";
import { createInstance } from "@/api/index.js";
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
      console.log(this.member.username);
      console.log(this.member.password);
      const instance = createInstance();
      console.log(this.member);
      instance.post("/accounts/login/", JSON.stringify(this.member))
        .then(
          (response) => {
            console.log(response);
            const decoded = jwt_decode(response.data.token);
            //console.log(username);
            let token = response.data["token"];
            localStorage.setItem("token", token);
            //this.$store.commit("SET_IS_LOGIN", true);
            this.$store.commit("SET_TOKEN", token);
            this.$store.commit("SET_USER_INFO", decoded.username);
            this.$router.push("/");
          }
        )
        .catch(() => {
          alert("에러발생!");
          //this.$router.push("/");
        });
      
    },
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("이메일을 입력해주세요.");
      return errors;
    },
    
  }
};
</script>

<style lang="scss" scoped>
</style>
