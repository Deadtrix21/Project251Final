<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <v-container id="loginPage">
            <v-card class="widthModify">
                  <TheLogin
                        v-if="!loginToggle"
                        @toggle="toggleLoginPage()"
                        @userInfo="setUserInfo"
                  />
                  <TheSignUp v-else @toggle="toggleLoginPage()" />
            </v-card>
      </v-container>
</template>
<script>
import TheLogin from '../components/Auth/TheLogin.vue'
import TheSignUp from '../components/Auth/TheSignUp.vue'
export default {
      components: { TheLogin, TheSignUp },
      data() {
            return {
                  loginToggle: true,
            }
      },
      methods: {
            toggleLoginPage() {
                  this.loginToggle = !this.loginToggle
            },
            setUserInfo(value) {
                  this.$store.dispatch('authModule/setUserDetails', value)
            },
      },
}
</script>
<style>
#loginPage {
      display: flex;
      justify-content: center;
      align-items: center;
}
#buttonsForm {
      display: flex;
      justify-content: end;
}
</style>
