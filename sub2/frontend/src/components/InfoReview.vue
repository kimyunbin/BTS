<template>
<v-flex >
  <v-card hover class="justify-center" width=550px height=250px>
    <v-card-title primary-title>
      <div>
        <span style="padding-bottom:2px">{{review.userid}}</span>
        <v-btn round dark @click="deleteReview()"  style="position:absolute;right:5px;"><v-icon>delete</v-icon></v-btn>
        <star-rating v-model="rating" read-only v-bind:star-size="30"></star-rating>
        <br>
        <p class="headline mb-3"><b>{{review.title}}</b></p>
        <div>
          <p class="green--text font-weight-medium"><b>{{review.contents}}</b></p>
        </div>
        
        <h6>작성일: {{review.write_date}}</h6>
        <h6>이 리뷰는 {{review.userid}}님의 개인 의견이며 저희 서비스 의견과 무관합니다.</h6>
      </div>
    </v-card-title>
    <br>
  </v-card>
  <hr>
</v-flex>
</template>

<script>
import { mapGetters } from "vuex";
import StarRating from 'vue-star-rating'

export default {
  props: {
    review:{
      type: Object,
      required:true
    }
  },
  created() {
    this.rating=this.review.evaluate;
  },
  data() {
    return {
      rating:0,
      eval:0,
    }
  },
  components: {
    StarRating
  },
  computed:{
    
  },
  methods: {
    deleteReview(){
      //리뷰삭제로직이 들어가면 됩니다.
      alert("미구현");
    }
  },
};
</script>

<style scoped>
</style>