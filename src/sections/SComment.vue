<template>
  <div class="container">
    <div
      class="mt-6 sm:mt-10 md:!mt-[60px] bg-white rounded-[30px] sm:rounded-[36px] px-6 sm:px-8 py-4 md:py-7"
    >
      <div class="flex items-center justify-between">
        <p
          class="text-[#BAE06A] font-bold text-[34px] ms:text-[40px] md:text-[58px] leading-10 sm:leading-[70px]"
        >
          {{ $t("comment") }}
        </p>
        <div class="flex items-center gap-3 ms:gap-4 md:gap-7">
          <div
            class="swiper-button-prev cursor-pointer w-9 ms:w-11 h-9 ms:h-11 rounded-[8px] flex justify-center items-center bg-[#F5F5F4] transition duration-300 hover:bg-[#E3E3E2]"
          >
            <i
              class="fa-solid fa-chevron-left text-[#0062FF] text-lg ms:text-xl"
            ></i>
          </div>

          <div
            class="swiper-button-next cursor-pointer w-9 ms:w-11 h-9 ms:h-11 rounded-[8px] flex justify-center items-center bg-[#F5F5F4] transition duration-300 hover:bg-[#E3E3E2]"
          >
            <i
              class="fa-solid fa-chevron-right text-[#0062FF] text-lg ms:text-xl"
            ></i>
          </div>
        </div>
      </div>
      <div class="mt-3 ms:mt-4">
        <swiper
          :slidesPerView="3"
          :spaceBetween="32"
          :modules="[Autoplay, Navigation]"
          :loop="true"
          :autoplay="true"
          :delay="300"
          :pauseOnMouseEnter="true"
          :breakpoints="{
            '320': { slidesPerView: 1, spaceBetween: 15 },
            '480': { slidesPerView: 1, spaceBetween: 20 },
            '640': { slidesPerView: 1, spaceBetween: 20 },
            '768': { slidesPerView: 2, spaceBetween: 30 },
          }"
          class="mySwiper"
        >
          <swiper-slide
            v-for="(item, index) in sliderData"
            :key="index"
            class="!self-stretch"
          >
            <CommentCard class="!self-stretch" v-bind="item" />
          </swiper-slide>
        </swiper>
      </div>
      <div class="flex justify-end mt-4 ms:mt-8">
        <SButton variant="light">Fikr yuborish</SButton>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Autoplay, Navigation } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import CommentCard from "@/components/card/CommentCard.vue";
import "swiper/css";
import SButton from "@/components/SButton.vue";

const sliderData = [
  {
    id: 1,
    comment:
      "Отличная задумка и есть потенциал данной\n" +
      "платформы. Платформа действительно интересная\n" +
      "и вериться в то, что ее еще ждет успех",
    logo: "logo",
    title: "SKY logistics",
  },
  {
    id: 2,
    comment:
      "Chat.im - это удобный чат-сервис для службы поддержки на базе искусственного интеллекта.",
    logo: "logo2",
    title: "Scipher medicine ",
  },
  {
    id: 3,
    comment:
      "Отличная задумка и есть потенциал данной\n" +
      "платформы. Платформа действительно интересная\n" +
      "и вериться в то, что ее еще ждет успех",
    logo: "logo",
    title: "SKY logistics",
  },
  {
    id: 4,
    comment:
      "Chat.im - это удобный чат-сервис для службы поддержки на базе искусственного интеллекта.",
    logo: "logo2",
    title: "Scipher medicine ",
  },
];
</script>
