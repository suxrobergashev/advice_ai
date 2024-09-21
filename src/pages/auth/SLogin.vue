<template>
  <div class="px-10 sm:px-[100px] h-[100vh] flex flex-col justify-center">
    <div class="text-[#49549D]">
      <p class="text-[#49549D] text-[32px] font-bold">Xush kelibsiz</p>
      <p class="text-[#312ECB] ms:mt-1">
        Hisobingiz yo'qmi?
        <router-link to="/sign-up" class="font-medium hover:text-[#49549D]"
          >Ro'yxatdan o'tish</router-link
        >
      </p>
    </div>

    <div class="mt-5 sm:mt-12">
      <SInput v-model="form.email" placeholder="Phone number" class="mt-4" />
      <SInput
        v-model="form.password"
        type="password"
        placeholder="Parol"
        class="mt-4"
      />
      <div class="mt-5 flex justify-end">
        <router-link
          to="/forgot"
          class="text-[#49549D] text-sm hover:text-blue-800"
          >Parolni unutdingizmi?</router-link
        >
      </div>
      <SButton class="mt-5 sm:mt-[30px] rounded-[5px]">Kirish</SButton>

      <div class="mt-5 sm:mt-[30px] flex items-center gap-3">
        <div class="h-[1px] bg-[#04030866] w-full"></div>
        <p class="text-[#49549D]">yoki</p>
        <div class="h-[1px] bg-[#04030866] w-full"></div>
      </div>
      <div class="mt-5 sm:mt-[30px]">
        <SButton variant="white" class="rounded-[5px] border !border-[#49549D]">
          <div class="flex items-center gap-2">
            <GoogleSVG />
            <p class="font-semibold text-base text-[#49549D]">
              Google orqali kirish
            </p>
          </div>
        </SButton>
        <SButton
          variant="white"
          class="mt-3 ms:mt-5 rounded-[5px] border !border-[#49549D]"
        >
          <div class="flex items-center gap-2">
            <AppleSVG />
            <p class="font-semibold text-base text-[#49549D]">
              Apple orqali kirish
            </p>
          </div>
          </SButton
        >
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SInput from "@/components/form/SInput.vue";
import { reactive } from "vue";
import SButton from "@/components/SButton.vue";
import GoogleSVG from "@/assets/icon/GoogleSVG.vue";
import AppleSVG from "@/assets/icon/AppleSVG.vue";

const form = reactive({
  email: "",
  password: "",
});
</script>
