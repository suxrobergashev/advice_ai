<template>
  <div>
    <div class="bg-[#EAEAFE] py-6">
      <div class="container relative z-[20]">
        <SideBar
          :is-open="openSidebar"
          @closeSidebar="(e) => (openSidebar = e)"
        />

        <div class="flex justify-between items-center">
          <div
            class="block lg:hidden flex-shrink-0 cursor-pointer"
            @click="openSidebar = true"
          >
            <i
              class="fa-solid fa-bars text-[20px] text-black ms:text-[25px]"
            ></i>
          </div>

          <div class="items-center gap-5 cursor-pointer hidden lg:flex">
            <a
              v-for="(item, index) in link"
              :key="index"
              :href="`#${item.link}`"
              class="font-medium text-[15px] leading-[26px] transition duration-300 text-[#141920] hover:text-[#0469FF] relative navItem"
            >
              {{ $t(`${item.title}`) }}
            </a>
          </div>

          <div class="flex flex-shrink-0 items-center gap-3">
            <div class="flex">
              <div v-for="item in langs" :key="item">
                <div
                  class="flex justify-center items-center px-2 w-8 h-8 rounded-[50%] text-[#141920] text-xs cursor-pointer font-[700]"
                  :class="activeLang.value == item.value ? 'bg-white' : ''"
                  @click="changeLanguage(item)"
                >
                  {{ item.label }}
                </div>
              </div>
            </div>
            <SButton
              class="hidden md:block text-center"
              @click="router.push('/sign-up')"
              >{{ $t("connect") }}
            </SButton>
          </div>
        </div>
      </div>
    </div>
    <SModal :is-open="openModal" @closeModal="(e) => (openModal = e)" />
  </div>
</template>

<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import { onMounted, ref } from "vue";
import { useI18n } from "vue-i18n";
import SideBar from "@/components/SideBar.vue";
import SModal from "@/components/modal/SModal.vue";
import { useRouter } from "vue-router";

const { locale } = useI18n();
const router = useRouter();
const openSidebar = ref(false);
const openModal = ref(false);

type TLink = { link: string; title: string }[];
const link: TLink = [
  {
    link: "about",
    title: "about",
  },
  {
    link: "opportunity",
    title: "main",
  },
  {
    link: "tariff",
    title: "tariff",
  },
  {
    link: "comment",
    title: "help",
  },
  {
    link: "download",
    title: "download",
  },
  {
    link: "faq",
    title: "faq",
  },
  {
    link: "faq",
    title: "contact",
  },
];

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
