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
        <div class="" v-for="item in 4" :key="item">
          <AboutCard />
        </div>
      </div>
      <div
        class="mt-6 sm:mt-10 md:mt-[50px] text-[#5E6282] font-medium text-base sm:text-lg md:text-xl leading-[22px] sm:leading-6 md:leading-[26px] text-center md:px-[54px]"
      >
        Lorem Ipsum is simply dummy text of the printing and typesetting
        industry. Lorem Ipsum has been the industry's standard dummy text ever
        since the 1500s, when an unknown printer took a galley of type and
        scrambled it to make a type specimen book.
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import AboutCard from "@/components/card/AboutCard.vue";
</script>
