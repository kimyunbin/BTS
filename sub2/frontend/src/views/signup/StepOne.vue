<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행 경비는 얼마나 되나요?</b></h5>
        <br>
        <div class="field">
            <sequential-entrance fromRight>
                    <div name="budget" required class="box" v-for="index in 5" :key="index" @click="onClick(index)">
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
    import one from "@/assets/img/경비/동전.png";
    import two from "@/assets/img/경비/천.png";
    import three from "@/assets/img/경비/오천.png";
    import four from "@/assets/img/경비/만.png";
    import five from "@/assets/img/경비/오만.png";
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
                    "5만원 이하",
                    "5~10만원",
                    "10~20만원",
                    "20~50만원",
                    "50만원 이상",
                ],
                budget : '',
            }
        },
        validations: {
            budget: {
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
                if(val === true) {
                    this.$v.$touch();
                }
            }
        },
        mounted() {
            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});
            } else {
                this.$emit('can-continue', {value: true});
            };
            $(document).ready(function() {
                $(".card").each(function () {
                    $(this).on('click', function () {
                        if($(this).hasClass('filter')) {
                            $(this).removeClass('filter');
                        } else {
                            $(this).addClass('filter')
                        }
                    })
                })
            });
        },
        computed:{
            ...mapGetters(["SET_SELECT_BUDGET"]),
        },
        methods: {
            onClick(index) {
                // console.log("index " , index);
                if(index === 1) {
                    this.budget = 5;
                }
                if(index === 2) {
                    this.budget = 10;
                }
                if(index === 3) {
                    this.budget = 20;
                }
                if(index === 4) {
                    this.budget = 50;
                }
                if(index === 5) {
                    this.budget = 100;
                }
                this.setBudget(this.budget)
                console.log(this.budget)
            },
            filter() {
                $(".card").each(function () {
                    $(this).on('click', function () {
                        if($(this).hasClass('filter')) {
                            $(this).removeClass('filter');
                        } else {
                            $(this).addClass('filter')
                        }
                    })
                })
            },
            setBudget(budget){
                this.$store.dispatch("SET_SELECT_BUDGET", budget);
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
    cursor: pointer;
    display: inline-block;
    border-radius: 10px;
    width: 160px;
    height: 100px;
    margin: 1rem;
}
.card {
    border-style: none;
    width: 160px;
    height: 100px;
}
.filter {
    filter: grayscale(100%);
}
</style>