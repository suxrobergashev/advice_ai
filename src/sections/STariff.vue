<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import TariffCard from "@/components/card/TariffCard.vue";
import { ITariff } from "@/types/tariff";

const tariffCard: ITariff[] = [
  {
    id: 1,
    type: "simple",
    tariff: "Oddiy",
    price: "Bepul",
    count: 3,
    services: [
      {
        id: 1,
        title: "Advice AI dan foydalanish",
      },
      {
        id: 2,
        title: "300 ta request kunlik",
      },
      {
        id: 3,
        title: "Iqdtidorga munosib kasblarni ko'rish",
      },
      {
        id: 4,
        title: "Mutahasislik bo'yicha universetutlar ro'yxati",
      },
      {
        id: 5,
        title: "Mutahasislik bo'yicha o'quv markazlar ro'yxati",
      },
      {
        id: 6,
        title: "Mutahasislik bo'yicha online kurslar",
      },
      {
        id: 7,
        title: "Mutahasislik testlar",
      },
    ],
  },
  {
    id: 2,
    type: "middle",
    tariff: "Premium",
    price: "100 000 UZS",
    count: 5,
    services: [
      {
        id: 1,
        title: "Advice AI dan foydalanish",
      },
      {
        id: 2,
        title: "1 000 ta request kunlik",
      },
      {
        id: 3,
        title: "Iqdtidorga munosib kasblarni ko'rish",
      },
      {
        id: 4,
        title: "Mutahasislik bo'yicha universetutlar ro'yxati",
      },
      {
        id: 5,
        title: "Mutahasislik bo'yicha o'quv markazlar ro'yxati",
      },
      {
        id: 6,
        title: "Mutahasislik bo'yicha online kurslar",
      },
      {
        id: 7,
        title: "Mutahasislik testlar",
      },
    ],
  },
  {
    id: 3,
    type: "gold",
    tariff: "Premium Gold",
    price: "150 000 UZS",
    count: 7,
    services: [
      {
        id: 1,
        title: "Advice AI dan foydalanish",
      },
      {
        id: 2,
        title: "Cheksiz requestlar kunlik",
      },
      {
        id: 3,
        title: "Iqdtidorga munosib kasblarni ko'rish",
      },
      {
        id: 4,
        title: "Mutahasislik bo'yicha universetutlar ro'yxati",
      },
      {
        id: 5,
        title: "Mutahasislik bo'yicha o'quv markazlar ro'yxati",
      },
      {
        id: 6,
        title: "Mutahasislik bo'yicha online kurslar",
      },
      {
        id: 7,
        title: "Mutahasislik testlar",
      },
    ],
  },
];
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
          >Demoni ishlatib ko'rish
        </SButton>
      </div>
      <div
        class="grid grid-cols-1 md:grid-cols-3 mt-6 sm:mt-[50px] md:mt-[60px] gap-8 md:gap-0"
      >
        <TariffCard
          v-for="item in tariffCard"
          class="md:border-r border-[#9696964D]"
          v-bind:key="item.id"
          :data="item"
        />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
