<script setup lang="ts">
import { onMounted, ref } from "vue";
import Header from "@/components/SHeader.vue";
import SLoading from "@/components/SLoading.vue";
import Footer from "@/components/SFooter.vue";

const isLoading = ref(true);
onMounted(() => {
  setTimeout(() => {
    isLoading.value = false;
  }, 1500);
});
</script>

<template>
  <div
    class="bg-#fff h-full overflow-hidden min-h-[100vh] flex flex-col justify-between"
  >
    <div>
      <Header />
      <SLoading v-if="isLoading" />
      <router-view />
    </div>
    <Footer class="pt-6 dm:pt-[160px]" />
  </div>
</template>

<style scoped></style>
