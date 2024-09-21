<template>
  <div class="px-6 sm:px-[100px] h-[100vh] flex flex-col justify-center">
    <div >
      <div class="text-[#49549D]">
        <p class="text-[#49549D] text-[32px] font-bold">Забыли пароль</p>
        <p class="text-[#312ECB] ms:mt-1 text-sm sm:text-base leading-5 sm:leading-[22px]">Введите адрес электронной почты, который вы использовали для создания учетной записи, чтобы мы могли отправить вам инструкции по сбросу пароля.</p>
      </div>

      <div class="mt-10 sm:mt-[100px]">
        <SInput v-model="form.email" type="email" placeholder="Email" class="mt-4"/>
        <SButton class="mt-5 sm:mt-[30px] rounded-[5px]" @click="send()">Отправить</SButton>
        <router-link to="/login" class="mt-5 sm:mt-[30px] inline-block w-full">
          <SButton variant="white" class="rounded-[5px] text-[#49549D] border border-[#49549D]">Вернуться на страницу авторизации</SButton>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import SInput from "@/components/form/SInput.vue";
import {reactive, ref} from "vue";
import SButton from "@/components/SButton.vue";
import {useRouter} from "vue-router";

const router = useRouter()
const form = reactive({
  email:"",
})

function send(){
  router.push('/forgot/step1')
}
</script>

