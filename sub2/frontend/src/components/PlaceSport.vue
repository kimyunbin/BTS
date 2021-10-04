<template>
  <v-card @click="setSelectInfo()" hover class="justify-center" >
        <div v-if ="item.img.length">
          <v-img
            :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.img[0].awsimages}`"
            width=100%
            height="200"
            object-fit: cover
          />
        </div>

        <div v-else>
          <v-img
            src="https://go-test-buket.s3.ap-northeast-2.amazonaws.com/noimage.png"
            width=100%
            height="200"
            object-fit: cover
          />
        </div>
        <v-card-title primary-title>
        <div>
          <p class="headline mb-0"><b>{{item.title}}</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{item.address}}</b></p>
          </div>
        </div>
      </v-card-title>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
export default {
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
};
</script>

<style scoped>
</style>
