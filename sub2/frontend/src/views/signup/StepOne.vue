<template>
    
    <div style="padding: 2rem 3rem; text-align: left;">
        <form>

        <div class="field">
            <v-text-field
            name="name"
            color="blue"
            background-color="transparent"
            v-model="name"
            :error-messages="nameErrors"
            label="닉네임"
            required
            @blur="$v.name.$touch()"
            ></v-text-field>
            <v-btn @click="authentic()" color="blue" class="white--text">인증하기</v-btn>
        </div>
        <div class="field">
            <v-text-field
            type="email"
            color="blue"
            background-color="transparent"
            name="email"
            v-model="email"
            :error-messages="emailErrors"
            label="E-mail"
            required
            @blur="$v.email.$touch()"
            ></v-text-field>
        </div>
        <div class="field">
            <v-text-field
            :type="'password'"
            name="password"
            color="blue"
            background-color="transparent"
            v-model="password"
            
            label="비밀번호"
            ></v-text-field>
        </div>
        <div class="field">
            <v-text-field
            :type="'password'"
            name="passwordConfirm"
            color="blue"
            background-color="transparent"
            v-model="password_confirm"
            label="비밀번호확인"
            ></v-text-field>
        </div>
        <div class="field">
            <v-text-field
            :type="'password'"
            name="passwordConfirm"
            color="blue"
            background-color="transparent"
            v-model="password_confirm"
            label="나이"
            ></v-text-field>
        </div>
        <div class="field">
            <v-text-field
            :type="'password'"
            name="passwordConfirm"
            color="blue"
            background-color="transparent"
            v-model="password_confirm"
            label="성별"
            ></v-text-field>
        </div>
        <v-btn @click="clear">초기화</v-btn>
        </form>
    </div>
</template>

<script>
    import {validationMixin} from 'vuelidate'
    import {
        required,
        maxLength,
        email,
        minLength}
    from 'vuelidate/lib/validators'

    export default {
        props: ['clickedNext', 'currentStep'],
        mixins: [validationMixin],
        data() {
            return {
            name: "",
            email: "",
            password: "",
            password_confirm:"",
            error: {
                password_confirm: false,
            },
            };
        },
        validations: {
            name: { required, maxLength: maxLength(8) },
            email: { required, email },
            password: {required, minLength: minLength(8)}
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
            },
            password_confirm: function(v){
                this.checkForm();
            },
        },
        mounted() {
            if(!this.$v.$invalid) {
                this.$emit('can-continue', {value: true});
            } else {
                this.$emit('can-continue', {value: false});
            }
        },
        computed: {
            nameErrors() {
                const errors = [];
                if (!this.$v.name.$dirty) return errors;
                !this.$v.name.maxLength &&
                    errors.push("8글자 이내로 작성해주세요.");
                !this.$v.name.required && errors.push("이름을 입력해주세요.");
                return errors;
                },
            emailErrors() {
                const errors = [];
                if (!this.$v.email.$dirty) return errors;
                !this.$v.email.email && errors.push("@ 이메일 형식으로 입력해주세요.");
                !this.$v.email.required && errors.push("이메일을 입력해주세요.");
                return errors;
            }, 
            passwordErrors() {
                const errors = [];
                if (!this.$v.password.$dirty) return errors;
                !this.$v.password.minLength &&
                    errors.push("비밀번호가 8글자 이상이어야합니다.");
                !this.$v.body.required && errors.push("비밀번호를 확인해주세요");
                return errors;
            },
        },
        mathods: {
            submit() {
                this.$v.$touch();
            },
            clear() {
                this.$v.$reset();
                this.name = "";
                this.email = "";
                this.body = "";
                this.password = "";
                this.password_confirm = "";
            },
            checkForm() {
                if (this.password !== this.password_confirm)
                    this.error.password_confirm = "비밀번호가 다릅니다.";
                else this.error.password_confirm = false;


                let isSubmit = true;
                Object.values(this.error).map(v => {
                    if (v) isSubmit = false;
                });
                this.isSubmit = isSubmit;
            },
            authentic(){
                
            },
        },
    }
</script>