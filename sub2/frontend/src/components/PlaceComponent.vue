<template>
  <div @click="setSelectPlace()" class="card" >
    <div class="card-img">
      <img
        class="skeleton"
        :src="item.imgurl"
        width=100%
        height="180"
        object-fit: cover
      />
    </div>

    <div class="text">
      <p class="headline mb-0"><b>{{item.name}}</b></p>
      <div>
        <p class="green--text mb-0 font-weight-medium"><b>{{item.state}}</b></p>
      </div>
    </div>
  </div>
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
img{
  border-radius: 10px;
  transition-duration: 0.5s;
  -webkit-transition-duration: 0.5s;
  -moz-transition-duration: 0.5s;
  -o-transition-duration: 0.5s;
}
.card{
  border: none;
  cursor: pointer;
  width: 270px;
  border-radius: 10px;
  overflow: hidden;
}
.card-img{
  border: none;
  cursor: pointer;
  width: 270px;
  border-radius: 10px;
  overflow: hidden;
}
.card:hover img{
  transform: 0.5s;
  -webkit-transform: scale(1.2);
}
.headline{
  margin-top: 3px;
}
.text{
  padding-left: 3px;
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
