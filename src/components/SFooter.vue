<template>
  <div class="bg-[#171A20]">
    <div class="container pb-4 ms:pb-6 dm:pb-[144px] px-8">
      <div
        class="grid grid-cols-1 ms:grid-cols-3 dm:grid-cols-5 gap-3 ms:gap-10"
      >
        <div class="ms:col-span-3 dm:col-span-2">
          <h2
            class="text-[#FF5C00] max-w-[210px] font-bold uppercase text-xl ms:text-[28px] leading-7 ms:leading-[33.843px] tracking-[0.846px]"
          >
            ПОДДЕРЖКА И ОБНОВЛЕНИЕ
          </h2>
          <p
            class="mt-2 ms:mt-7 text-[#8E8E8E] leading-[16.598px] text-xs pr-5"
          >
            Мы готовы помочь и оказать поддержку каждому клиенту в установке и
            использовании Chat.im. Наш центр поддержки работает только по будням
            с понедельника по пятницу. Пожалуйста, учитывайте, что мы можем не
            ответить вам в выходные.
          </p>
        </div>
        <div class="flex flex-col gap-2 ms:gap-3">
          <a
            href="https://mail.google.com/mail/u/1/#inbox"
            class="flex items-center gap-3 cursor-pointer group"
          >
            <div
              class="icon-emailsvg text-lg transition duration-300 group-hover:!text-[#8E9DCC]"
            ></div>
            <p
              class="leading-[22.131px] text-sm transition duration-300 group-hover:text-[#8E9DCC]"
            >
              advice_ai@bot.com
            </p>
          </a>
          <a
            href="https://t.me/Botirov_Valisher"
            target="_blank"
            class="flex items-center gap-3 cursor-pointer group"
          >
            <div
              class="icon-telegramsvg text-lg transition duration-300 group-hover:!text-[#8E9DCC]"
            ></div>
            <p
              class="leading-[22.131px] text-sm transition duration-300 group-hover:text-[#8E9DCC]"
            >
              @adviceai_bot
            </p>
          </a>
          <a
            href="tel:+998945360998"
            class="flex items-center gap-3 cursor-pointer group"
          >
            <div
              class="icon-phonesvg text-lg transition duration-300 group-hover:!text-[#8E9DCC]"
            ></div>
            <p
              class="leading-[22.131px] text-sm transition duration-300 group-hover:text-[#8E9DCC]"
            >
              + 998 94 536 09 98
            </p>
          </a>
          <a
            href="https://www.instagram.com/valisher_botirov"
            class="flex items-center gap-3 cursor-pointer group"
          >
            <div
              class="icon-facebook-brandssvg text-lg transition duration-300 group-hover:!text-[#8E9DCC]"
            ></div>
            <p
              class="leading-[22.131px] text-sm transition duration-300 group-hover:text-[#8E9DCC]"
            >
              advice_ai
            </p>
          </a>
        </div>
        <div class="flex flex-col gap-2 ms:gap-4">
          <p
            class="leading-[22.574px] tracking-[0.269px] text-sm cursor-pointer transition duration-300 hover:text-[#8E9DCC]"
          >
            {{ $t("blog") }}
          </p>
          <p
            class="leading-[22.574px] tracking-[0.269px] text-sm cursor-pointer transition duration-300 hover:text-[#8E9DCC]"
          >
            FAQ
          </p>
          <p
            class="leading-[22.574px] tracking-[0.269px] text-sm cursor-pointer transition duration-300 hover:text-[#8E9DCC]"
          >
            {{ $t("about") }}
          </p>
        </div>
        <div class="flex flex-col gap-2 ms:gap-4">
          <router-link
            to="/terms_use"
            class="leading-[22.574px] tracking-[0.269px] text-sm cursor-pointer transition duration-300 hover:text-[#8E9DCC]"
            >{{ $t("terms_of_use") }}</router-link
          >
          <router-link
            to="/privacy_police"
            class="leading-[22.574px] tracking-[0.269px] text-sm cursor-pointer transition duration-300 hover:text-[#8E9DCC]"
            >{{ $t("privacy_police") }}</router-link
          >
        </div>
      </div>
      <div
        class="flex items-center flex-col gap-4 ms:gap-0 ms:flex-row justify-between mt-10 ms:mt-[60px]"
      >
        <SButton variant="black" class="w-full ms:w-auto">Напишите нам</SButton>
        <div class="w-full ms:w-auto">
          <div class="flex justify-between ms:items-center gap-5">
            <p>Мы в соц. сетях:</p>
            <div class="flex items-center gap-5">
              <a
                href="https://t.me/Botirov_Valisher"
                target="_blank"
                class="icon-telegramsvg text-2xl cursor-pointer transition duration-300 hover:rotate-[360deg]"
              ></a>
              <a
                href="https://www.linkedin.com/in/valisher-botirov/"
                target="_blank"
                class="icon-facebook-brandssvg text-2xl cursor-pointer transition duration-300 hover:rotate-[360deg]"
              ></a>
              <a
                href="https://www.instagram.com/valisher_botirov"
                target="_blank"
                class="icon-instagram text-2xl cursor-pointer transition duration-300 hover:rotate-[360deg]"
              ></a>
            </div>
          </div>
          <p
            class="text-[#66676B] leading-[11.066px] text-[10px] text-center ms:text-left mt-3 ms:mt-2"
          >
            © 2024 Advice AI. All rights reserved.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import SButton from "@/components/SButton.vue";
</script>
