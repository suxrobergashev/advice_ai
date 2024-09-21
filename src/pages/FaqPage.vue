<script setup lang="ts">
import AccordionItem from "@/components/card/AccordionItem.vue";

const faqData = [
  {
    id: 1,
    question: "Вы предоставляете услугу по установке виджета?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 2,
    question: "Могу я редактировать исходный код плагина?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 3,
    question:
      "Нужно ли мне устанавливать какое-либо оборудование / программное обеспечение на свой сервер, чтобы использовать \n" +
      "Этот виджет?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 4,
    question: "Могу я редактировать исходный код плагина?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 5,
    question:
      "Нужно ли мне устанавливать какое-либо оборудование / программное обеспечение на свой сервер, чтобы использовать \n" +
      "Этот виджет?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 6,
    question: "Могу я редактировать исходный код плагина?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 7,
    question:
      "Нужно ли мне устанавливать какое-либо оборудование / программное обеспечение на свой сервер, чтобы использовать \n" +
      "Этот виджет?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
  {
    id: 8,
    question: "Могу я редактировать исходный код плагина?",
    answer:
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
  },
];
</script>

<template>
  <div class="container pt-6 sm:pt-10 pb-12 sm:pb-[100px]">
    <h2
      class="text-[#252623] font-bold leading-[40px] break-words sm:leading-[70px] text-4xl sm:text-[58px] text-center"
    >
      {{ $t("faq_text") }}
    </h2>
    <div class="flex flex-col gap-2 sm:gap-[10px] mt-6 sm:mt-[60px]">
      <div
        data-aos="zoom-in"
        :data-aos-delay="index * 50"
        v-for="(item, index) in faqData"
        :key="index"
      >
        <AccordionItem class="!bg-white" v-bind="item" :index="index + 1" />
      </div>
    </div>
  </div>
</template>
