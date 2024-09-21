<template>
  <Teleport to="body">
    <div
      :class="isOpen ? 'translate-x-0' : '-translate-x-full'"
      class="fixed w-full h-[100vh] inset-y-0 duration-300 right-0 bg-black z-[9999] flex items-center justify-center"
    >
      <i
        @click="emit('closeSidebar', false)"
        class="fa-sharp fa-solid fa-xmark text-white text-2xl top-10 right-10 absolute"
      ></i>
      <div class="text-center gap-6 text-lg text-white ">
        <div v-for="item in link" :key="item">
          <a
            :href="`#${item.link}`"
            @click="emit('closeSidebar', false)"
            class="font-medium text-white mt-6 inline-block leading-[16.94px] transition duration-300 hover:text-[#0469FF] hover:border-[#0469FF] border-b pb-2"
          >
            {{ $t(`${item.title}`) }}
          </a>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
interface Props {
  isOpen: boolean;
}

defineProps<Props>();

const emit = defineEmits(["closeSidebar"]);

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
</script>
