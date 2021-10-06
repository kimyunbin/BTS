<template>
<div class="my">
  <div class="img">
    <img :src="`https://go-test-buket.s3.ap-northeast-2.amazonaws.com/${item.img[idx].awsimages}`" alt="">
  </div>
  <div class="control">
    <div class="left" @click="down"></div>
    <div class="right" @click="up"></div>
  </div>
</div>
</template>

<script>
export default {
  components: {
  },
  props: {
    item:{
      type: Object,
      required:true
    }
  },
  data() {
    return {
      idx:0
    }
  },
  methods:{
    down(){
      if (this.idx===0){
        return this.idx=this.item.img.length-1
      } 
      console.log(this.idx--)
    },
    up(){
      if (this.idx === this.item.img.length-1){
        return this.idx=0
      }
      console.log(this.idx++)
    },
  }
}
</script>

<style scoped>
.my{
  position: relative;
}
.control{
  border-radius: 10px;
  overflow: hidden;
  width: 100%;
  height: 500px;
  position: absolute;
  color: #fff;
  transition-duration: 0.5s;
  -webkit-transition-duration: 0.5s;
  -moz-transition-duration: 0.5s;
  -o-transition-duration: 0.5s;
}
.left{
  height: 100%;
  width: 40%;
  margin-right: 10%;
  cursor: pointer;
}
.right{
  height: 100%;
  width: 40%;
  margin-left: 10%;
  cursor: pointer;
}
.left:hover{
  background-color: rgba(0, 0, 0, 0.3);
  content: "<";
  -webkit-transition: all 0.3s ease-in-out; 
  -moz-transition: all 0.3s ease-in-out; 
  -o-transition: all 0.3s ease-in-out; 
  transition: all 0.3s ease-in-out;

}
.right:hover{
  background-color: rgba(0, 0, 0, 0.3);
  content: ">";
  -webkit-transition: all 0.3s ease-in-out; 
  -moz-transition: all 0.3s ease-in-out; 
  -o-transition: all 0.3s ease-in-out; 
  transition: all 0.3s ease-in-out;
}
.img{
  width: 100%;
  height: 500px;
  position: absolute;
  border-radius: 10px;
  overflow: hidden;
  display: flex;
  object-fit: cover;
}
</style>