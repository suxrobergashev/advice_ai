<template>
  <div>
    <div class="bg-[#dbd9d6cc] py-6">
      <div class="container relative z-[20]">
        <div class="flex justify-between items-center">
          <router-link to="/">
            <!--            <img src="@/assets/icon/logo_dark.svg" alt="logo" />-->
            <p class="font-bold text-[38px] !text-gray-700">Advice AI</p>

          </router-link>

          <div class="flex flex-shrink-0 items-center gap-3">
            <div class="flex">
              <div v-for="item in langs" :key="item.label">
                <div
                  class="flex justify-center items-center px-2 w-8 h-8 rounded-[50%] text-[#141920] text-xs cursor-pointer font-[700]"
                  :class="activeLang.value == item.value ? 'bg-white' : ''"
                  @click="changeLanguage(item)"
                >
                  {{ item.label }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import { onMounted, ref } from "vue";
import { useI18n } from "vue-i18n";
import SideBar from "@/components/SideBar.vue";
import SModal from "@/components/modal/SModal.vue";

const { locale } = useI18n();

const langs = [
  {
    value: "uz",
    label: "UZ",
  },
  {
    value: "ru",
    label: "RU",
  },
];

const activeLang = ref({
  value: "uz",
  label: "UZ",
});

function changeLanguage(item: { value: string; label: string }) {
  localStorage.setItem("locale", item.value);
  localStorage.setItem("langLabel", item.label);
  if (activeLang.value.value !== item.value) {
    window.location.reload();
  }
}

function getImageUrl(name: string) {
  return new URL(`../assets/icon/${name}.svg`, import.meta.url).href;
}

onMounted(() => {
  locale.value = localStorage.getItem("locale") || "uz";
  activeLang.value.value = locale.value;
  activeLang.value.label = localStorage.getItem("langLabel") || "O'zb";
});
</script>
<style scoped>
.navItem::after {
  position: absolute;
  content: "";
  bottom: -6px;
  height: 2px;
  width: 100%;
  left: 0;
  top: 22px;
  background: #141920;
  border-radius: 2px;
  transition: 0.2s;
  transition-timing-function: ease-in-out;
  transform: scale(0);
}
.navItem:hover::after {
  transform: scale(110%);
}
</style>
