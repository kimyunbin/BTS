<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      

      <v-flex xs12 sm12 md6 lg6 xl6>
        <h2 class="pb-4 mb-4">
          <span>여행지역 궁합도 사전 질문</span>
          
        </h2>

        <form>

          <vueper-slides class="in" :touchable="false" :bullets="false" :arrows="false" ref="first" style="width: 500px; height: 600px; display: inline-block;">
            <vueper-slide
              :key="1">
              <template v-slot:content>
                <div>
                  <sequential-entrance>
                    <div class="box" v-for="app in apps" :key="app">{{ app }}</div>
                  </sequential-entrance>
                  <v-text-field
                    name="question1"
                    color="blue"
                    background-color="transparent"
                    v-model="question1"
                    label="질문1"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat to="/signup" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn id="right" large flat class="blue--text" @click="$refs.first.next()">
                    다음으로&nbsp;<i class="fas fa-arrow-right"></i>
                  </v-btn>
                </div>
              </template>
            </vueper-slide>
            <vueper-slide
              :key="2">
              <template v-slot:content>
                <div>
                  <v-text-field
                    name="question2"
                    color="blue"
                    background-color="transparent"
                    v-model="question2"
                    label="질문2"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat @click="$refs.first.previous()" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn id="right" large flat class="blue--text" @click="$refs.first.next()">
                    다음으로&nbsp;<i class="fas fa-arrow-right"></i>
                  </v-btn>
                </div>
              </template>
            </vueper-slide>
            <vueper-slide
              :key="3">
              <template v-slot:content>
                <div>
                  <v-text-field
                    name="question3"
                    color="blue"
                    background-color="transparent"
                    v-model="question3"
                    label="질문3"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat @click="$refs.first.previous()" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn id="right" large flat class="blue--text" @click="$refs.first.next()">
                    다음으로&nbsp;<i class="fas fa-arrow-right"></i>
                  </v-btn>
                </div>
              </template>
            </vueper-slide>
            <vueper-slide
              :key="4">
              <template v-slot:content>
                <div>
                  <v-text-field
                    name="question4"
                    color="blue"
                    background-color="transparent"
                    v-model="question4"
                    label="질문4"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat @click="$refs.first.previous()" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn id="right" large flat class="blue--text" @click="$refs.first.next()">
                    다음으로&nbsp;<i class="fas fa-arrow-right"></i>
                  </v-btn>
                </div>
              </template>
            </vueper-slide>
            <vueper-slide
              :key="5">
              <template v-slot:content>
                <div>
                  <v-text-field
                    name="question5"
                    color="blue"
                    background-color="transparent"
                    v-model="question5"
                    label="질문5"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat @click="$refs.first.previous()" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn id="right" large flat class="blue--text" @click="$refs.first.next()">
                    다음으로&nbsp;<i class="fas fa-arrow-right"></i>
                  </v-btn>
                </div>
              </template>
            </vueper-slide>
            <vueper-slide
              :key="6">
              <template v-slot:content>
                <div>
                  <v-text-field
                    name="question6"
                    color="blue"
                    background-color="transparent"
                    v-model="question6"
                    label="질문6"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field>
                  <v-btn large flat @click="$refs.first.previous()" class="blue--text">
                    <i class="fas fa-arrow-left"></i>&nbsp;이전으로
                  </v-btn>
                  <v-btn
                    id="right2"
                    @click="submit"
                    type="submit"
                    color="blue"
                    class="white--text"
                    :disabled=" (name==''||email==''||password=='' || password !== password_confirm)"
                  >회원가입</v-btn>
                </div>
              </template>
            </vueper-slide>
          </vueper-slides>
          
        </form>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'

export default {
  components: { VueperSlides, VueperSlide },
  data() {
    return {
      question1:"",
      question2:"",
      question3:"",
    };
  },
  methods: {
    submit() {
    const instance = createInstance();
      
      instance.post("/user/signup", JSON.stringify())
        .then(
          (response) => {
            console.log(response);
            if (response.data.message === "success") {
              alert("회원가입 완료");
              this.$router.push("/");
            } else {
              alert("회원가입 실패");
            }
          }
        )
        .catch(() => {
          alert("에러발생!");
          this.$router.push("/");
        });
    },
    showAlert(msg) {
      alert(msg);
    },
  },
  computed: {
    
  },
  
  
};
</script>

<style lang="scss" scoped>
#right {
  margin-left: 38%;
}
#right2 {
  margin-left: 45%;
}
</style>
