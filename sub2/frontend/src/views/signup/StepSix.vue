<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행활동은 무엇인가요?</b></h5>
        <br>
        <div class="field">
            <sequential-entrance class="field" fromRight>
                    <div name="budget" required class="box" v-for="index in 11" :key="index" @click="onClick(index)">
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
    import one from "@/assets/img/활동/자연.png";
    import two from "@/assets/img/활동/음식.png";
    import three from "@/assets/img/활동/스포츠.png";
    import four from "@/assets/img/활동/역사.png";
    import five from "@/assets/img/활동/테마파크.png";
    import six from "@/assets/img/활동/휴식.png";
    import seven from "@/assets/img/활동/온천.png";
    import eight from "@/assets/img/활동/쇼핑.png";
    import nine from "@/assets/img/활동/문화.png";
    import ten from "@/assets/img/활동/지역축제.png";
    import eleven from "@/assets/img/활동/시티.png";
    import { mapGetters } from "vuex";

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
                    six,
                    seven,
                    eight,
                    nine,
                    ten,
                    eleven,
                ],
                tooltip:[
                    "자연풍경",
                    "음식",
                    "역사유적지",
                    "레포츠",
                    "테마파크",
                    "휴식",
                    "온천",
                    "쇼핑",
                    "문화예술",
                    "지역축제",
                    "시티투어",
                ],
                activity : '',
            }
        },
        validations: {
            activity: {
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
            ...mapGetters(["SET_SELECT_ACTIVITY"]),
        },
        methods: {
            onClick(index) {
                // console.log("index " , index);
                if(index === 1) {
                    this.activity = "10000000000";
                }
                if(index === 2) {
                    this.activity = "01000000000";
                }
                if(index === 3) {
                    this.activity = "00010000000";
                }
                if(index === 4) {
                    this.activity = "00100000000";
                }
                if(index === 5) {
                    this.activity = "00001000000";
                }
                if(index === 6) {
                    this.activity = "00000100000";
                }
                if(index === 7) {
                    this.activity = "00000010000";
                }
                if(index === 8) {
                    this.activity = "00000001000";
                }
                if(index === 9) {
                    this.activity = "00000000100";
                }
                if(index === 10) {
                    this.activity = "00000000010";
                }
                if(index === 11) {
                    this.activity = "00000000001";
                }
                this.setActivity(this.activity)
                // console.log(this.budget)
            },
            filter() {
                $(".card").each(function () {
                    $(this).click(function () {
                        if($(this).hasClass('filter')) {
                            $(this).removeClass('filter');
                        } else {
                            $(this).addClass('filter')
                        }
                    })
                })
            },
            setActivity(activity){
                this.$store.dispatch("SET_SELECT_ACTIVITY", activity);
            },
        },
    }
</script>

<style lang="scss" scoped>
.field{
    display: flex;
    justify-content: center;
    align-content: center;
}
.box {
    display: inline-block;
    border-radius: 10px;
    width: 160px;
    height: 100px;
    margin: 2rem 1rem;
}
.card {
    width: 160px;
    height: 100px;
}
.filter {
    filter: grayscale(100%);
}
</style>