<template>
  <div>
    <v-dialog
      v-model="dialog"
      width="1200px"
      height ="900px"
    >
      <template v-slot:activator="{ on, attrs }">
        <div 
          class="card" 
          @click="setSelectInfo(item.id)"
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
        <div class="ctr">
          <div></div>
          <div class="btn-gp">
            <div class="likeBtn" @click="changeLike(item.id)">
              <i class="fas fa-heart" v-if="select_like == true"/>
              <i class="far fa-heart" v-else />
            </div>
            <div class="shareBtn" @click="share()">
              <i class="fas fa-share-alt" />
            </div>
            <div class="closeBtn" @click="dialog = false">
              <i class="fas fa-times" ></i>
            </div>
          </div>
        </div>
        <div class="modal-title">
          <span class="text-h5">{{item.title}}</span>
        </div>
        <div class="modal-content">
          <div class="modal-img">
            <carosel :item=item />
          </div>
          <div class="modal-rv">
            <InfoReview
              v-for="(review,key) in rvs"
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
        <div class="modal-footer">
          <div class="adr">{{item.address}}</div>
          <div class="loc">📌 X: {{item.latitude}} ,Y: {{item.longitude}}</div>
        </div>
      </div>
    </v-dialog>
  </div>
</template>


<script>
import { mapGetters, mapState } from "vuex";
import StarRating from 'vue-star-rating'
import InfoReview from "@/components/InfoReview";
import carosel from "@/components/my-Carosel";
export default {
  components: {
    StarRating,
    InfoReview,
    carosel,
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
      },
      rvs:[],
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
    setSelectInfo(k){
      this.$store.dispatch("GET_REVIEW", k).then(()=>{
        this.rvs = this.$store.state.reviews
      })
      this.dialog = true
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
    changeLike(k){
      // this.isLike = !this.isLike;
      this.$store.dispatch("SPOT_LIKE", k)
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
  background-color: #f1f2f6;
  overflow:hidden;
  border-radius: 10px;
  border: 5px solid #a5b1c2 ;
}
.ctr{
  display: flex;
  height: 33px;
  padding-top: 3px;
  padding-bottom: 5px;
  background-color: #a5b1c2;
  justify-content: space-between;
}
.modal-title{
  font-size: 50px;
  display: flex;
  justify-content: center;
  font-family: 'IBM Plex Sans KR', sans-serif;
  font-weight:500;
  color: #1e272e;
  letter-spacing: 8px;
}

.modal-footer{
  display: flex;
  justify-content: space-between;
  border: none;
  margin: 0%;
  padding: 0%;
}
.adr{
  margin-top: 20px;
  margin-bottom: 10px;
  padding-left: 40px;
  font-size: 20px;
  color: #4caf50;
  height: 50px;
  display: flex;
  align-items: flex-start;
}
.loc{
  margin: 10px;
  padding-right: 30px;
  color: #4caf50;
}
.btn-gp{
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-right: 40px;
}
.btn-gp div{
  margin: 0%;
  padding: 0%;
  height: 25px;
  border: 2px solid #fff;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.likeBtn {
  width: 30px;
  height: 30px;
  margin: 0.4em 0 0 0;
  background-size: cover;
  cursor: pointer;
  -webkit-transition: all 0.3s ease-in-out; 
  -moz-transition: all 0.3s ease-in-out; 
  -o-transition: all 0.3s ease-in-out; 
  transition: all 0.3s ease-in-out;
  color: red;
}
.likeBtn:hover {
  background-color: #fff;
  color: red;
  }
.shareBtn {
  width: 28px;
  height: 29px;
  margin: 0.4em 0 0 0;
  z-index: 10;
  background-size: cover;
  cursor: pointer;
  -webkit-transition: all 0.3s ease-in-out; 
  -moz-transition: all 0.3s ease-in-out; 
  -o-transition: all 0.3s ease-in-out; 
  transition: all 0.3s ease-in-out;
  color: #fff;
}
.shareBtn:hover {
  background-color: #4caf50;
  }
.closeBtn {
  width: 28px;
  height: 29px;
  margin: 0.4em 0 0 0;
  z-index: 10;
  background-size: cover;
  cursor: pointer;
  -webkit-transition: all 0.3s ease-in-out; 
  -moz-transition: all 0.3s ease-in-out; 
  -o-transition: all 0.3s ease-in-out; 
  transition: all 0.3s ease-in-out;
  color: red;
}
.closeBtn:hover {
  background-color: red;
  color: #fff;
  }

.modal-img{
  width: 50%;
  margin: 3%;
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
  background-color: #f1f2f6;
}
.rv-c{
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  width: 90%;
}

</style>
