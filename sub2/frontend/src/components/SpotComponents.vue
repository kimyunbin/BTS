<template>
  <v-card @click="setSelectInfo()" hover class="justify-center" >

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
  </v-card>
</template>


<script>
import StarRating from 'vue-star-rating'
import { mapGetters } from "vuex";
export default {
  components: {
    StarRating
  },
  data:()=>{
    return {
      default:"https://i.ibb.co/q7dBcZ1/image.jpg"
    }
  },
  props: {
    item:{
      type: Object,
      required:true
    }
  },
  computed:{
    ...mapGetters(["SET_SELECT_INFO"]),
  },
  methods: {
    setSelectInfo(){
      this.$store.dispatch("SET_SELECT_DETAIL", this.item).then(()=>{
        this.$router.push("/infodetail");
      });
    }
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
v-card{
  border-radius: 10px;
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
</style>
