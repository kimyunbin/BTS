<template>
  <v-card @click="setSelectInfo()" hover class="justify-center" >
        <v-img
          :src="item.src"
          width=100%
          height="200"
          object-fit: cover
        />

        <v-card-title primary-title>
        <div>
          <p class="headline mb-0"><b>{{item.title}}</b></p>
          <div>
            <p class="green--text font-weight-medium"><b>{{item.content}}</b></p>
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
      this.$store.dispatch("SET_SELECT_INFO", this.item).then(()=>{
        this.$router.push("/infodetail");
      });
    }
  },
};
</script>

<style scoped>
</style>
