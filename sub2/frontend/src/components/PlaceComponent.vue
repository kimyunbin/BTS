<template>
  <v-card @click="setSelectPlace()" hover class="justify-center" >
        <v-img
          :src="item.imgurl"
          width=100%
          height="200"
          object-fit: cover
        />

        <v-card-title primary-title>
        <div>
          <p class="headline mb-0"><b>{{item.name}}</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{item.state}}</b></p>
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
      this.$store.dispatch("SET_SELECT_PLACE", this.item.name).then(()=>{
      this.$store.dispatch("SET_SELECT_INFO", this.item.name)
      .then(()=>{

        this.$router.replace("/placedetail");
      })
      });
    }
  },
};
</script>

<style scoped>
</style>
