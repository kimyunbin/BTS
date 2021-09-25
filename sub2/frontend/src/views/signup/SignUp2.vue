<template>
    <div id="signup">
    <section class="section" style="padding-top: .5rem">
        <div class="container">
            <div class="columns">
                <div class="column is-8 is-offset-2">
                    <horizontal-stepper :steps="demoSteps" @completed-step="completeStep" :top-buttons="false"
                                        @active-step="isStepActive" @stepper-finished="alert"></horizontal-stepper>
                </div>
            </div>
        </div>
    </section>
    </div>
</template>

<script>
    import HorizontalStepper from '../../components/HorizontalStepper.vue';

    import StepOne from './StepOne.vue';
    import StepTwo from './StepTwo.vue';
    import StepThree from './StepThree.vue';
    import StepFour from './StepFour.vue';
    import StepFive from './StepFive.vue';
    import StepSix from './StepSix.vue';
    // import StepTwo from './Stepexample.vue';

    const teamUrl = 'https://github.com/PygmySlowLoris';
    const repoUrl = 'https://github.com/PygmySlowLoris/vue-stepper';

    export default {
        name: 'signup',
        components: {
            HorizontalStepper
        },
        data(){
            return {
                repoUrl: repoUrl,
                teamUrl: teamUrl,
                demoSteps: [
                    {
                        icon: 'monetization_on',
                        name: 'first',
                        title: '경비',
                        subtitle: '',
                        component: StepOne,
                        completed: false
                    },
                    {
                        icon: 'people',
                        name: 'second',
                        title: '여행인원',
                        subtitle: '',
                        component: StepTwo,
                        completed: false
                    },
                    {
                        icon: 'accessibility_new',
                        name: 'third',
                        title: '동반자',
                        subtitle: '',
                        component: StepThree,
                        completed: false
                    },
                    {
                        icon: 'flight_land',
                        name: 'fourth',
                        title: '교통수단',
                        subtitle: '',
                        component: StepFour,
                        completed: false
                    },
                    {
                        icon: 'search',
                        name: 'fifth',
                        title: '여행지 선택이유',
                        subtitle: '',
                        component: StepFive,
                        completed: false
                    },
                    {
                        icon: 'flag',
                        name: 'sixth',
                        title: '여행활동',
                        subtitle: '',
                        component: StepSix,
                        completed: false
                    },
                ],
                activeStep: 0
            }
        },
        computed: {},
        methods: {
            completeStep(payload) {
                this.demoSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        step.completed = true;
                    }
                })
            },
            isStepActive(payload) {
                this.demoSteps.forEach((step) => {
                    if (step.name === payload.name) {
                        if(step.completed === true) {
                            step.completed = false;
                        }
                    }
                })
            },
            alert(payload) {
                alert('end')
            }
        }
    }
</script>

<style scoped>
    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    .pointer {
        cursor: pointer;
    }

    h1, h2 {
        font-weight: normal;
    }

    hr {
        background-color: transparent;
        border: none;
        display: block;
        height: inherit;
        margin: 1.5rem 0;
        border-top: dashed 1px;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #0b99b9;
        text-decoration: underline;
    }

    .text-medium-grey {
        color: #333;
    }

    .text-light-grey {
        color: #888;
    }

    .box.formated {
        position: relative;
        padding: 0;
    }

    .box.formated .heading {
        font-size: 1rem;
        text-transform: capitalize;
        padding: .8rem 1.5rem;
        background-color: #fafafa;
    }

    .box.formated .content {
        padding: 1rem 2rem;
    }

    i.top-left {
        position: absolute;
        left: 1.5rem;
        top: 0.8rem;
    }

    .vertical-separator {
        display: flex;
        justify-content: space-around;
    }

    .vertical-separator .line {
        border-right: 1px solid #cccccc;
    }
</style>
