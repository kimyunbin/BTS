<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-4">
          <span>회원가입</span>
          
        </h2>

        <form>
          <v-layout row wrap justify-center align-center>
          <v-text-field
            name="name"
            color="blue"
            background-color="transparent"
            v-model="nickname"
            label="닉네임"
            required
            @blur="$v.name.$touch()"
          ></v-text-field>
          <v-btn @click="authentic()" color="blue" class="white--text">인증하기</v-btn>
          </v-layout>
          
          <v-text-field
            type="email"
            color="blue"
            background-color="transparent"
            name="email"
            v-model="username"
            label="E-mail"
            required
            @blur="$v.email.$touch()"
          ></v-text-field>
          
          <v-text-field
            :type="'password'"
            name="password"
            color="blue"
            background-color="transparent"
            v-model="password"
            
            label="비밀번호"
          ></v-text-field>

          <v-text-field
            :type="'password'"
            name="passwordConfirm"
            color="blue"
            background-color="transparent"
            v-model="password_confirm"
            label="비밀번호확인"
          ></v-text-field>
          <div style="color:red" v-if="error.password_confirm">{{error.password_confirm}}</div>

          <v-select
            v-model="select"
            :items="gender"
            :rules="[v => !!v || '성별을 선택해 주세요']"
            label="성별"
            required
            @change="$v.select.$touch()"
            @blur="$v.select.$touch()"
          ></v-select>

          <v-text-field
            type="number"
            name="age"
            color="blue"
            background-color="transparent"
            v-model="age"
            label="나이"
          ></v-text-field>

          <v-btn
            large flat to="/signup2"
            color="blue"
            class="white--text"
            :disabled=" (name=='' || email=='' || password=='' || password !== password_confirm || gender=='' || age=='')"
          >다음으로</v-btn>
          
          <v-btn @click="clear">초기화</v-btn>
          <v-btn @click="fakeSignUp"></v-btn>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { validationMixin } from "vuelidate";
import { createInstance } from "@/api/index.js";

import {
  required,
  maxLength,
  email,
  minLength
} from "vuelidate/lib/validators";
export default {
  
  mixins: [validationMixin],
  validations: {
    name: { required, maxLength: maxLength(8) },
    email: { required, email },
    password: { required, minLength: minLength(8) },
    age: { required },
    gender: { required },
  },
  data() {
    return {
      username: "",
      nickname:"",
      password: "",
      password_confirm:"",
      error: {
        password_confirm: false,
      },
      select: "",
      gender: [
        '남성',
        '여성',
      ],
      age: "",
      budget:"200000",
      travelers:"2",
      comapanion:true,
      transportation:"11000",
      selection:11000,
      age:26,
      activity:"10101010101",
      sex:true,
    };
  },
  computed: {
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.maxLength &&
        errors.push("8글자 이내로 작성해주세요.");
      !this.$v.name.required && errors.push("이름을 입력해주세요.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.username.$dirty) return errors;
      !this.$v.email.email && errors.push("@ 이메일 형식으로 입력해주세요.");
      !this.$v.email.required && errors.push("이메일을 입력해주세요.");
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.password.$dirty) return errors;
      !this.$v.password.minLength &&
        errors.push("비밀번호가 8글자 이상이어야합니다.");
      !this.$v.body.required && errors.push("비밀번호를 확인해주세요");
      return errors;
    }
  },
  watch:{
    password_confirm: function(v){
      this.checkForm();
    }
  },
  methods:{
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.name = "";
      this.email = "";
      this.body = "";
      this.password = "";
      this.password_confirm = "";
      // this.gender = null;
      this.age = "";
    },
    checkForm() {
      if (this.password !== this.password_confirm)
        this.error.password_confirm = "비밀번호가 다릅니다.";
      else this.error.password_confirm = false;


      let isSubmit = true;
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    },
    authentic(){

    },
    fakeSignUp(){
      const member={
        username:this.username,
        nickname: this.nickname,
        password:this.password,
        budget:this.budget,  
        travelers:this.travelers, 
        companion: true,
        transportation :"11000", 
        selection:"11000"  ,
        age: "26",
        activity : "10101010101",
        sex :true
      }
      console.log(member);
      const instance = createInstance();
      instance.post("/accounts/signup/", JSON.stringify(member))
        .then(
          (response) => {
            console.log(response);
            if (response.data.status === "success") {
              alert("회원가입 완료");
              this.$router.push("/");
            } else {
              alert("회원가입 실패");
            }
          }
        )
        .catch(() => {
          alert("에러발생!");
          //this.$router.push("/");
        });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
