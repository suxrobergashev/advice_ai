<script setup lang="ts"></script>

<template>
  <div class="grid grid-cols-1 md:grid-cols-2 h-full overflow-hidden min-h-[100vh]">
    <div
      class="hidden md:flex bg-[#49549D] p-10 dm:p-[100px]  flex-col justify-between auth-section"
    >
      <div class="flex">
        <img src="@/assets/icon/logo.svg" alt="logo" />
      </div>
      <div>
        <p class="font-bold text-[40px]">Chat.im</p>
        <p class="mt-3 dm:mt-5 text-2xl">Платформа для связи с клиентами</p>
      </div>
    </div>
    <div>
      <router-view />
    </div>
  </div>
</template>

<style scoped>
.auth-section {
  width: 100%;
  height: 100%;
  background-image: url("src/assets/images/auth-bg.png");
  background-size: cover;
  background-position: center;
}
</style>
