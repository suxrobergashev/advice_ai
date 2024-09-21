<script setup lang="ts">
import BlockquoteSVG from "@/assets/icon/BlockquoteSVG.vue";

interface Props {
  id: number;
  comment: string;
  logo: string;
  title: string;
}

defineProps<Props>();
function getImageUrl(name: string) {
  return new URL(`../../assets/images/fake-images/${name}.png`, import.meta.url)
    .href;
}
</script>

<template>
  <div class="bg-[#F5F5F4] rounded-[4px] p-[18px]">
    <p class="font-medium text-[#8C97AB] leading-[22px]">
      {{ comment }}
    </p>
    <div class="mt-4 flex justify-between items-center">
      <div class="flex items-center">
        <img :src="getImageUrl(logo)" alt="logo" />
        <p
          class="text-base ms:text-lg text-[#8C97AB] font-medium leading-[22px]"
        >
          {{ title }}
        </p>
      </div>
      <BlockquoteSVG class="w-[54px] ms:w-[64px]" />
    </div>
  </div>
</template>
