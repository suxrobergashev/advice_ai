<template>
  <div class="container">
    <div
      class="bg-white rounded-[30px] sm:rounded-[36px] px-6 sm:px-16 pt-6 md:pt-11 pb-6 sm:pb-8 md:pb-14 mt-6 sm:mt-10 md:!mt-[60px]"
    >
      <p
        class="text-[#BAE06A] font-bold text-[34px] sm:text-[40px] md:text-[58px] leading-10 sm:leading-[70px]"
      >
        {{ $t("opportunity") }}
      </p>
      <div
        class="border-t border-[#DEDED8] grid grid-cols-1 gap-6 sm:gap-10 lg:gap-0 lg:grid-cols-2 items-center pt-10 mt-4 sm:mt-8"
      >
        <div class="relative flex items-center">
          <img
            src="@/assets/images/fake-images/fake1.jpg"
            alt="images"
            class="w-[220px] ms:w-[280px] sm:w-[308px] h-[130px] ms:h-[160px] sm:h-[180px] object-cover rounded-[13px]"
          />
          <img
            src="@/assets/images/fake-images/fake2.jpg"
            alt="images"
            class="w-[150px] sm:w-[216px] h-[210px] ms:h-[280px] sm:h-[330px] object-cover rounded-[11px] translate-x-[-80px]"
          />
        </div>
        <OppornutunityInfo
          desc="Создавайте качественные статьи, документы, блоги,
рекламные текста, письма и другие виды контента."
          title="Генерация текстов и документов"
        />
      </div>
      <div
        class="border-t border-[#DEDED8] flex flex-col-reverse lg:grid gap-6 sm:gap-[50px] lg:gap-[90px] lg:grid-cols-2 items-center pt-6 sm:pt-10 mt-8 sm:mt-[60px]"
      >
        <OppornutunityInfo
          desc="Изучайте английский язык, корректируйте грамматику, готовьтесь к тестам и улучшайте знание языка."
          title="Помощь в изучении английского языка"
        />
        <div class="">
          <img
            src="@/assets/images/fake-images/fake4.jpg"
            alt="images"
            class="rounded-[20px] w-full h-[200px] ms:h-[300px] object-cover sm:h-[400px] lg:max-h-[470px] lg:h-full"
          />
        </div>
      </div>
      <div
        class="border-t border-[#DEDED8] grid grid-cols-1 gap-6 sm:gap-10 lg:gap-0 lg:grid-cols-2 items-center pt-6 sm:pt-10 mt-8 sm:mt-[60px]"
      >
        <div class="flex justify-center sm:justify-start mt-10 translate-x-10">
          <img
            src="@/assets/images/fake-images/fake6.jpg"
            alt="images"
            class="rounded-[20px] w-[180px] ms:w-[200px] sm:!w-[242px] object-cover h-[220px] sm:h-[279px]"
          />
          <img
            src="@/assets/images/fake-images/fake5.jpg"
            alt="images"
            class="rounded-[20px] w-[180px] ms:w-[200px] sm:!w-[242px] object-cover h-[220px] sm:!h-[279px] -translate-y-8 ms:-translate-y-10 -translate-x-20"
          />
        </div>
        <OppornutunityInfo
          desc="Saiora позволяет писать код на разных языках
программирования, создавать тесты для кода
находить ошибки, чтобы улучшить вашу работу."
          title="Помощь в программировании"
        />
      </div>
      <div
        class="border-t border-[#DEDED8] flex flex-col-reverse lg:grid gap-10 sm:gap-[100px] lg:gap-[90px] lg:grid-cols-2 items-center pt-6 sm:pt-16 mt-8 sm:mt-[60px]"
      >
        <OppornutunityInfo
          desc="Saiora поможет вам провести анализ рынка,
разработать бизнес-стратегию, создать
маркетинговые стратегии, составить финансовый
план, управлять проектами, набрать команду,
оптимизировать бизнес-процессы и многое другое
для развития вашего бизнеса.."
          title="Помощь с ведением и
развитием бизнеса"
        />
        <div
          class="flex lg:translate-y-[-29px] translate-x-[20px] sm:translate-x-[0]"
        >
          <img
            src="@/assets/images/fake-images/fake1.jpg"
            alt="images"
            class="rounded-[20px] w-[180px] ms:w-[200px] sm:!w-[380px] object-cover h-[220px] sm:h-[270px]"
          />
          <img
            src="@/assets/images/fake-images/fake7.jpg"
            alt="images"
            class="rounded-[20px] w-[180px] ms:w-[200px] sm:!w-[380px] object-cover h-[220px] sm:!h-[270px] translate-y-[20px] sm:translate-y-[69px] translate-x-[-100px] sm:translate-x-[-300px]"
          />
        </div>
      </div>
      <div
        class="border-y border-[#DEDED8] grid gap-6 sm:gap-[50px] lg:gap-[90px] lg:grid-cols-2 items-center pt-6 sm:pt-10 pb-6 sm:pb-10 mt-8 sm:mt-[80px]"
      >
        <div class="">
          <img
            src="@/assets/images/fake-images/fake4.jpg"
            alt="images"
            class="rounded-[20px] w-full h-[200px] ms:h-[300px] object-cover sm:h-[400px] lg:max-h-[470px] lg:h-full"
          />
        </div>
        <OppornutunityInfo
          desc="Изучайте английский язык, корректируйте грамматику, готовьтесь к тестам и улучшайте знание языка."
          title="Помощь в изучении английского языка"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import OppornutunityInfo from "@/components/card/OppornutunityInfo.vue";
</script>
