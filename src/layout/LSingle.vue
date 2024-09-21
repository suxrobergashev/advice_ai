<script setup lang="ts">
import SLoading from "@/components/SLoading.vue";
import Footer from "@/components/SFooter.vue";
import SingleLayoutHeader from "@/components/SingleLayoutHeader.vue";
</script>

<template>
  <div
    class="bg-#fff h-full overflow-hidden min-h-[100vh] flex flex-col justify-between"
  >
    <div>
      <SingleLayoutHeader />
      <!--      <SLoading v-if="isLoading" />-->
      <router-view />
    </div>
    <Footer class="pt-6 dm:pt-[140px]" />
  </div>
</template>

<style scoped></style>
