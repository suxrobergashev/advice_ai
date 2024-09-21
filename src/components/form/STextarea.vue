<template>
  <div class="block w-full relative">
    <label
      v-if="label"
      :for="`a-input-${id}`"
      class="flex sm:items-end items-start justify-between mb-1 sm:mb-2 flex-col gap-2 sm:flex-row"
    >
      <span class="text-sm sm:text-base leading-130 text-white font-normal">
        {{ $t(label) }}
      </span>
      <transition name="fade">
        <slot name="error">
          <span
            v-if="error && errorLabel"
            class="text-xs font-medium leading-4 text-right transition duration-300 text-red"
          >
            {{ errorLabel }}
          </span>
        </slot>
      </transition>
    </label>
    <label
      class="bg-[#161E25] sm:px-[18px] ms:px-3 px-2 sm:py-[20px] py-3 pb-3.5 md:pb-4 rounded-[10px] flex items-center border border-[#161E25] border-opacity-[0.16] hover:border-opacity-50 hover:border-white focus-within:border-white transition-all duration-300 group"
      :class="[inputClass, { '!border-[red]': error }]"
    >
      <div class="flex items-start w-full">
        <slot name="prefix" class="pointer-events-none" />
        <textarea
          :id="`a-textarea-${id}`"
          :value="modelValue"
          :autocomplete="autocomplete"
          v-bind="{ minlength, maxlength, max, min, placeholder }"
          class="group"
          :class="[
            'outline-none w-full bg-transparent h-[150px] ms:h-[190px] leading-[125%] placeholder:text-[#C6C6C6] text-[#C6C6C6] font-medium text-sm sm:text-base resize-none',
            inputStyle,
          ]"
          :pattern="pattern"
          :required="required"
          @input="handleInput"
          @blur="handleBlur"
          @keyup.enter="handleSubmit"
        ></textarea>
        <div class="absolute bottom-0 right-3 md:right-4">
          <p class="text-[12px] text-white group-focus-within:text-white">
            {{ modelValue.length }} - {{ maxlength }}
          </p>
        </div>
      </div>
    </label>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

interface Props {
  type?: string;
  placeholder?: string;
  modelValue?: any;
  error?: boolean;
  maxlength?: number | string;
  minlength?: number;
  max?: number;
  min?: number;
  inputClass?: string;
  label?: string;
  errorLabel?: string;
  inputStyle?: string;
  optional?: boolean;
  autocomplete?: string;
  maska?: object;
  pattern?: string;
  required?: boolean;
  suffixClass?: string;
  inputCustomClass?: string;
}

withDefaults(defineProps<Props>(), {
  type: "text",
  maxlength: 100,
  minlength: undefined,
  max: undefined,
  min: undefined,
  inputStyle: undefined,
  inputClass: undefined,
});

const id = computed(() => {
  return Math.floor(Math.random() * 101);
});

const emit = defineEmits<{
  (e: "update:modelValue", value: any): void;
  (e: "blur", value: Event): void;
  (e: "keyup", value: Event): void;
}>();

const handleInput = (e: any) => {
  emit("update:modelValue", e.target.value);
};
const handleBlur = (e: Event) => {
  emit("blur", e);
};
const handleSubmit = (e: Event) => {
  emit("keyup", e);
};
</script>
