<template>
      <section>
            <v-list-item two-line class="itmesBtn" to="/Login">
                  <v-list-item-avatar>
                        <v-btn icon>
                              <v-icon v-if="!user.loggedIn">{{
                                    user.img
                              }}</v-icon>
                              <img v-else :src="user.img" />
                        </v-btn>
                  </v-list-item-avatar>

                  <v-list-item-content>
                        <v-list-item-title>{{ user.name }}</v-list-item-title>
                  </v-list-item-content>
            </v-list-item>
      </section>
</template>

<script>
function dd() {
      return {
            loggedIn: false,
            img: 'mdi-account',
            name: 'Sign In',
      }
}
export default {
      props: {
            user: {
                  type: Object,
                  required: false,
                  default: dd(),
            },
      },
      data() {
            return {}
      },
      mounted() {
            setInterval(() => {
                  var userEmail = this.$store.getters['authModule/getUserEmail']
                  if (userEmail != undefined && userEmail != '') {
                        this.user.name = userEmail
                  }
            }, 5000)
      },
}
</script>

<style>
.itmesBtn {
      justify-content: center;
      margin: 0 !important;
}
</style>
