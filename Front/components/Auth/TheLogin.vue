<template>
      <v-form ref="form" v-model="valid" lazy-validation>
            <v-container>
                  <v-container>
                        <v-text-field
                              v-model="email"
                              :rules="emailRules"
                              filled
                              dense
                              label="Email"
                        ></v-text-field>
                        <v-text-field
                              v-model="password"
                              :rules="passwordRules"
                              filled
                              dense
                              label="Password"
                        ></v-text-field>
                  </v-container>

                  <v-container id="buttonsForm">
                        <v-btn
                              :disabled="!valid"
                              color="success"
                              outlined
                              class="mr-2"
                              @click="validate"
                        >
                              Login
                        </v-btn>

                        <v-btn
                              color="error"
                              class="mr-2"
                              outlined
                              @click="reset"
                        >
                              Cancel
                        </v-btn>
                        <v-btn
                              color="primary"
                              outlined
                              @click="$emit('toggle')"
                        >
                              Sign Up
                        </v-btn>
                  </v-container>
            </v-container>
      </v-form>
</template>
<script>
export default {
      data() {
            return {
                  valid: false,
                  password: '',
                  passwordRules: [
                        (v) => !!v || 'Password is required',
                        (v) =>
                              (v && v.length <= 16) ||
                              'Password must be less than 16 characters',
                        (v) => {
                              if (v.length <= 5) {
                                    return 'Password must be more than 6 characters'
                              }
                        },
                  ],
                  email: '',
                  emailRules: [
                        (v) => !!v || 'E-mail is required',
                        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
                  ],
            }
      },
      methods: {
            validate() {

                  this.$store.commit("authModule/setUser", {
                        email: this.email,
                        password: this.password,
                  })
                  this.$store.commit("authModule/setLogin",true)
                  this.$store.dispatch("authModule/authenticateUser");
                  setTimeout(()=>{this.$router.push('/Client/')}, 1500)

            },
            reset() {
                  this.$refs.form.reset()
                  this.$router.push('/')
            },
      },
}
</script>
<style></style>
