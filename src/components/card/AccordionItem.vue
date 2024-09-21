<script setup lang="ts">
import { ref } from "vue";

interface Props {
  id: number;
  index: number;
  question?: string;
  answer?: string;
}

defineProps<Props>();

const isOpen = ref(false);
function open() {
  isOpen.value = !isOpen.value;
}
</script>

<template>
  <div
    class="w-full overflow-hidden text-black rounded-[10px] px-4 bg-[#F4F4F3]"
  >
    <input type="checkbox" :id="id" class="!absolute !opacity-0 !z-[-1]" />
    <label
      @click="open"
      class="tab-label w-full cursor-pointer flex justify-between gap-3 py-3"
      :for="id"
    >
      <p class="font-semibold text-black text-sm sm:text-base max-w-[600px]">
        {{ question }}
      </p>
      <div>
        <i
          class="fa-solid fa-chevron-down text-black transition duration-300"
          :class="isOpen ? 'rotate-[180deg]' : 'rotate-0'"
        ></i>
      </div>
    </label>
    <div
      class="tab-content max-h-0 border-transparent transition duration-300 ease-linear text-[#999] leading-[135.023%] text-sm"
    >
      {{ answer }}
    </div>
  </div>
</template>

<style scoped>
.tab-label {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.tab-content {
  max-height: 0;
  transition: all 0.3s;
  border: transparent;
  backdrop-filter: blur(10px);
}

input:checked ~ .tab-content {
  max-height: 100vh;
  padding-bottom: 4px;
}
</style>
