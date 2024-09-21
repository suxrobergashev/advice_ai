<template>
  <div class="px-10 sm:px-[100px] h-[100vh] flex flex-col justify-center">
    <div v-if="!isSuccess">
    <div class="text-[#49549D]">
      <p class="text-[#49549D] text-[32px] font-bold">Сброс пароля</p>
      <p class="text-[#312ECB] ms:mt-1">Выберите новый пароль для своей учетной записи</p>
    </div>

    <div class="mt-5 sm:mt-12">
      <SInput v-model="form.password" type="password" placeholder="Ваш новый пароль" class="mt-4"/>
      <SInput v-model="form.confirmPassword" type="password" placeholder="Подтвердите новый парольоль" class="mt-4"/>
      <SButton class="mt-5 sm:mt-[30px] rounded-[5px]" @click="resetPassword()">Сброс пароля</SButton>
      <router-link to="/login" class="mt-5 sm:mt-[30px] inline-block w-full">
        <SButton variant="white" class="rounded-[5px] text-[#49549D] border border-[#49549D]">Вернуться на страницу авторизации</SButton>
      </router-link>
    </div>
    </div>
<!--    success mode-->
    <div v-else class="flex flex-col items-center ">
      <svg xmlns="http://www.w3.org/2000/svg" width="100" height="101" viewBox="0 0 100 101" fill="none">
        <path d="M37.5 50.5L45.8333 58.8333L62.5 42.1667M87.5 50.5C87.5 71.2107 70.7107 88 50 88C29.2893 88 12.5 71.2107 12.5 50.5C12.5 29.7893 29.2893 13 50 13C70.7107 13 87.5 29.7893 87.5 50.5Z" stroke="#34A853" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="mt-4 font-semibold text-[#49549D] text-xl">
        Пароль успешно сброшен
      </div>
      <router-link to="/login" class="mt-8 inline-block w-full">
        <SButton class="rounded-[5px] ">Авторизоваться</SButton>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import SInput from "@/components/form/SInput.vue";
import {reactive, ref} from "vue";
import SButton from "@/components/SButton.vue";

const isSuccess = ref(false)

const form = reactive({
  password:"",
  confirmPassword:""
})

function resetPassword(){
  isSuccess.value = true
}
</script>

