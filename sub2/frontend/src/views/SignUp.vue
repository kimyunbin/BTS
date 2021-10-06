<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-4">
          <span>회원가입</span>
          
        </h2>

        <form>
          
          <v-text-field
            name="name"
            color="blue"
            background-color="transparent"
            v-model="form.nickname"
            label="닉네임"
            required
            @blur="$v.name.$touch()"
          ></v-text-field>
          
          <v-text-field
            type="email"
            color="blue"
            background-color="transparent"
            name="email"
            v-model="form.username"
            label="E-mail"
            required
            @blur="$v.email.$touch()"
          ></v-text-field>
          <v-btn @click="authentic()" color="blue" class="buttons white--text">인증하기</v-btn>
          
          <v-text-field
            :type="'password'"
            name="password"
            color="blue"
            background-color="transparent"
            v-model="form.password"
            
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
            v-model="form.sex"
            :items="sexList"
            label="성별"
            item-text="name"
            item-value="value"
            return-object
          ></v-select>

          <v-text-field
            type="number"
            name="age"
            color="blue"
            background-color="transparent"
            v-model="form.age"
            label="나이"
          ></v-text-field>

          <v-btn
            large flat
            @click="setUserSignup()"
            color="blue"
            class="white--text"
            :disabled=" (form.username=='' || form.email=='' || form.password=='' || form.password !== password_confirm || form.gender=='' || form.age=='')"
          >다음으로</v-btn>

          
          <v-btn @click="clear" color="red"  class="white--text">초기화</v-btn>
          <!-- <v-btn @click="fakeSignUp"></v-btn> -->
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { validationMixin } from "vuelidate";
import { createInstance } from "@/api/index.js";

import { mapGetters } from "vuex";
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
      password_confirm:"",
      error: {
        password_confirm: false,
      },
      form:{
        username: "",
        nickname:"",
        password: "",
        age: "",
        sex:true,
      },
      sexList: [
        { name: "남자", value: true },
        { name: "여자", value: false },
      ],
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
  computed:{
    ...mapGetters(["SET_SELECT_USERSIGNUP"]),
  },
  methods:{
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.form.nickname = "";
      this.form.username = "";
      this.form.password = "";
      this.password_confirm = "";
      // this.gender = null;
      this.form.age = "";
    },
    checkForm() {
      if (this.form.password !== this.password_confirm)
        this.error.password_confirm = "비밀번호가 다릅니다.";
      else this.error.password_confirm = false;


      let isSubmit = true;
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    },
    authentic(){
      const body = {
        username: this.form.username,
        nickname: this.form.nickname
      };
      const instance = createInstance();
      instance.post("/accounts/check/", JSON.stringify(body))
        .then(
          (response) => {
            console.log(response);
            if (response.data.status === "success") {
              this.$alert("인증완료").then(() => {
                    
              });
            } else {
              this.$alert("인증실패").then(() => {
                    
              });
            }
          }
        )
        .catch(() => {
          this.$alert("인증실패").then(() => {
                    
              });
        })

    },
    setUserSignup(){
      this.sex = this.sexList.value;
      this.$store.dispatch("SET_SELECT_USERSIGNUP", this.form).then(()=>{
        this.$router.push("/signup2/"); 
      });
    },
    check(){ 
      console.log(this.form)
    },
  }
};
</script>

<style lang="scss" scoped>
.buttons {
  position: relative;
  left: 80%;
}
</style>
