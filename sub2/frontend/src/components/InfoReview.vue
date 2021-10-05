<template>
  <div class="comment">
    <div class="top">
      <star-rating v-model="rating" read-only v-bind:star-size="30"></star-rating>
      <div class="user">{{review.user.nickname}}</div>
    </div>
    <div class="bottom">
      <div>
        <p class="word"><b>{{review.content}}</b></p>
      </div>
      <h6>작성일: {{createtime}}</h6>
    </div>
    <hr>
  </div>
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
    // this.rating=this.review.rating
    var time = new Date(this.review.created_at)
    var year = time.getFullYear();
    var month = ('0' + (time.getMonth() + 1)).slice(-2);
    var day = ('0' + time.getDate()).slice(-2);

    var dateString = year + '-' + month  + '-' + day;
    this.createtime = dateString
  },
  data() {
    return {
      rating:this.review.rating,
      eval:0,
      createtime:''
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
      this.$alert("작성자만 삭제할 수 있습니다");
    }
  },
};
</script>

<style scoped>
.word {
  display: block;
  color: black;
  font-size: 20px;
  font-weight: bolder !important;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  line-height: 1.2;
/*        height: 4.8em;*/
  text-align: left;
  word-wrap: break-word;
  display: -webkit-box;
  -webkit-line-clamp: 2 ;
  -webkit-box-orient: vertical;
}

.comment{
  width: 90%;
}
.top{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.user{
  padding-right: 20px;
  font-size: 15px;
  font-weight: 500;
}
</style>
