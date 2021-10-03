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

<!-- <v-flex >
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>
    <v-card-title>Cafe Badilico</v-card-title>

    <v-img
      height="250"
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>


    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ms-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 text-subtitle-1">
        $ • Italian, Cafe
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider>


    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions>
  </v-card>
</v-flex> -->
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
        this.$router.replace("/infodetail");
      });
    },
    deleteReview() {
      this.$store.dispatch("SPOT_LIKE", this.select_detail.id)
      .then(()=>{
        // this.$store.state.select_like
        // console.log(this.select_like,'ccc')
        alert("관심목록에서 취소되었습니다.");
        this.$router.replace("/myinteresting");
      })
    }
  },
}
</script>

<style>
.img-box {
  width: 100%;
  max-height: 450px;
  overflow: cover;
  display: flex;
  justify-content: center;

}
</style>
