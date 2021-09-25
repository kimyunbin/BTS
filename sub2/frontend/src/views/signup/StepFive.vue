<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 여행지를 선택하는 가장 큰 이유는 무엇인가요?</b></h5>
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
    import one from "@/assets/img/이유/지명도.png";
    import two from "@/assets/img/이유/볼거리.png";
    import three from "@/assets/img/이유/가격.png";
    import four from "@/assets/img/이유/거리.png";
    import five from "@/assets/img/이유/숙박.png";

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
                    "지명도",
                    "볼거리",
                    "저렴한 가격",
                    "이동거리",
                    "숙박시설",
                ],
                selection : '',
            }
        },
        validations: {
            selection: {
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
        methods: {
            onClick() {
                $(".card").each(function ()
                    {
                        $(this).click(function () {                              
                            if($(this).hasClass("filter")) {
                                $(this).removeClass("filter");
                                if($(".card").index(this) === 0) {
                                    this.selection = 1;
                                }
                                else if($(".card").index(this) === 1) {
                                    this.selection = 2;
                                } 
                                else if($(".card").index(this) === 2) {
                                    this.selection = 3;
                                } 
                                else if($(".card").index(this) === 3) {
                                    this.selection = 4;
                                } 
                                else {
                                    this.selection = 5;
                                } 
                                console.log(this.selection);        
                            } else {
                                $(this).addClass("filter");
                                this.selection = '';
                                console.log(this.selection)        
                            }
                        });
                    });
                // this.budget = 
            }
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