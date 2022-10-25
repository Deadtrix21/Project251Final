<template>
      <div class="">
            <v-navigation-drawer
                  absolute
                  permanent
                  left
                  expand-on-hover
                  mini-variant-width="50px"
            >
                  <TheUserBar />
                  <v-divider />
                  <v-list nav>
                        <v-list-item
                              v-for="(item, index) in PagesTitle"
                              :key="index"
                              :to="item.path"
                        >
                              <v-list-item-icon>
                                    <v-icon>{{ item.mdi }}</v-icon>
                              </v-list-item-icon>
                              <v-list-item-title>
                                    {{ item.name }}
                              </v-list-item-title>
                        </v-list-item>
                  </v-list>
            </v-navigation-drawer>
      </div>
</template>
<script>
import TheUserBar from './common/TheUserBar.vue'
export default {
      components: { TheUserBar },
      computed: {
            PagesTitle() {
                  return this.$store.getters['NavPages/pager']
            },
      },
}
</script>
<style></style>
