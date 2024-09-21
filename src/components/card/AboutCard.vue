<script setup lang="ts">
interface Props {
  info: {
    id: number;
    icon: string;
    title: string;
    description: string;
  };
}

defineProps<Props>();
</script>

<template>
  <div class="text-center">
    <div
      class="w-[56px] h-[56px] rounded-xl bg-[#49549D] flex justify-center items-center mx-auto"
    >
      <div class="text-2xl" :class="info?.icon"></div>
    </div>
    <p class="mt-2 sm:mt-4 font-bold text-xl text-[#1E1D4C]">
      {{ info?.title }}
    </p>
    <p class="mt-1 sm:mt-3 md:mt-4 text-[#5E6282] font-semibold leading-[26px]">
      {{ info?.description }}
    </p>
  </div>
</template>

<style scoped></style>
