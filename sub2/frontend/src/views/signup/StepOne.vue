<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행 경비는 얼마나 되나요?</b></h5>
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
    import one from "@/assets/img/경비/동전.png";
    import two from "@/assets/img/경비/천.png";
    import three from "@/assets/img/경비/오천.png";
    import four from "@/assets/img/경비/만.png";
    import five from "@/assets/img/경비/오만.png";

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
                console.log(val);
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
            }
        },
        methods: {
            onClick() {
                $(".card").each(function ()
                    {
                        $(this).click(function () {                              
                            if($(this).hasClass("filter") === true) {
                                $(this).removeClass("filter");
                                if($(".card").index(this) === 0) {
                                    this.budget = 5;
                                }
                                else if($(".card").index(this) === 1) {
                                    this.budget = 10;
                                } 
                                else if($(".card").index(this) === 2) {
                                    this.budget = 20;
                                } 
                                else if($(".card").index(this) === 3) {
                                    this.budget = 50;
                                } 
                                else {
                                    this.budget = 100;
                                } 
                                // console.log(this.budget);
                            } else {
                                $(this).addClass("filter");        
                                this.budget = '';
                                // console.log(this.budget)
                            }
                        });
                    });
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