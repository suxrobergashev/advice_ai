<template>
  <div
    class="cursor-pointer select-none flex justify-center text-sm ms:text-base items-center py-[10px] px-[18px] ms:px-4 rounded-xl font-medium transition duration-300 active:scale-[0.95]"
    :class="[customClass, buttonStyle]"
  >
    <slot></slot>
    <slot name="pre"></slot>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

interface Props {
  customClass?: string;
  variant: string;
}

const props = withDefaults(defineProps<Props>(), {
  variant: "blue",
});

// eslint-disable-next-line vue/return-in-computed-property
const buttonStyle = computed(() => {
  switch (props.variant) {
    case "blue":
      return "bg-[#49549D] font-[800] hover:bg-[#1877F2] hover:text-white transition duration-300 text-white";
    case "white":
      return "bg-white font-bold text-base sm:text-lg leading-5 text-[#363636] transition duration-300 hover:bg-[#F4F4F3]";
    case "gray":
      return "bg-[#BAE06A] text-[#141920] font-[800] text-base sm:text-lg sm:leading-[30.525px] transition duration-300 hover:bg-[#21AE2E]";
    case "light":
      return "bg-[#8E9DCC] hover:bg-[#49549D] font-bold";
    case "black":
      return "bg-[#2E3036] rounded-[3px] border transition duration-300 border-[#ffffff26] hover:bg-[#66676B]";
  }
});
</script>
