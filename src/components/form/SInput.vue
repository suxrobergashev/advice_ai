<template>
  <div class="block w-full relative">
    <label
      v-if="label"
      :for="`a-input-${id}`"
      class="flex items-center justify-between mb-1 sm:mb-2"
    >
      <span
        class="text-sm sm:text-base leading-130 text-[#04030866] font-normal"
        :class="labelStyle"
      >
        {{ $t(label) }}
      </span>
      <transition name="fade">
        <span
          v-if="error && errorLabel"
          class="text-xs font-semibold leading-4 text-right transition duration-300 text-[red]"
        >
          {{ errorLabel }}
        </span>
      </transition>
    </label>
    <label
      class="!bg-white border border-[#04030899] sm:px-4 ms:px-3 px-2 sm:py-3 dm:py-3  py-2 rounded-[5px] flex items-center transition-all duration-300  border-opacity-[0.16] hover:border-opacity-50 hover:border-[#04030866] focus-within:border-opacity-100 focus-within:border-[#04030866]"
      :class="[inputClass, { '!border-red': error }]"
    >
      <div class="flex items-center w-full">
        <slot name="prefix" class="pointer-events-none" />
        <input
          :id="`a-input-${id}`"
          v-maska="type === 'phone' ? '(##) ###-##-##' : maska ?? null"
          :value="modelValue"
          :autocomplete="autocomplete"
          :type="type === 'phone' ? 'text' : type"
          v-bind="{ minlength, maxlength, max, min }"
          :class="[
            'outline-none w-[100%] bg-transparent h-full placeholder:text-[#04030866]  text-[#04030899] text-sm sm:text-base  ',
            inputStyle,
          ]"
          :placeholder="placeholder"
          :pattern="pattern"
          :required="required"
          @input="handleInput"
          @blur="handleBlur"
          @keyup.enter="handleSubmit"
        />
      </div>

      <slot :class="suffixClass" name="suffix" />
    </label>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

interface Props {
  type?: string;
  placeholder?: string;
  modelValue: any;
  error?: boolean;
  maxlength?: number | string;
  minlength?: number | string;
  max?: number;
  min?: number;
  inputClass?: string;
  label?: string;
  errorLabel?: string;
  inputStyle?: string;
  optional?: boolean;
  autocomplete?: string;
  maska?: string;
  pattern?: string;
  required?: boolean;
  suffixClass?: string;
  labelStyle?: string;
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
