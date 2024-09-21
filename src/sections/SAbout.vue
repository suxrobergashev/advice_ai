<template>
  <div class="container">
    <div
      class="bg-white rounded-[30px] sm:rounded-[36px] px-6 sm:px-9 pt-6 md:pt-11 pb-6 sm:pb-8 md:pb-14 mt-6 sm:mt-10 md:!mt-[65px]"
    >
      <p
        class="text-[#BAE06A] font-bold text-[34px] sm:text-[40px] md:text-[58px] sm:px-7 leading-10 sm:leading-[70px]"
      >
        {{ $t("about") }}
      </p>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8 sm:gap-10 dm:gap-[80px] mt-8 sm:mt-10 md:mt-[68px]"
      >
        <div class="" v-for="item in aboutInfo" :key="item.id">
          <AboutCard :info="item" />
        </div>
      </div>
      <div
        class="mt-6 sm:mt-10 md:mt-[50px] text-[#5E6282] font-medium text-base sm:text-lg md:text-xl leading-[22px] sm:leading-6 md:leading-[26px] text-center md:px-[54px]"
      >
        Bizning sun'iy intellekt maslahatchimiz o'quvchilarga qiziqishlari va
        ko'nikmalariga asoslanib, mos yo'nalishlarni aniqlashda yordam beradi. U
        zamonaviy texnologiyalar va ma'lumotlar tahliliga tayanib,
        o'quvchilarning shaxsiy qiziqishlariga mos keluvchi kasblar va
        yo'nalishlarni tavsiya qiladi.
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AboutCard from "@/components/card/AboutCard.vue";
const aboutInfo = [
  {
    id: 1,
    title: "1200+ faol foydalanuvchi",
    icon: "fa-solid fa-user",
    description:
      "Biz orqali foydalanuvchilarimiz o'z iqditorlarini aniqlab kelishmoqda",
  },
  {
    id: 2,
    title: "15+ xususiy maktablar",
    icon: "fa-solid fa-school",
    description:
      "Biz orqali foydalanuvchilarimiz o'z iqditorlarini aniqlab kelishmoqda",
  },
  {
    id: 3,
    title: "100+ Mutahasislik kurslari",
    icon: "fa-solid fa-book",
    description:
      "Biz orqali foydalanuvchilarimiz o'z iqditorlarini aniqlab kelishmoqda",
  },
  {
    id: 4,
    title: "1 000+ Mutahasislik testlari",
    icon: "fa-solid fa-brain",
    description:
      "Biz orqali foydalanuvchilarimiz o'z iqditorlarini aniqlab kelishmoqda",
  },
];
</script>
