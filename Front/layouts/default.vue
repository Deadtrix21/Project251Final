<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <v-app dark>
            <TheHeader></TheHeader>
            <v-main id="context">
                  <Nuxt class="Nuxt" />
            </v-main>
      </v-app>
</template>

<script>
import TheHeader from '~/components/Navigation/TheHeader.vue'
export default {
      components: { TheHeader },
}
</script>
<style>
html,
body {
      margin: 0px;
      overflow: hidden;
      padding: 0px;
}

#context {
      margin-left: 45px !important;
}
</style>
