<template>
  <v-card @click="setSelectInfo()" hover class="justify-center" >

        <div v-if ="item.img.length">
          <v-img
            :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.img[0].awsimages}`"
            width=100%
            height="180"
            object-fit: cover
          />
        </div>

        <div v-else>
          <v-img
            src="https://i.ibb.co/q7dBcZ1/image.jpg"
            width=100%
            height="180"
            object-fit: cover
          />
        </div>
        <v-card-title primary-title>
        <div>
          <p class="headline mt-0 mb-0"><b>{{item.title|longTitle}}</b></p>
          <div>
            <p class="green--text font-weight-medium mb-0"><b>{{item.address.split(" ",2).join(" ")}}</b></p>
          </div>
        </div>
      </v-card-title>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
export default {
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
      console.log(this.item)
      this.$store.dispatch("SET_SELECT_DETAIL", this.item).then(()=>{
        this.$router.replace("/infodetail");
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
</style>
