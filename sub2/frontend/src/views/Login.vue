<template>
  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-4">
          <span>로그인</span>
        </h2>

        <form >
          <v-text-field
            type="email"
            color="blue"
            background-color="transparent"
            name="email"
            v-model="email"
            :error-messages="emailErrors"
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
          <v-btn
            @click="submit"
            type="submit"
            color="blue"
            class="white--text"
            :disabled="(email==''||password=='')"
          >로그인</v-btn>
          <v-btn @click="clear">초기화</v-btn>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { validationMixin } from "vuelidate";
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
  },
  data() {
    return {
      name: "",
      email: "",
      password: "",
    
    };
  },
  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.email = "";
      this.password ="";
    }
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
