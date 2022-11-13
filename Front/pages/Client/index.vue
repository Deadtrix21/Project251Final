<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <v-container>
            <h1>Sensor info</h1>
            <v-card v-if="core.length == 0">
                  <h1>No Data Available</h1>
            </v-card>
            <v-list v-else>
                  <v-list-item-group>
                        <v-list-item v-for="item in core" :key="item.uid">
                              <v-list-item-content>
                                    <v-list-item-title>
                                          ID
                                          <h3>{{ item.uid }}</h3>
                                          <v-divider></v-divider>
                                    </v-list-item-title>
                                    <p
                                          v-for="(items, index) in item.today"
                                          :key="index"
                                    >
                                          <v-list-item>
                                                <v-list-item-content>
                                                      <v-list-item-title
                                                            class="text-h6"
                                                      >
                                                            {{ items.time }}
                                                      </v-list-item-title>
                                                      <v-list-item-subtitle>
                                                            <section>
                                                                  Level Number:
                                                                  {{
                                                                        items.level
                                                                  }}
                                                            </section>
                                                            <section>
                                                                  Level class:

                                                                  <metadiv
                                                                        v-if="
                                                                              items.level >
                                                                                    0 &&
                                                                              items.level <
                                                                                    300
                                                                        "
                                                                        >Dry
                                                                        soil</metadiv
                                                                  >
                                                                  <metadiv
                                                                        v-if="
                                                                              items.level >
                                                                                    300 &&
                                                                              items.level <
                                                                                    700
                                                                        "
                                                                        >Moist
                                                                        soil</metadiv
                                                                  >
                                                                  <metadiv
                                                                        v-if="
                                                                              items.level >
                                                                              700
                                                                        "
                                                                        >Under
                                                                        water
                                                                  </metadiv>
                                                            </section>
                                                      </v-list-item-subtitle>
                                                </v-list-item-content>
                                          </v-list-item>
                                    </p>
                              </v-list-item-content>
                        </v-list-item>
                  </v-list-item-group>
            </v-list>
      </v-container>
</template>
<script>
export default {
      middleware: [ 'auth'],
      data() {
            return {
                  core: [],
            }
      },
      mounted() {
            console.log(this.$store.getters['authModule/emailAuthed'])
            setInterval(() => {
                  this.$axios
                        .get(
                              'http://localhost:8001/devices/?email=' +
                                    this.$store.getters[
                                          'authModule/emailAuthed'
                                    ]
                        )
                        .then((res) => {
                              this.core = res.data.data
                        })
                        .catch((e) => {
                              console.log(e)
                        })
            }, 5000)
      },
      computed: {},
}
</script>
<style></style>
