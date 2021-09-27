<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      


          <v-btn @click="check">체크</v-btn>
          
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapState } from 'vuex';

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
      console.log(this.budget)
      console.log(this.travelers)
      console.log(this.companion)
      console.log(this.transportations)
      console.log(this.selection)
      console.log(this.activity)
      console.log(this.user_signup)
    },
  }
};
</script>

<style lang="scss" scoped>
</style>
