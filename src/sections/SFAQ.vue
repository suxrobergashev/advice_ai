<template>
  <div class="container">
    <div
      class="bg-white rounded-[30px] sm:rounded-[36px] px-6 sm:px-9 pt-6 md:pt-11 pb-6 sm:pb-8 md:pb-14 mt-6 sm:mt-10 md:!mt-[65px]"
    >
      <p
        class="text-[#BAE06A] font-bold text-[34px] sm:text-[40px] md:text-[58px] leading-10 sm:leading-[70px]"
      >
        FAQ
      </p>

      <div class="grid grid-cols-1 gap-3 mt-4 sm:mt-6">
        <div
          data-aos="zoom-in"
          :data-aos-delay="index * 50"
          v-for="(item, index) in faqData"
          :key="index"
        >
          <AccordionItem v-bind="item" :index="index + 1" />
        </div>
      </div>
      <router-link to="/faq" class="flex justify-end mt-4 ms:mt-8">
        <SButton variant="light" class="sm:max-w-[256px] sm:w-full"
          >Ko'proq ko'rish
          <template #pre>
            <i class="fa-solid fa-arrow-right text-white pl-2"></i>
          </template>
        </SButton>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import AccordionItem from "@/components/card/AccordionItem.vue";


const faqData = [
  {
    id: 1,
    question: "Advice AI dan qanday to'g'ri foydalanish mumkin?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 2,
    question: "Advice AI iqtidorga munosib universetutlarni taqdim etaoladimi?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 3,
    question:
      "Tizimdan foydalin qanday qilib sohaga oid testlarni ishlash mumkin?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 4,
    question:
      "Advice AI mutahassislikga oid o'quv kurslarni ham taqdim etadimi?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 5,
    question: "Advice AI ning premium tariflarida qanday imkoniyatlar mavjud?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
];
</script>
