<template>
  <section>
    <vue-horizontal-list :items="item.img" :options="options">
      <template v-slot:nav-prev>
        <div>👈</div>
      </template>

      <template v-slot:nav-next>
        <div>👉</div>        
      </template>
      
      <template v-slot:default="{ item }">
        <img
            :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.awsimages}`" 
            class="mask"
          />
      </template>

    </vue-horizontal-list>
  </section>
</template>

<script>
import VueHorizontalList from "vue-horizontal-list";
export default {
  components: {
    VueHorizontalList,  
  },
  props: {
    item:{
      type: Object,
      required:true
    }
  },
  data() {
    return {
      options: {
        autoplay: { play: true, repeat: true, speed: 2500 },
      },
    }
  }
}
</script>

<style scoped>
.mask{
  object-fit: cover;
  height: 500px;
}
</style>