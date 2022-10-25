<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <v-card class="ma-4 pa-4 d-flex row-reverse">
            <v-tabs show-arrows>
                  <v-tab>
                        <v-icon> mdi-palette </v-icon>
                        Theme
                  </v-tab>

                  <v-tab-item>
                        <v-card flat>
                              <v-divider />
                              <v-card-text>
                                    <v-container>
                                          <secion id="themeTitle"
                                                >Toggle Website Theme
                                          </secion>
                                          <v-btn
                                                @click="ThemeChanger()"
                                                v-if="$vuetify.theme.dark"
                                          >
                                                <v-icon
                                                      >mdi-white-balance-sunny</v-icon
                                                >
                                          </v-btn>
                                          <v-btn @click="ThemeChanger()" v-else>
                                                <v-icon
                                                      >mdi-weather-night</v-icon
                                                >
                                          </v-btn>
                                    </v-container>
                              </v-card-text>
                        </v-card>
                  </v-tab-item>
            </v-tabs>
      </v-card>
</template>
<script>
export default {
      methods: {
            ThemeChanger() {
                  this.$vuetify.theme.dark = !this.$vuetify.theme.dark
            },
      },
}
</script>
<style>
#child {
      padding: 10px;
}
</style>
