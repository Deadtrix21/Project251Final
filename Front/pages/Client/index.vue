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
                              <v-list-group :value="true" no-action sub-group>
                                    <template v-slot:activator>
                                          <v-list-item-content>
                                                <v-list-item-title>
                                                      <div
                                                            v-if="
                                                                  item.alias ==
                                                                        '' ||
                                                                  item.alias ==
                                                                        null ||
                                                                  item.alias ==
                                                                        'null' ||
                                                                  (item.alias ==
                                                                        'undefined') |
                                                                        (item.alias ==
                                                                              undefined)
                                                            "
                                                      >
                                                            {{ item.name }}
                                                            <v-btn
                                                                  @click="
                                                                        setName(
                                                                              item
                                                                        )
                                                                  "
                                                                  class="mx-10"
                                                                  >Edit
                                                                  Name</v-btn
                                                            >
                                                      </div>
                                                      <div v-else>
                                                            <v-list-item>
                                                                  <v-list-item-content>
                                                                        <v-list-item-title
                                                                              class="text-h6"
                                                                        >
                                                                              {{
                                                                                    item.alias
                                                                              }}
                                                                              <v-btn
                                                                                    @click="
                                                                                          setName(
                                                                                                item
                                                                                          )
                                                                                    "
                                                                                    class="mx-10"
                                                                                    >Edit
                                                                                    Name</v-btn
                                                                              >
                                                                        </v-list-item-title>
                                                                        <v-list-item-subtitle
                                                                              >ID
                                                                              {{
                                                                                    item.name
                                                                              }}</v-list-item-subtitle
                                                                        >
                                                                  </v-list-item-content>
                                                            </v-list-item>
                                                      </div>
                                                </v-list-item-title>
                                          </v-list-item-content>
                                    </template>

                                    <v-list-item
                                          v-for="device in item['listing']"
                                          :key="device.id"
                                          link
                                    >
                                          <div class="d-inline-flex items">
                                                <section class="mx-5">
                                                      {{ device.id }}
                                                </section>
                                                <section class="mx-5">
                                                      {{ device.level }}
                                                </section>
                                                <section class="mx-5">
                                                      {{ device.current }}
                                                </section>
                                          </div>
                                    </v-list-item>
                              </v-list-group>
                        </v-list-item>
                  </v-list-item-group>
            </v-list>
      </v-container>
</template>
<script>
export default {
      middleware: ['auth'],
      data() {
            return {
                  core: [],
                  newArray: [],
            }
      },
      methods: {
            setName(item) {
                  console.log(item)
                  const name = prompt('Give a name for the Sensor Group')
                  this.$store.commit('authModule/setAlias', {
                        obj: item,
                        alias: name,
                  })
                  this.$store.dispatch('authModule/uploadAlias')
            },
      },
      mounted() {
            setInterval(() => {
                  const details = this.$store.getters['authModule/getAll']
                  let structure = `{
                        deviceGet(uuid:"${details.uuid}")
                              {
                                    alias
                                    name
                                    uuid
                                    listing{
                                          id
                                          current
                                          level
                                    }
                              }
                  }`
                  this.$axios
                        .post(
                              `http://${window.location.hostname}:5000/devices`,
                              { query: structure }
                        )
                        .then((data) => {
                              try {
                                    let arrayA = []
                                    const dataset = data.data.data.deviceGet
                                    dataset.forEach((element) => {
                                          element.active = false
                                          arrayA.push(element)
                                    })
                                    this.core = dataset
                              } catch (e) {
                                    console.log(e)
                              }
                        })
                        .catch((e) => {
                              console.log(e)
                        })
            }, 10000)
      },
}
</script>
<style>
.items {
      width: 100%;
}
</style>
