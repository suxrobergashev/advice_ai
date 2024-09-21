<template>
  <div class="px-10 sm:px-[100px] h-[100vh] flex flex-col justify-center">
    <div class="text-[#49549D]">
      <p class="text-[#49549D] text-[32px] font-bold">Hisob yaratish</p>
      <p class="text-[#312ECB] ms:mt-1">
        Hisobingiz mavjudmi?
        <router-link to="/login" class="font-medium hover:text-[#49549D]"
          >Kirish</router-link
        >
      </p>
    </div>
    <div class="mt-5 sm:mt-10">
      <div class="flex flex-col ms:flex-row gap-4 ms:gap-[30px]">
        <SInput v-model="form.name" placeholder="Ism" />
        <SInput v-model="form.surname" placeholder="Familiya" />
      </div>
      <SInput v-model="form.email" placeholder="Telefon raqam" class="mt-4" />
      <SInput
        v-model="form.password"
        type="password"
        placeholder="Parol"
        class="mt-4"
      />
      <div class="flex items-center gap-3 mt-4">
        <input type="checkbox" class="w-4 h-4" v-model="form.isCheck" />
        <p class="text-[#312ECB] text-xs sm:text-sm ms:max-w-[360px]">
          <router-link
            to="/privacy_police"
            class="hover:text-[#49549D] hover:!font-medium"
          >
            Advice AI ning Foydalanish shartlari va Maxfiylik siyosatiga rozilik
            bildiraman
          </router-link>
        </p>
      </div>
      <SButton class="mt-5 sm:mt-[30px] rounded-[5px]">Hisob yaratish</SButton>
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
        </SButton>
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
  name: "",
  surname: "",
  email: "",
  password: "",
  isCheck: false,
});
</script>
