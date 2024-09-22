<template>
  <div
    class="container pt-6 sm:pt-10 md:pt-[60px] flex flex-col dm:grid grid-cols-2 gap-4"
  >
    <div
      class="bg-[#49549D] rounded-[30px] sm:rounded-[40px] pt-10 sm:pt-[55px] pb-[30px] px-5 sm:px-8 lg:px-16"
    >
      <h2 class="font-bold text-[40px] sm:text-[50px] text-[#BAE06A]">
        Advice AI
      </h2>
      <div
        class="mt-[20px] font-medium leading-[46px] sm:leading-[55px] lg:leading-[70px] text-[40px] sm:text-[50px] lg:text-[58px]"
      >
        Iqtidoringizni biz bilan oson aniqlang
      </div>
      <p class="mt-7 text-lg font-medium leading-7">
        Advice AI foydalanuvchilariga o‘z iqtidorlarini sun’iy intellekt ustiga
        qurilgan tizim orqali oson aniqlashga va ularni munosib kasbga
        yo‘naltirishga xizmat qiladi
      </p>
      <div class="mt-8 flex gap-4">
        <a
          href="https://play.google.com/store/apps?hl=ru&gl=US"
          target="_blank"
        >
          <img src="@/assets/icon/google.svg" alt="google play" />
        </a>
        <a href="https://www.apple.com/app-store/" target="_blank">
          <img src="@/assets/icon/apple.svg" alt="Apple" />
        </a>
      </div>
    </div>
    <div class="h-full">
      <div
        class="bg-[#333131] rounded-[30px] sm:rounded-[40px] px-5 sm:px-8 py-6"
      >
        <p class="text-2xl sm:text-[30px] font-[700] leading-8">
          Bizni ijtimoiy tarmoqlarda kuzatib boring !
        </p>
        <div class="flex gap-6 mt-4">
          <a
            v-for="(item, index) in social"
            :key="index"
            :href="item.link"
            target="_blank"
          >
            <img
              :src="getImageUrl(item.icon)"
              alt="images"
              class="w-12 h-12 sm:w-16 sm:h-16"
            />
          </a>
        </div>
      </div>
      <div
        class="mt-4 sm:mt-[26px] rounded-[30px] sm:rounded-[40px] px-6 bg-image py-5 sm:py-0 sm:h-[300px] dm:h-[354px] flex items-center"
      >
        <div class="ms:max-w-[300px]">
          <p
            class="text-[#363636] text-2xl text-center sm:text-[26px] leading-6 sm:leading-8 font-bold mb-4 sm:mb-3"
          >
            Bizni xoziroq sinab ko'rishingiz mumkin
          </p>
          <div class="flex justify-center">
            <SButton variant="white" @click="$router.push('/advice')"
              >Sinab ko'rish</SButton
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SButton from "@/components/SButton.vue";

function getImageUrl(name: string) {
  return new URL(`../assets/icon/${name}.svg`, import.meta.url).href;
}

const social: { icon: string; link: string }[] = [
  {
    link: "https://t.me/Botirov_Valisher",
    icon: "telegram",
  },
  {
    link: "https://t.me/Botirov_Valisher",
    icon: "whatsapp",
  },
  {
    link: "https://t.me/Botirov_Valisher",
    icon: "mail",
  },
  {
    link: "https://t.me/Botirov_Valisher",
    icon: "facebook",
  },
  {
    link: "https://t.me/Botirov_Valisher",
    icon: "instagram",
  },
];
</script>

<style scoped>
.bg-image {
  background: url("@/assets/images/bannerBg.png") no-repeat right,
    linear-gradient(0deg, #d9dbf1 0%, #d9dbf1 100%);
  background-size: contain;
  box-shadow: -7px 7px 33.6px 0px rgba(16, 33, 194, 0.25) inset;
}

@media (max-width: 500px) {
  .bg-image {
    background: none, linear-gradient(0deg, #d9dbf1 0%, #d9dbf1 100%);
  }
}
</style>
