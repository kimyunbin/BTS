<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행지 교통수단은 무엇인가요?</b></h5>
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
    import one from "@/assets/img/교통수단/항공.jpeg";
    import two from "@/assets/img/교통수단/지하철.jpeg";
    import three from "@/assets/img/교통수단/관광버스.jpeg";
    import four from "@/assets/img/교통수단/렌트카.jpeg";
    import five from "@/assets/img/교통수단/기타.jpeg";

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                img:[
                    one,
                    two,
                    four,
                    three,
                    five,
                ],
                tooltip:[
                    "항공",
                    "지하철",
                    "렌트카",
                    "관광버스",
                    "기타",
                ],
                transportations : '',
            }
        },
        validations: {
            transportations: {
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
                                    this.transportations = 1;
                                }
                                else if($(".card").index(this) === 1) {
                                    this.transportations = 2;
                                } 
                                else if($(".card").index(this) === 2) {
                                    this.transportations = 4;
                                } 
                                else if($(".card").index(this) === 3) {
                                    this.transportations = 3;
                                } 
                                else {
                                    this.transportations = 5;
                                } 
                                console.log(this.transportations);       
                            } else {
                                $(this).addClass("filter");
                                this.transportations = '';
                                console.log(this.transportations)      
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