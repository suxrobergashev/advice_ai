<script setup lang="ts">
interface Props {
  title: string;
  desc: string;
  link?: string;
}

defineProps<Props>();
</script>

<template>
  <div>
    <p
      class="text-[#141920] font-[900] leading-6 ms:leading-[30px] sm:leading-10 text-xl ms:text-2xl sm:text-[32px] tracking-[-1px]"
    >
      {{ title }}
    </p>
    <p
      class="text-[#141920] mt-2 sm:mt-4 leading-[23px] ms:leading-6 sm:leading-[30px] text-base ms:text-lg sm:text-xl font-medium"
    >
      {{ desc }}
    </p>
    <a
      href="#"
      class="cursor-pointer text-[#49549D] leading-[30px] font-bold mt-4 ms:mt-6 sm:mt-10 lg:mt-12 hover:text-blue-800 inline-block"
      >Batafsil malumot</a
    >
  </div>
</template>
