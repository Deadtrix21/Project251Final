<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <div id="items">
            <v-container grid-list-xs>
                  <v-alert
                        v-model="work"
                        dense
                        outlined
                        dismissible
                        type="success"
                  >
                        Success
                  </v-alert>
                  <v-alert
                        v-model="failed"
                        dense
                        outlined
                        dismissible
                        type="error"
                  >
                        An Error Occurred
                  </v-alert>
                  <v-card>
                        <section class="d-inline-flex">
                              <h3 class="pa-4 mx-6">Manage Users</h3>
                              <h3 class="mx-6 d-none d-sm-flex">
                                    <section class="d-flex">
                                          <v-combobox
                                                v-model="select"
                                                class="pa-4"
                                                :items="rebuild"
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
                                                <v-btn @click="sort()"
                                                      >Search</v-btn
                                                >
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
                                                :items="rebuild"
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
                                                <th class="text-left">UUID</th>
                                                <th class="text-left">
                                                      Actions
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
                                                <td>
                                                      <v-btn
                                                            color="error"
                                                            @click="
                                                                  deleteAccount(
                                                                        item
                                                                  )
                                                            "
                                                            >Delete</v-btn
                                                      >
                                                </td>
                                          </tr>
                                    </tbody>
                              </template>
                        </v-simple-table>
                  </v-card>

                  <v-card class="my-10">
                        <section class="d-inline-flex">
                              <h3 class="pa-4 mx-6">Manage Devices</h3>
                              <h3 class="mx-6 d-inline-flex">
                                    <section class="d-flex">
                                          <v-text-field
                                                label="Filter"
                                                placeholder="Name"
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
                                                <th class="text-left">UUID</th>
                                                <th class="text-left">
                                                      Actions
                                                </th>
                                          </tr>
                                    </thead>
                                    <tbody>
                                          <tr
                                                v-for="item in DeviceArray"
                                                :key="item.name"
                                          >
                                                <td>{{ item.name }}</td>
                                                <td>{{ item.uuid }}</td>
                                                <td>
                                                      <v-btn
                                                            color="error"
                                                            @click="deleteDevice(item)"
                                                            >Delete</v-btn
                                                      >
                                                      <v-btn
                                                            color="success"
                                                            @click="linkDevice(item)"
                                                            >Link To</v-btn
                                                      >
                                                </td>
                                          </tr>
                                    </tbody>
                              </template>
                        </v-simple-table>
                  </v-card>
            </v-container>
      </div>
</template>
<script>
var _ = require('lodash')

export default {
      middleware: ['checkAuth'],
      data() {
            return {
                  work: false,
                  failed: false,
                  select: '',
                  filterBy: '',
                  rebuild: ['uuid', 'email', 'token', 'none'],
                  coreArray: [],
                  DeviceArray: [],
            }
      },
      mounted() {
            setInterval(() => {this.refresh()}, 4000)
      },
      methods: {
            refresh() {
                        this.$store.dispatch('authModule/getAllUsers')
                        this.$store.dispatch('authModule/getAllDevice')
                        setTimeout(() => {
                              let query = this.$store.getters['authModule/getAllUser']
                              let queryD = this.$store.getters['authModule/getAllDevices']
                              this.DeviceArray = queryD
                              this.coreArray = query
                        }, 3000)
            },
            sort() {
                  try {
                        let word = `${this.filterBy}`
                        let bythis = this.select
                        if (bythis == 'none') {
                              this.coreArray = this.getNew()
                        } else {
                              this.$store.dispatch('authModule/getAllUsers')
                              setTimeout(() => {
                                    let query =
                                          this.$store.getters[
                                                'authModule/getAllUser'
                                          ]
                                    this.coreArray = _.filter(query, [
                                          bythis,
                                          word,
                                    ])
                              }, 3000)
                        }
                  } catch (error) {
                        this.failed = true
                  }
            },
            deleteAccount(item) {
                  let query = this.$store.getters['authModule/getUserEmail']
                  if (item.email == query) {
                        this.failed = true
                        alert('cannot delete own accout')
                  } else if (item.email == 'test@outlook.com') {
                        this.work = false
                        this.failed = true
                        alert('This is the super admin account')
                  } else {
                        this.$store.commit(
                              'authModule/setDeleteAccount',
                              item.email
                        )
                        let check = this.$store.dispatch(
                              'authModule/deleteUserAccount'
                        )
                        this.work = true
                        this.failed = false
                  }
                  this.refresh()
            },
            deleteDevice(item) {
                  this.$store.commit('authModule/setDeleteDevice', item.name)
                  this.$store.dispatch('authModule/deleteDeviceAccount')
                  this.refresh();
                  this.work = true
                  this.failed = false
            },
            linkDevice(item) {
                  const uuid = prompt('set a uuid')
                  if (uuid != undefined && uuid != null) {
                        this.$store.commit('authModule/setLinkDevice', {
                              link: uuid,
                              name: item.name,
                        })
                        this.$store.dispatch('authModule/linkDeviceAccount')
                        this.refresh();
                        this.work = true
                        this.failed = false
                  }else{
                        this.work = false
                        this.failed = true
                  }
            },
      },
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