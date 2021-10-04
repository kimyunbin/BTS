<template>
    <div style="padding: 2rem 3rem; text-align: left;">
        <h5><b>당신이 선호하는 여행지 교통수단은 무엇인가요?</b></h5>
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
    import one from "@/assets/img/교통수단/항공.jpeg";
    import two from "@/assets/img/교통수단/지하철.jpeg";
    import three from "@/assets/img/교통수단/관광버스.jpeg";
    import four from "@/assets/img/교통수단/렌트카.jpeg";
    import five from "@/assets/img/교통수단/기타.jpeg";
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
            ...mapGetters(["SET_SELECT_TRANSPORTATIONS"]),
        },
        methods: {
            onClick(index) {
                // console.log("index " , index);
                if(index === 1) {
                    this.transportations = "10000";
                }
                if(index === 2) {
                    this.transportations = "01000";
                }
                if(index === 3) {
                    this.transportations = "00010";
                }
                if(index === 4) {
                    this.transportations = "00100";
                }
                if(index === 5) {
                    this.transportations = "00001";
                }
                this.setTransportations(this.transportations)
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
            setTransportations(setTransportations){
                this.$store.dispatch("SET_SELECT_TRANSPORTATIONS", setTransportations);
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