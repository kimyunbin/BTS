<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행 동반자는 누구인가요?</b></h5>
        <br>
        <div class="field">
            <sequential-entrance fromRight>
                    <div name="budget" required class="box" v-for="index in 3" :key="index" @click="onClick()">
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
    import one from "@/assets/img/동반자/혼자.jpg";
    import two from "@/assets/img/동반자/연인.jpg";
    import three from "@/assets/img/동반자/가족.jpg";

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
                img:[
                    one,
                    two,
                    three,
                ],
                tooltip:[
                    "혼자서",
                    "연인이랑",
                    "가족이랑",
                ],
                companion : '',
            }
        },
        validations: {
            companion: {
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
                                    this.companion = true;
                                }
                                else if($(".card").index(this) === 1) {
                                    this.companion = false;
                                } 
                                else {
                                    this.companion = null;
                                } 
                                console.log(this.companion);        
                            } else {
                                $(this).addClass("filter");
                                this.companion = '';
                                console.log(this.companion)
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
    margin: 1rem 3rem;
}
.card {
    width: 160px;
    height: 100px;
}
.filter {
    filter: grayscale(100%);
}
</style>