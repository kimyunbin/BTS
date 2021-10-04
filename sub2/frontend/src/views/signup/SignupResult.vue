<template>

  <v-container grid-list-xl>
    <v-layout row justify-center align-center wrap class="mt-4 pt-2">
      <v-container>
        <div class="boarding-pass">
          <header>
            <div class="flight">
              <small>flight</small>
              <strong>{{user_signup.nickname}}님 회원권</strong>
            </div>
          </header>
          <section class="cities">
            <div class="city">
              <small>Korea</small>
              <strong>you</strong>
            </div>
            <div class="city">
              <small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssafy</small>

              <strong>&nbsp;&nbsp;&nbsp;BTS</strong>
            </div>
            <svg class="airplane">
              <use xlink:href="#airplane"></use>
            </svg>
          </section>
          <section class="infos">
            <div class="places">
              <div class="box">
                <small>성별</small>
                <strong>{{this.sex}}</strong>
              </div>
              <div class="box">
                <small>나이</small>
                <strong>{{user_signup.age}}</strong>
              </div>
              <div class="box">
                <small>경비</small>
                <strong>{{budget}}</strong>
              </div>
              <div class="box">
                <small>인원</small>
                <strong>{{travelers}}</strong>
              </div>
            </div>
            <div class="times">
              <div class="box">
                <small>동반자</small>
                <strong>{{this.three}}</strong>
              </div>
              <div class="box">
                <small>교통편</small>
                <strong>{{this.four}}</strong>
              </div>
              <div class="box">
                <small>선택이유</small>
                <strong>{{this.five}}</strong>
              </div>
              <div class="box">
                <small>활동</small>
                <strong>{{this.six}}</strong>
              </div>
            </div>
          </section>
          <section class="strap">
            <div class="box">
              <div class="passenger">
                <small>passenger</small>
                <v-btn @click="submit()" color="blue" class="buttons white--text">회원가입</v-btn>
              </div>
            </div>
          </section>
        </div>

        <svg xmlns="http://www.w3.org/2000/svg" width="0" height="0" display="none">
          <symbol  id="airplane" viewBox="243.5 245.183 25 21.633">
            <g>
              <path fill="#336699" d="M251.966,266.816h1.242l6.11-8.784l5.711,0.2c2.995-0.102,3.472-2.027,3.472-2.308
                                      c0-0.281-0.63-2.184-3.472-2.157l-5.711,0.2l-6.11-8.785h-1.242l1.67,8.983l-6.535,0.229l-2.281-3.28h-0.561v3.566
                                      c-0.437,0.257-0.738,0.724-0.757,1.266c-0.02,0.583,0.288,1.101,0.757,1.376v3.563h0.561l2.281-3.279l6.535,0.229L251.966,266.816z
                                      "/>
            </g>
          </symbol>
        </svg>
        <!-- <v-btn @click="submit()" color="blue" class="white--text">회원가입</v-btn> -->
      </v-container>
        <!-- <v-btn @click="check">체크</v-btn> -->
        
    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { mapState } from 'vuex';
import { createInstance } from "@/api/index.js";

export default {
  
  data() {
    return {
      sex: "",
      one: "",
      two: "",
      three: "",
      four: "",
      five: "",
      six: "",
    };
  },
  computed: {
            ...mapGetters([
                "select_budget", "select_travelers", "select_companion", "select_transportations", "select_selection", "select_activity", "select_user_signup"
            ]),
            ...mapState(["budget","travelers","companion","transportations","selection", "activity", "user_signup"]),
        },
  created() {
    if(this.user_signup.sex === true) {
      this.sex = "남자"
    } else {
      this.sex = "여자"
    };

    if(this.companion === true) {
      this.three = "혼자서"
    } else if(this.companion === false) {
      this.three = "친구/연인"
    } else {
      this.three = "가족"
    };

    if(this.activity === "10000000000") {
      this.six = "자연풍경"
    } 
     else if(this.activity === "01000000000") {
      this.six = "음식"
    }
     else if(this.activity === "00010000000") {
      this.six = "역사유적지"
    }
     else if(this.activity === "00100000000") {
      this.six = "레포츠"
    }
     else if(this.activity === "00001000000") {
      this.six = "테마파크"
    }
     else if(this.activity === "00000100000") {
      this.six = "휴식"
    }
     else if(this.activity === "00000010000") {
      this.six = "온천"
    }
     else if(this.activity === "00000001000") {
      this.six = "쇼핑"
    }
     else if(this.activity === "00000000100") {
      this.six = "문화예술"
    }
     else if(this.activity === "00000000010") {
      this.six = "지역축제"
    }
     else {
      this.six = "시티투어"
    };

    if(this.transportations === "10000") {
      this.four = "항공"
    }
    else if (this.transportations === "01000") {
      this.four = "지하철"
    }
    else if (this.transportations === "00010") {
      this.four = "렌트카"
    }
    else if (this.transportations === "00100") {
      this.four = "관광버스"
    }
    else {
      this.four = "기타"
    };

    if(this.selection === "10000") {
      this.five = "지명도"
    }
    else if(this.selection === "01000") {
      this.five = "볼거리"
    }
    else if(this.selection === "00010") {
      this.five = "이동거리"
    }
    else if(this.selection === "00100") {
      this.five = "가격"
    }
    else {
      this.five = "숙발시설"
    };
    console.log(this.five)
    
  },
  methods:{
    check(){ 
      console.log(this.user_signup)
      console.log(this.budget)
      console.log(this.travelers)
      console.log(this.companion)
      console.log(this.transportations)
      console.log(this.selection)
      console.log(this.activity)
      
    },
    submit(){
      const body ={
        username:this.user_signup.username,
        nickname:this.user_signup.nickname,
        password:this.user_signup.password,
        budget:this.budget,
        travelers:this.travelers,
        companion:this.companion,
        transportation:this.transportations,
        selection:this.selection,
        age:this.user_signup.age,
        activity:this.activity,
        sex:this.user_signup.sex
      };
      console.log(body);
      const instance = createInstance();
      instance.post("/accounts/signup/", JSON.stringify(body))
        .then(
          (response) => {
            console.log(response);
            if (response.data.status === "success") {
              alert("회원가입 완료");
              //this.$router.push("/");
            } else {
              alert("회원가입 실패");
            }
          }
        )
        .catch(() => {
          alert("에러발생!");
          //this.$router.push("/");
        });
    }
  }
};
</script>

<style lang="scss" scoped>

  *,
  *::before,
  *::after {
    box-sizing: border-box;
  }

  @mixin center {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }


  /*--------------------
  Boarding Pass
  --------------------*/
  .boarding-pass {
    @include center;
    width: 500px;
    height: 400px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 5px 30px rgba(0, 0, 0, .2);
    overflow: hidden;
    text-transform: uppercase;
    margin-top: 200px;

    small {
      display: block;
      font-size: 11px;
      color: #A2A9B3;
      margin-bottom: 2px;
    }

    strong {
      font-size: 15px;
      display: block;
    }

    /*--------------------
    Header
    --------------------*/
    & header {
      background: linear-gradient(to bottom, #36475f, #2c394f);
      padding: 12px 20px;
      height: 60px;

      .flight {
        float: right;
        color: #fff;
        text-align: right;

        small {
          font-size: 8px;
          margin-bottom: 2px;
          opacity: 0.8;
        }

        strong {
          font-size: 18px;
        }

      }
    }

    /*--------------------
    Cities
    --------------------*/
    .cities {
      position: relative;

      &::after {
        content: '';
        display: table;
        clear: both;
      }

      .city {
        padding: 20px 18px;
        float: left;

        &:nth-child(2) {
          float: right;
        }

        strong {
          font-size: 40px;
          font-weight: 300;
          line-height: 1;
        }

        small {
          margin-bottom: 0px;
          margin-left: 3px;
        }
      }

      .airplane {
        position: absolute;
        width: 30px;
        height: 25px;
        top: 57%;
        left: 30%;
        opacity: 0;
        transform: translate(-50%, -50%);
        animation: move 3s infinite;
      }

      @keyframes move {
        40% {
          left: 50%;
          opacity: 1;
        }
        100% {
          left: 70%;
          opacity: 0;
        }
      }
    }

    
    /*--------------------
    Infos
    --------------------*/
    .infos {
      display: flex;
      border-top: 1px solid #99D298;

      .places,
      .times {
        width: 50%;
        padding: 10px 0;

        &::after {
          content: '';
          display: table;
          clear: both;
        }
      }
      
      .times {
        
        small {
          color: #97A1AD;
        }

        strong {
          color: #239422;
        }
      }

      .places {
        background: #ECECEC;
        border-right: 1px solid #99D298;
        
        small {
          color: #97A1AD;
        }

        strong {
          color: #239422;
        }
      }

      .box {
        padding: 10px 20px 10px;
        width: 47%;
        float: left;
        // text-overflow: ellipsis;
        // display: inline-block;

        small {
          font-size: 10px;
        }
      }
    }

    
    /*--------------------
    Strap
    --------------------*/
    .strap {
      clear: both;
      position: relative;
      border-top: 1px solid #99D298;

      &::after {
        content: '';
        display: table;
        clear: both;
      }

      .box {
        padding: 23px 0 20px 20px;

        & div {
          margin-bottom: 15px;
          
          small {
            font-size: 10px;
          }

          strong {
            font-size: 13px;
          }
        }

        sup {
          font-size: 8px;
          position: relative;
          top: -5px;
        }
      }
    }
  }
  .buttons {
    position: relative;
    left: 70%;
  }

</style>
