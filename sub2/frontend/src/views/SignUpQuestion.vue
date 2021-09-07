<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-4">
          <span>추가질문</span>
          
        </h2>

        <form>
          <v-text-field
            name="question1"
            color="blue"
            background-color="transparent"
            v-model="question1"
            label="질문1"
            required
            @blur="$v.name.$touch()"
          ></v-text-field>

          <v-text-field
            name="question2"
            color="blue"
            background-color="transparent"
            v-model="question2"
            label="질문2"
            required
            @blur="$v.name.$touch()"
          ></v-text-field>
          
          <v-text-field
            name="question1"
            color="blue"
            background-color="transparent"
            v-model="question3"
            label="질문3"
            required
            @blur="$v.name.$touch()"
          ></v-text-field>
          
          <v-btn
            @click="submit"
            type="submit"
            color="blue"
            class="white--text"
            :disabled=" (name==''||email==''||password=='' || password !== password_confirm)"
          >회원가입</v-btn>
          <v-btn large flat to="/signup" class="blue--text">
            <v-icon>arrow_back</v-icon>뒤로가기
          </v-btn>
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  data() {
    return {
      question1:"",
      question2:"",
      question3:"",
    };
  },
  methods: {
    submit() {
    const instance = createInstance();
      
      instance.post("/user/signup", JSON.stringify())
        .then(
          (response) => {
            console.log(response);
            if (response.data.message === "success") {
              alert("회원가입 완료");
              this.$router.push("/");
            } else {
              alert("회원가입 실패");
            }
          }
        )
        .catch(() => {
          alert("에러발생!");
          this.$router.push("/");
        });
    },
  },
  computed: {
    
  },
  
  
};
</script>

<style lang="scss" scoped>
</style>
