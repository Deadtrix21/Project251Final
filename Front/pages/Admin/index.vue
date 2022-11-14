<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <div id="items">
            <v-container grid-list-xs>
                  <v-card>
                        <section class="d-inline-flex">
                              <h3 class="pa-4 mx-6">Manage Users</h3>
                              <h3 class="mx-6 d-none d-sm-flex">
                                    <section class="d-flex">
                                          <v-combobox
                                                v-model="select"
                                                class="pa-4"
                                                :items=rebuild
                                                label="Filter Option"
                                                dense
                                          ></v-combobox>
                                    </section>
                                    <section class="d-flex">
                                          <v-text-field
                                                label="Filter"
                                                placeholder="Email"
                                                v-model="filterBy"
                                          ></v-text-field>
                                          <div class="pa-4">
                                                <v-btn @click="sort()">Search</v-btn>
                                          </div>
                                    </section>
                              </h3>
                              <h3 class="mx-6 d-block d-sm-none">
                                    <section class="d-flex">
                                          <v-text-field
                                                label="Search"
                                                placeholder="Email"
                                          ></v-text-field>
                                          <div class="pa-4">
                                                <v-btn>Search</v-btn>
                                          </div>
                                    </section>
                                    <section class="d-flex">
                                          <v-combobox
                                                v-model="select"
                                                class="pa-4"
                                                :items=rebuild
                                                label="Filter Option"
                                                dense
                                          ></v-combobox>
                                    </section>
                                    <section class="d-flex">
                                          <v-text-field
                                                label="Filter"
                                                placeholder="Email"
                                          ></v-text-field>
                                          <div class="pa-4">
                                                <v-btn>Search</v-btn>
                                          </div>
                                    </section>
                              </h3>
                        </section>

                        <v-simple-table class="px-5 mx-5 py-2" height="300">
                              <template v-slot:default>
                                    <thead>
                                          <tr>
                                                <th class="text-left">Email</th>
                                                <th class="text-left">
                                                      UUID
                                                </th>
                                          </tr>
                                    </thead>
                                    <tbody>
                                          <tr
                                                v-for="item in coreArray"
                                                :key="item._id"
                                          >
                                                <td>{{ item.email }}</td>
                                                <td>{{ item.uuid }}</td>
                                          </tr>
                                    </tbody>
                              </template>
                        </v-simple-table>
                  </v-card>
                  <v-card class="my-10">
                        <section class="d-inline-flex">
                              <h3 class="pa-4 mx-6">Manage Devices</h3>
                              <h3 class="mx-6 d-inline-flex">
                                    <v-text-field

                                          label="Search"
                                          placeholder="Email"
                                    ></v-text-field>
                                    <div class="pa-4">
                                          <v-btn>Search</v-btn>
                                    </div>
                              </h3>
                        </section>

                        <v-simple-table class="px-5 mx-5 py-2" height="300">
                              <template v-slot:default>
                                    <thead>
                                          <tr>
                                                <th class="text-left">Email</th>
                                                <th class="text-left">
                                                      UUID
                                                </th>
                                          </tr>
                                    </thead>
                                    <tbody>
                                          <tr
                                                v-for="item in coreArray"
                                                :key="item._id"
                                          >
                                                <td>{{ item.email }}</td>
                                                <td>{{ item.uuid }}</td>
                                          </tr>
                                    </tbody>
                              </template>
                        </v-simple-table>
                  </v-card>
            </v-container>
      </div>
</template>
<script>
var _ = require('lodash');

export default {
      data() {
            return {
                  select : "",
                  filterBy : "",
                  rebuild : [
                              "uuid",
                              "email",
                              "token",
                              "none"
                        ],
                  coreArray : [],
            }
      },
      methods: {
            sort(){
                  let word = `${this.filterBy}`
                  let bythis = this.select
                  if (bythis == "none"){
                        this.coreArray = this.getNew()
                  }
                  else{
                        this.$store.dispatch('authModule/getAllUsers')
                        setTimeout(()=>{
                              let query = this.$store.getters["authModule/getAllUser"]
                              this.coreArray = _.filter(query, [bythis, word]);
                  }, 3000)

                  }
            }
      },
      mounted() {
            this.$store.dispatch('authModule/getAllUsers')
            setTimeout(()=>{
                  let query = this.$store.getters["authModule/getAllUser"]
                  this.coreArray = query
            }, 5000)


      }
}
</script>
<style>
#items {
      overflow-y: auto;
      height: 96vh;
}
*::-webkit-scrollbar {
      width: 4px !important;
}

*::-webkit-scrollbar-track {
      box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3) !important;
}

*::-webkit-scrollbar-thumb {
      background-color: rgba(0, 0, 0, 0.5);
}
</style>
