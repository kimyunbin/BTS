<template>
  <v-card @click="setSelectPlace()" hover class="justify-center" >
        <v-img
          :src="item.imgurl"
          width=100%
          height="180"
          object-fit: cover
        />

        <v-card-title primary-title>
        <div>
          <p class="headline mt-0 mb-0"><b>{{item.name}}</b></p>
          <div>
            <p class="green--text mb-0 font-weight-medium"><b>{{item.state}}</b></p>
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
    ...mapGetters(["SET_SELECT_PLACE"]),
    ...mapGetters(["SET_SELECT_INFO"])
  },
  methods: {
    setSelectPlace(){
      // console.log(this.item.state + ' ' + this.item.name)
      const name = this.item.state + ' ' + this.item.name
      this.$store.dispatch("SET_SELECT_PLACE", name).then(()=>{
      this.$store.dispatch("SET_SELECT_INFO", name)
      .then(()=>{

        this.$router.push("/placedetail");
      })
      });
    }
  },
};
</script>

<style scoped>
</style>
