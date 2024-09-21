<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import TariffCard from "@/components/card/TariffCard.vue";
</script>

<template>
  <div class="container">
    <div
      class="bg-[#141920] rounded-[30px] sm:rounded-[40px] px-6 sm:px-16 pt-6 sm:pt-10 md:pt-16 pb-6 sm:pb-[38px] mt-6 sm:mt-10 md:!mt-[60px]"
    >
      <div
        class="flex justify-between sm:items-center flex-col sm:flex-row gap-4"
      >
        <p
          class="text-[#BAE06A] font-bold text-[34px] sm:text-[40px] md:text-[58px] sm:px-7 leading-10 sm:leading-[70px]"
        >
          {{ $t("tariff") }}
        </p>
        <SButton variant="gray" class="text-base sm:text-lg"
          >Попробовать бесплатно</SButton
        >
      </div>
      <div
        class="grid grid-cols-1 md:grid-cols-3 mt-6 sm:mt-[50px] md:mt-[60px] gap-8 md:gap-0"
      >
        <TariffCard class="md:border-r border-[#9696964D]" />
        <TariffCard class="md:border-r border-[#9696964D]" type="middle" />
        <TariffCard type="gold" />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
