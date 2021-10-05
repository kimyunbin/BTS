<template>
  <div>
    <v-dialog
      v-model="dialog"
      width="1200px"
      height ="800px"
    >
      <template v-slot:activator="{ on, attrs }">
        <div 
          class="card" 
          @click="setSelectInfo()"
          color="primary"
          dark
          v-bind="attrs"
          v-on="on">
          <div v-if ="item.img.length">
            <v-img
              class="skeleton"
              :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.img[0].awsimages}`"
              width=100%
              height="180"
              object-fit: cover
            />
          </div>
          <div v-else>
            <v-img
              src="https://go-test-buket.s3.ap-northeast-2.amazonaws.com/noimage.png"
              width=100%
              height="180"
              object-fit: cover
            />
          </div>
          <v-card-title primary-title>
            <div>
              <p class="headline mt-0 mb-0"><b>{{item.title|longTitle}}</b></p>
              <div>
                <star-rating v-model="item.avg_rating" read-only v-bind:star-size="20"></star-rating>
                <p class="green--text font-weight-medium mt-1 mb-0"><b>{{item.address.split(" ",2).join(" ")}}</b></p>
              </div>
            </div>
          </v-card-title>
        </div>
      </template>
      <div class="my-modal">
        <div class="modal-title">
          <div></div>
          <span class="text-h5">{{select_detail.title}}</span>
          <div class="btn-gp">
            <div @click="changeLike">
              <i
                class="fas fa-heart fa-sm"
                v-if="select_like == true"
                style="color:red;font-size: 0.5em;"
              />
              <i class="far fa-heart fa-sm" v-else style="color:red;font-size: 0.5em;"/>
            </div>
            <div @click="share()">
              <i
                class="fas fa-share-alt fa-sm"
                style="color:green;font-size: 0.5em;"
              />
            </div>
          </div>
        </div>
        <div class="modal-content">
          <div class="modal-img">
            <v-carousel hide-delimiters>
              <v-carousel-item
                v-for="(item,i) in select_detail.img"
                :key="i"
                :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.awsimages}`"
                object-fit:cover
              >
              </v-carousel-item>
            </v-carousel>
          </div>
          <div class="modal-rv">
            <InfoReview
              v-for="(review,key) in reviews"
              :key = key
              :review = review
            />
            <div class="rv-c">
              <h4 data-aos="fade-up"><b>당신의 리뷰를 남겨주세요.</b></h4>
              <form>
                <v-textarea
                  color="blue"
                  background-color="transparent"
                  :counter="200"
                  v-model="review.contents"
                  label="이 곳에 대하여 어떻게 생각하시나요?"
                  name="body"
                ></v-textarea>
                <star-rating v-model="review.evaluate" v-bind:star-size="40"></star-rating>
              </form>
              <v-btn @click="submit()" type="submit" color="primary" class="white--text">등록하기</v-btn>
            </div>
          </div>
        </div>
      </div>
    </v-dialog>
  </div>
</template>


<script>
import { mapGetters, mapState } from "vuex";
import StarRating from 'vue-star-rating'
import InfoReview from "@/components/InfoReview";
import heart from "@/assets/heart.png"
import heart_b from "@/assets/heart_b.png"
export default {
  components: {
    StarRating,
    InfoReview,
    heart,
    heart_b
  },
  data:()=>{
    return {
      defaultimg:"https://i.ibb.co/q7dBcZ1/image.jpg",
      dialog:false,
      review :{
        userid:"",
        title :"",
        contents :"",
        write_date:"",
        evaluate: 0,
      }
    }
  },
  props: {
    item:{
      type: Object,
      required:true
    }
  },
  computed:{
    ...mapGetters([
      "SET_SELECT_INFO",
      "select_info",
      "select_like"
    ]),
    ...mapState([
      "user_info",
      "reviews",
      "select_like",
      "select_detail",
    ]),
  },
  methods: {
    setSelectInfo(){
      this.$store.dispatch("SET_SELECT_DETAIL", this.item).then(()=>{
        this.$store.dispatch("GET_REVIEW", this.select_detail.id)
        this.dialog = true
      })
    },
    submit(){
        if (this.review.contents == "") {
          alert('리뷰 내용을 작성해주세요')
        } else if (this.review.evaluate == 0) {
          alert('별점을 입력해주세요')
        } else {
          const data = {
            'Spok_pk' : this.select_detail.id,
            'data' : {
              'content': this.review.contents,
              'rating' : this.review.evaluate
            }
          }

          this.$store.dispatch("WRITE_REVIEW", data)
          .then(()=>{
            var today = new Date();
            this.reviews.unshift({
              user:{
                nickname:this.user_info,
              },
              rating :this.review.evaluate,
              content:this.review.contents,
              created_at:today,
            })
          }).then(()=>{
            this.review = {
              userid:"",
              title :"",
              contents :"",
              write_date:"",
              evaluate: 0,
            }
          })
        }
    },
    changeLike(){
      // this.isLike = !this.isLike;
      console.log(this.select_detail.id)
      this.$store.dispatch("SPOT_LIKE", this.select_detail.id)
      .then(()=>{
        this.$store.state.select_like
        console.log(this.select_like,'ccc')
      })
    },

    share(){
      var url = '';
      var textarea = document.createElement("textarea");
      document.body.appendChild(textarea);
      url = window.document.location.href;
      textarea.value = url;
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      alert("URL이 복사되었습니다.")
    },
  },
  filters:{
    longTitle: function(title){
      if (title.length > 8){
        return `${title.substring(0,7)}...`
      } else {
        return title
      }
    }

  }
};
</script>

<style scoped>
::-webkit-scrollbar { display: none; }

img{
  object-fit: cover;
}

.card{
  border-radius: 10px;
  overflow: hidden;
  z-index: 1;
  cursor: pointer;
}
.card:hover img{
  transform: 0.5s;
  -webkit-transform: scale(1.2);
}
.star{
  color: red;
}
.skeleton {
  animation: shine 1s linear infinite alternate;
}

@keyframes shine {
  0%{
    background-color: hsl(200, 20%, 70%);
  }
  100%{
    background-color: hsl(200, 20%, 95%);
  }
}

.my-modal{
  background-color: #fff;
  overflow:hidden;
}

.modal-title{
  font-size: 50px;
  display: flex;
  justify-content: space-around;
}

.btn-gp{
  display: flex;
  flex-direction: row;
  gap: 10px;
}

  .likeBtn {
    right: 0;
    width: 30px;
    height: 30px;
    margin: 0.2em 0 0 0;
    z-index: 10;
    background-size: cover;
  }
  .likeBtn:hover {
    cursor: pointer;
    transform: scale(1.1);
  }
  .shareBtn {
    right: 0;
    width: 28px;
    height: 29px;
    margin: 0.4em 0 0 0;
    z-index: 10;
    background-size: cover;
  }
  .shareBtn:hover {
    cursor: pointer;
    transform: scale(1.1);
  }

.modal-img{
  width: 50%;
  margin: 3%;
}
.modal-img i{
  object-fit: cover;
  width: 500px;
  height: 500px;

}

.modal-rv{
  width: 50%;
  height: 500px;
  margin-top: 3%;
  overflow: scroll;
}

.modal-content{
  display: flex;
  flex-direction: row;
  border: none;
}
.rv-c{
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  width: 90%;
}

</style>
