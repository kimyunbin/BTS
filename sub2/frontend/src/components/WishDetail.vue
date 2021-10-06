<template>
<div>

<v-flex >
  <v-card hover class="justify-center" width=550px height=550px @click="setSelectInfo()">
    <v-card-title primary-title>

      <div>
        <v-btn round dark @click="deleteReview()"  style="position:absolute;right:5px;"><v-icon>delete</v-icon></v-btn>

        <p class="headline mb-3">
          <b>{{wishDetail.Touristspot.title}}</b>
        </p>

        <star-rating v-model="rating" read-only v-bind:star-size="30"></star-rating>
        <span style="padding-bottom:2px">리뷰 수: {{wishDetail.Touristspot.counting}}</span>
        <br>
        <br>

        <div>
          <p class="green--text font-weight-medium"><b>{{wishDetail.Touristspot.address}}</b></p>
        </div>
        <!-- <h6>연락처: {{wishDetail.tel}}</h6> -->
      </div>

    </v-card-title>
      <div class="img-box">
        <v-img
          width=100%
          :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${wishDetail.Touristspot.img[0].awsimages}`"
        ></v-img>
        <br>
      </div>
    <br>
  </v-card>
  <hr>
  <div style="height:100px">
  </div>
</v-flex>
</div>
</template>

<script>
import StarRating from 'vue-star-rating'
import { mapGetters, mapState } from "vuex";

export default {
  name: 'WishDetail',
  components: {
    StarRating
  },
  props: {
    wishDetail:{
      type: Object,
      required:true
    }
  },
  data() {
    return {
      rating: 0,
      eval:0,
    }
  },
  computed: {
  ...mapGetters([
    "select_info",
    "select_detail",
    "select_like"
  ]),
  },
  created() {
    this.rating=this.wishDetail.Touristspot.avg_rating;
  },
  methods: {
    setSelectInfo(){
      console.log(this.wishDetail.Touristspot.id)
      this.$store.dispatch("SET_SELECT_DETAIL", this.wishDetail.Touristspot).then(()=>{
        this.$router.push("/infodetail");
      });
    },
    deleteReview() {
      // console.log(this.wishDetail.Touristspot,'ch')
      this.$store.dispatch("SPOT_LIKE", this.wishDetail.Touristspot.id)
      .then(()=>{
        // this.$store.state.select_like
        // console.log(this.select_like,'ccc')
        this.$alert("취소되었습니다.").then(() =>{
          this.$router.replace("/myinteresting");
        })
        
      })
    }
  },
}
</script>

<style scoped>
.img-box {
  width: 100%;
  max-height: 450px;
  overflow: cover;
  display: flex;
  justify-content: center;

}
</style>
