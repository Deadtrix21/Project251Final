<!-- eslint-disable vue/multi-word-component-names -->
<template>
      <v-container>
            <section v-for="Single in BlogPosts" :key="Single.id">
                  <h1>{{ Single.id }} - {{ Single.title }}</h1>
            </section>
      </v-container>
</template>

<script lang="ts">
export default {
      computed: {
            BlogPosts(): any {
                  return this.$store.getters.loadPosts
            },
      },
}
</script>

<style scoped></style>
