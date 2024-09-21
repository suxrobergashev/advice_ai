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
            src="@/assets/images/advice1.webp"
            alt="images"
            class="w-[220px] ms:w-[280px] sm:w-[308px] h-[130px] ms:h-[160px] sm:h-[180px] object-cover rounded-[13px]"
          />
          <img
            src="@/assets/images/advice2.jpg"
            alt="images"
            class="w-[150px] sm:w-[216px] h-[210px] ms:h-[280px] sm:h-[330px] object-cover rounded-[11px] translate-x-[-80px]"
          />
        </div>
        <OppornutunityInfo
          desc="Advice AI yordamida siz iqtidorlaringizni aniqlab olish va o'zingizga munosib mutahassislikni  bilib olishingiz mumkin!"
          title="AI yordamida iqtidorni aniqlash"
        />
      </div>
      <div
        class="border-t border-[#DEDED8] flex flex-col-reverse lg:grid gap-6 sm:gap-[50px] lg:gap-[90px] lg:grid-cols-2 items-center pt-6 sm:pt-10 mt-8 sm:mt-[60px]"
      >
        <OppornutunityInfo
          desc="Sun'iy intellektga asoslangan maslahatchi muloqot davomida sizning iqtidoringizni aniqlab, iqtidoringizga munosib kasblarga yo'naltiradi"
          title="Iqtidoringizga munosib kasbga yo'naltirish"
        />
        <div class="">
          <img
            src="@/assets/images/advice3.jpg"
            alt="images"
            class="rounded-[20px] w-full h-[200px] ms:h-[300px] object-cover sm:h-[400px] lg:max-h-[470px] lg:h-full"
          />
        </div>
      </div>
      <div
        class="border-t border-[#DEDED8] grid grid-cols-1 gap-6 sm:gap-10 lg:gap-0 lg:grid-cols-2 items-center pt-6 sm:pt-10 mt-8 sm:mt-[60px]"
      >
        <div class="flex justify-center sm:justify-start mt-10 translate-x-10">
          <div class="">
            <img
              src="@/assets/images/advice4.jpg"
              alt="images"
              class="rounded-[20px] w-full h-[200px] ms:h-[300px] object-cover sm:h-[400px] lg:max-h-[470px] lg:h-full"
            />
          </div>
        </div>
        <OppornutunityInfo
          desc="Advice AI iqtidoringizga mos kasbni o'rganishingiz uchun O'zbekiston va chet el universetutlarini yokida mahalliy kasbga yo'naltirilga o'quv markazlarni taqdim etadi"
          title="Kasb egallashingiz uchun universetut va o'quv markazlar ro'yxati"
        />
      </div>
      <div
        class="border-t border-[#DEDED8] flex flex-col-reverse lg:grid gap-10 sm:gap-[100px] lg:gap-[90px] lg:grid-cols-2 items-center pt-6 sm:pt-16 mt-8 sm:mt-[60px]"
      >
        <OppornutunityInfo
          desc="Advice AI iqtidoringizga mos kasbni o'rganishingiz uchun mahalliy va global bozordagi top online kurslarni taqdim etadi"
          title="Mutahassislik bo'yicha mahalliy va global online kurslar"
        />
        <div
          class="flex lg:translate-y-[-29px] translate-x-[20px] sm:translate-x-[0]"
        >
          <img
            src="@/assets/images/advice3.jpg"
            alt="images"
            class="rounded-[20px] w-[180px] ms:w-[200px] sm:!w-[380px] object-cover h-[220px] sm:h-[270px]"
          />
          <img
            src="@/assets/images/advice5.jpg"
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
            src="@/assets/images/advice1.webp"
            alt="images"
            class="rounded-[20px] w-full h-[200px] ms:h-[300px] object-cover sm:h-[400px] lg:max-h-[470px] lg:h-full"
          />
        </div>
        <OppornutunityInfo
          desc="Advice AI sizga o'z mutahasisligingizni yanada mustahkamlsh uchun online testlarni taqdim etadi va tekshirib o'z xulosasini aytadi"
          title="Sohaviy bilimlarni mustahkamlash uchun online testlar"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import OppornutunityInfo from "@/components/card/OppornutunityInfo.vue";
</script>
