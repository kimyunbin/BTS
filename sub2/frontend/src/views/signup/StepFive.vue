<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 여행지를 선택하는 가장 큰 이유는 무엇인가요?</b></h5>
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
    import one from "@/assets/img/이유/지명도.png";
    import two from "@/assets/img/이유/볼거리.png";
    import three from "@/assets/img/이유/가격.png";
    import four from "@/assets/img/이유/거리.png";
    import five from "@/assets/img/이유/숙박.png";
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
                ],
                tooltip:[
                    "지명도",
                    "볼거리",
                    "이동거리",
                    "저렴한 가격",
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
            ...mapGetters(["SET_SELECT_SELECTION"]),
        },
        methods: {
            onClick(index) {
                // console.log("index " , index);
                if(index === 1) {
                    this.selection = "10000";
                }
                if(index === 2) {
                    this.selection = "01000";
                }
                if(index === 3) {
                    this.selection = "00010";
                }
                if(index === 4) {
                    this.selection = "00100";
                }
                if(index === 5) {
                    this.selection = "00001";
                }
                this.setSelection(this.selection)
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
            setSelection(selection){
                this.$store.dispatch("SET_SELECT_SELECTION", selection);
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