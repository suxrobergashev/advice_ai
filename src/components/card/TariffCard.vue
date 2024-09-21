<script setup lang="ts">
import SButton from "@/components/SButton.vue";

interface Props {
  type: "simple" | "middle" | "gold";
}

withDefaults(defineProps<Props>(), {
  type: "simple",
});
</script>

<template>
  <div class="">
    <div
      class="flex items-center w-full border-b border-[#9696964D] pb-3 ms:pb-4 justify-center gap-2"
    >
      <img v-if="type == 'simple'" src="@/assets/icon/cup.svg" alt="icon" />
      <img v-if="type == 'middle'" src="@/assets/icon/shlap.svg" alt="icon" />
      <img v-if="type == 'gold'" src="@/assets/icon/karona.svg" alt="icon" />
      <p class="font-bold text-xl ms:text-2xl leading-7">Ежемесячно</p>
    </div>
    <div class="mt-5 sm:mt-7">
      <p class="text-sm text-center">
        <span class="uppercase font-bold text-[26px] ms:text-3xl md:text-[34px]"
          >$08.99</span
        >
        /за месяц
      </p>
      <p class="text-sm text-[#BAE06A] mt-3 sm:mt-4 text-center leading-4">
        Оплата каждый месяц
      </p>
      <div class="mt-2 sm:mt-4 md:mt-6 flex flex-col items-center gap-[6px]">
        <div
          class="flex items-center gap-2"
          v-for="(item, index) in 7"
          :key="item"
        >
          <i
            class="fa-solid fa-check text-xl sm:text-2xl"
            :class="index < 5 ? 'text-[#21AE2E]' : 'text-[#808080]'"
          ></i>
          <p class="text-[#6E7C90]">Скрипты продаж</p>
        </div>
      </div>
      <div class="mt-6 sm:mt-8 md:mt-[60px] flex justify-center">
        <SButton variant="white" class="!text-base sm:text-lg">Выбрать</SButton>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
