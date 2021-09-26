<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행 인원 수는 얼마나 되나요?</b></h5>
        <br>
        <div class="field">
            <sequential-entrance fromRight>
                    <div name="budget" required class="box" v-for="index in 5" :key="index" @click="onClick()">
                        <img class="card filter" :src="img[index-1]" alt="">
                        <br>
                        <p align="center"><b>{{tooltip[index-1]}}</b></p>
                    </div>
            </sequential-entrance>
            <!-- <label class="label">Username</label>
            <div class="control">
                <input :class="['input', ($v.form.username.$error) ? 'is-danger' : '']" type="text" placeholder="Text input"
                       v-model="form.username">
            </div>
            <p v-if="$v.form.username.$error" class="help is-danger">This username is invalid</p> -->
        </div>
    </div>
</template>

<script>
    import {validationMixin} from 'vuelidate'
    import {required, email} from 'vuelidate/lib/validators'
    import one from "@/assets/img/인원/1.png";
    import two from "@/assets/img/인원/2.png";
    import three from "@/assets/img/인원/3.png";
    import four from "@/assets/img/인원/4.png";
    import five from "@/assets/img/인원/5.png";
    import { mapGetters } from "vuex";

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                img:[
                    one,
                    two,
                    three,
                    four,
                    five,
                ],
                tooltip:[
                    "혼자",
                    "둘이서",
                    "3명",
                    "4명",
                    "5명 이상",
                ],
                travelers : '',
            }
        },
        validations: {
            travelers: {
                required
            },
        },
        watch: {
            $v: {
                handler: function (val) {
                    if(!val.$invalid) {
                        this.$emit('can-continue', {value: true});
                    } else {
                        this.$emit('can-continue', {value: false});
                        setTimeout(()=> {
                            this.$emit('change-next', {nextBtnValue: false});
                        }, 3000)
                    }
                },
                deep: true
            },

            clickedNext(val) {
                // console.log(val);
                if(val === true) {
                    this.$v.form.$touch();
                }
            }
        },
        mounted() {
            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});
            } else {
                this.$emit('can-continue', {value: true});
            }
        },
        computed:{
            ...mapGetters(["SET_SELECT_TRAVELERS"]),
        },
        methods: {
            onClick() {
                $(".card").each(function ()
                    {
                        $(this).click(function () {                              
                            if($(this).hasClass("filter")) {
                                $(this).removeClass("filter");
                                if($(".card").index(this) === 0) {
                                    this.travelers = 1;
                                }
                                else if($(".card").index(this) === 1) {
                                    this.travelers = 2;
                                } 
                                else if($(".card").index(this) === 2) {
                                    this.travelers = 3;
                                } 
                                else if($(".card").index(this) === 3) {
                                    this.travelers = 4;
                                } 
                                else {
                                    this.travelers = 5;
                                } 
                                // console.log(this.travelers);        
                            } else {
                                $(this).addClass("filter");
                                this.travelers = '';
                                // console.log(this.travelers)        
                            }
                        });
                    });
                    this.setTravelers();
            },
            setTravelers(){
                this.$store.dispatch("SET_SELECT_TRAVELERS", this.travelers);
            },
        },
    }
</script>

<style lang="scss" scoped>
.field{
    display: flex;
    justify-content: center;
}
.box {
    display: inline-block;
    border-radius: 10px;
    width: 160px;
    height: 100px;
    margin: 1rem;
}
.card {
    width: 160px;
    height: 100px;
}
.filter {
    filter: grayscale(100%);
}
</style>