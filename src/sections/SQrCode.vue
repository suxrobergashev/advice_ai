<template>
  <div class="container pb-6 dm:pb-0 dm:translate-y-20 pt-0 dm:pt-[162px]">
    <div
      class="mt-6 ms:mt-[40px] rounded-[20px] bg-[#49549D] flex relative px-6 sm:px-12 pb-5 sm:pb-[56px]"
    >
      <div class="   ">
        <h2
          class="text-2xl leading-[30px] pt-3 ms:pt-[16.5px] flex flex-wrap ms:text-[43px] ms:leading-[55px] lg:!text-[53.5px] sm:max-w-[530px] lg:leading-[66px] lg:pt-[26.5px] font-[800]"
        >
          Скачать мобильное приложение Chat.im
        </h2>
        <div
          class="flex items-center pt-[10px] lg:pt-[36px] gap-4 ms:gap-[25px]"
        >
          <div class="flex-shrink-0">
            <img
              class="sx:w-[70px] h-[70px] lg:!w-[112px] lg:h-[112px]"
              src="@/assets/images/qr_kod.png "
              alt="qr code"
            />
          </div>
          <div class="lg:max-w-[376px]">
            <p
              class="text-base ms:text-lg lg:text-[25px] font-medium leading-5 ms:leading-7 lg:leading-[32.2px]"
            >
              Наведите камеру и скачайте приложение Chat.im
            </p>

            <div class="flex gap-4 mt-2">
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
        </div>
      </div>

      <div class="hidden dm:block">
        <img
          class="absolute right-[254.7px] pt-[10px] bottom-0"
          src="@/assets/images/phone_white.png"
          alt="images"
        />
        <img
          class="absolute right-[45.7px] bottom-0"
          src="@/assets/images/phone_blue.png"
          alt="images"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
