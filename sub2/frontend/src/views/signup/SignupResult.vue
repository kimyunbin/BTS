<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      


          <v-btn @click="check">체크</v-btn>
          <v-btn @click="submit()">회원가입</v-btn>
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapState } from 'vuex';
import { createInstance } from "@/api/index.js";

export default {
  
  data() {
    return {
    
    };
  },
  computed: {
            ...mapGetters([
                "select_budget", "select_travelers", "select_companion", "select_transportations", "select_selection", "select_activity", "select_user_signup"
            ]),
            ...mapState(["budget","travelers","companion","transportations","selection", "activity", "user_signup"]),
        },
  methods:{
    check(){ 
      console.log(this.user_signup)
      console.log(this.budget)
      console.log(this.travelers)
      console.log(this.companion)
      console.log(this.transportations)
      console.log(this.selection)
      console.log(this.activity)
      
    },
    submit(){
      const body ={
        username:this.user_signup.username,
        nickname:this.user_signup.nickname,
        password:this.user_signup.password,
        budget:this.budget,
        travelers:this.travelers,
        companion:this.companion,
        transportation:this.transportations,
        selection:this.selection,
        age:this.user_signup.age,
        activity:this.activity,
        sex:this.user_signup.sex
      };
      console.log(body);
      const instance = createInstance();
      instance.post("/accounts/signup/", JSON.stringify(body))
        .then(
          (response) => {
            console.log(response);
            if (response.data.status === "success") {
              alert("회원가입 완료");
              //this.$router.push("/");
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
