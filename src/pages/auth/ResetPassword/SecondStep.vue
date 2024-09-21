<template>
  <div class="px-6 sm:px-[100px] h-[100vh] flex flex-col justify-center">
    <div>
      <div class="text-[#49549D]">
        <p class="text-[#49549D] text-[32px] font-bold">
          Проверьте свою электронную почту
        </p>
        <p
          class="text-[#312ECB] ms:mt-1 text-sm sm:text-base leading-5 sm:leading-[22px]"
        >
          Мы отправили электронное письмо с информацией для сброса пароля на
          адрес n***e@e***e.com.
        </p>
      </div>

      <div class="mt-10 sm:mt-[100px]">
        <p
          class="text-[#312ECB] ms:mt-1 text-sm sm:text-base leading-5 sm:leading-[22px]"
        >
          Не получили письмо? Проверьте папку со спамом или рекламными акциями.
        </p>
        <SButton class="mt-5 sm:mt-[30px] rounded-[5px]" @click="send()"
          >Повторно отправить электронное письмо</SButton
        >
        <router-link to="/login" class="mt-5 sm:mt-[30px] inline-block w-full">
          <SButton
            variant="white"
            class="rounded-[5px] text-[#49549D] border border-[#49549D]"
            >Вернуться на страницу авторизации</SButton
          >
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import SButton from "@/components/SButton.vue";
import { useRouter } from "vue-router";

const router = useRouter();

function send() {
  // router.push('/reset/step2')
  console.log("repeat");
}
</script>
