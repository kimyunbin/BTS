<template>
  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      <v-flex>
        <h2 class="pb-4 mb-4">
          <span>여행지역 궁합도 사전 질문</span>
        </h2>
        <form>
          <vueper-slides>
            <vueper-slide v-for="i in 5" :key="i" :title="i.toString()" />
          </vueper-slides>
          <vueper-slides class="in" :touchable="false" :bullets="false" :arrows="false" ref="first" style="width: 100%; height: 100%; display: inline-block;">
            <vueper-slide
              :key="1">
              <template v-slot:content>
                <div>
                  <br>
                  <h3>당신의 여행지갑 두께는?(1/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question1" required class="box" v-for="index in 5" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question1"
                    color="blue"
                    background-color="transparent"
                    v-model="question1"
                    label="질문1"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
                  <br>
                  <h3>당신이 생각하는 최상의 여행멤버 수는?(2/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question2" required class="box" v-for="index in 5" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question2"
                    color="blue"
                    background-color="transparent"
                    v-model="question2"
                    label="질문2"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
                  <br>
                  <h3>당신이 선호하는 여행 동반자는?(3/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question3" required class="box" v-for="index in 3" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question3"
                    color="blue"
                    background-color="transparent"
                    v-model="question3"
                    label="질문3"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
                  <br>
                  <h3>당신이 선호하는 여행지 교통편은?(4/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question4" required class="box" v-for="index in 5" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question4"
                    color="blue"
                    background-color="transparent"
                    v-model="question4"
                    label="질문4"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
                  <br>
                  <h3>당신이 여행지를 선택하는 이유는?(5/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question4" required class="box" v-for="index in 5" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question5"
                    color="blue"
                    background-color="transparent"
                    v-model="question5"
                    label="질문5"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
                  <br>
                  <h3>당신이 여행지에서 즐기는 활동은?(6/6)</h3>
                  <sequential-entrance fromRight>
                    <div name="question4" required class="box" v-for="index in 11" :key="index"></div>
                  </sequential-entrance>
                  <!-- <v-text-field
                    name="question6"
                    color="blue"
                    background-color="transparent"
                    v-model="question6"
                    label="질문6"
                    required
                    @blur="$v.name.$touch()"
                  ></v-text-field> -->
                  <br>
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
      question4:"",
      question5:"",
      question6:"",
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
              this.$alert("회원가입 완료").then(() => {
                this.$router.push("/login");
              })
            } else {
              this.$alert("인증실패").then(() => {
                    
              });
            }
          }
        )
        .catch(() => {
          this.$alert("인증실패").then(() => {
            this.$router.push("/");
          });
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
.box {
  display: inline-block;
  border-radius: 10px;
  background-color: coral;
  width: 100px;
  height: 100px;
  margin: 1rem;
}
</style>
