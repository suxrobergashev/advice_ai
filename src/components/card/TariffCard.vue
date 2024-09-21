<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import { ITariff } from "@/types/tariff";

interface Props {
  data: ITariff;
}

withDefaults(defineProps<Props>(), {});
</script>

<template>
  <div class="" :key="data.id">
    <div
      class="flex items-center w-full border-b border-[#9696964D] pb-3 ms:pb-4 justify-center gap-2"
    >
      <img
        v-if="data.type == 'simple'"
        src="@/assets/icon/cup.svg"
        alt="icon"
      />
      <img
        v-if="data.type == 'middle'"
        src="@/assets/icon/shlap.svg"
        alt="icon"
      />
      <img
        v-if="data.type == 'gold'"
        src="@/assets/icon/karona.svg"
        alt="icon"
      />
      <p class="font-bold text-xl ms:text-2xl leading-7">{{ data.tariff }}</p>
    </div>
    <div class="mt-5 sm:mt-7">
      <p class="text-sm text-center">
        <span
          class="uppercase font-bold text-[26px] ms:text-3xl md:text-[34px]"
          >{{ data.price }}</span
        >
        /oyiga
      </p>
      <p class="text-sm text-[#BAE06A] mt-3 sm:mt-4 text-center leading-4">
        Oylik obunalar uchun
      </p>
      <div class="mt-2 sm:mt-4 md:mt-6 flex flex-col items-start pl-2 gap-[6px]">
        <div
          class="flex items-center justify-start gap-2"
          v-for="(item, index) in data.services"
          :key="item.id"
        >
          <i
            class="fa-solid fa-check text-xl sm:text-2xl"
            :class="index < data.count ? 'text-[#21AE2E]' : 'text-[#808080]'"
          ></i>
          <p class="text-[#6E7C90]">{{ item.title }}</p>
        </div>
      </div>
      <div class="mt-6 sm:mt-8 md:mt-[60px] flex justify-center">
        <SButton variant="white" class="!text-base sm:text-lg">Tanlang</SButton>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
