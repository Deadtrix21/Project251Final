<template>
      <section>
            <v-list-item two-line class="itmesBtn">
                  <v-list-item-avatar>
                        <v-btn icon to="/Login">
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
const def = () => {
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
                  default: def,
            },
      },
}
</script>

<style>
.itmesBtn {
      justify-content: center;
      margin: 0 !important;
}
</style>
