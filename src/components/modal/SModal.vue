<template>
  <div
    id="popup-modal"
    :class="{ 'modal-class': isOpen }"
    @click="emit('closeModal', false)"
    class="fixed top-0 hidden items-center justify-center z-50 p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-modal md:h-full h-[100vh]"
  >
    <div
      class="relative w-full h-full max-w-[550px] md:h-auto mx-auto"
      :class="customClass"
      @click="(e) => e.stopPropagation()"
    >
      <div class="relative bg-[#292929] rounded-[8px] shadow py-4 px-5">
        <div class="flex justify-between">
          <p class="font-bold text-white text-xl leading-[48.41px]">
            Biz bilan bog'laning
          </p>
          <i
            @click="emit('closeModal', false)"
            class="fa-sharp fa-solid fa-xmark text-white text-2xl cursor-pointer"
          ></i>
        </div>
        <div class="text-center w-full">
          <form class="mb-4">
            <SInput
              v-model="form.fullName"
              class="mt-3"
              input-class="!bg-white !py-3"
              inputStyle="!text-black !placeholder:text-black "
              placeholder="Ismingizni yozing"
              label="Ismingiz"
            />
            <SInput
              v-model="form.phoneNumber"
              type="phone"
              class="mt-3 sm:mt-4"
              input-class="!bg-white !py-3"
              inputStyle="!text-black !placeholder:text-black "
              placeholder="00 000-00-00"
              label="Ismingiz"
            >
              <template #prefix>
                <p class="mr-2 font-bold text-sm sm:text-base">+998</p>
              </template>
            </SInput>
            <SSelect
              v-model="form.select"
              class="mt-3 sm:mt-4"
              :data="selectData"
              placeholder="Turar joy"
              label="Turar hudidingiz tanlang"
            />
            <STextarea
              v-model="form.message"
              class="mt-3 sm:mt-4"
              inputClass="!bg-white !py-3"
              inputStyle="!text-black !placeholder:text-black h-[130px] ms:h-[150px]"
              placeholder="Qiziqishingiz haqida qisqacha yozing !"
              label="O'zingiz haqida !"
            />
          </form>

          <SButton variant="info" @click="fetchModal">Jo'natish</SButton>
          <div
            class="text-center mt-3 sm:mt-4 text-[#5E5E5E] text-sm"
            v-if="false"
          >
            Отправляя заявку, вы соглашаетесь
            <span class="text-[#2E8AD1]">
              с условиями использования политикой конфиденциальности
            </span>
            вы подтверждаете свое согласие
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import SButton from "@/components/SButton.vue";
import SInput from "@/components/form/SInput.vue";
import { reactive } from "vue";
import STextarea from "@/components/form/STextarea.vue";
import SSelect from "@/components/form/SSelect.vue";

interface Props {
  isOpen: boolean;
  customClass?: string;
}

defineProps<Props>();

const emit = defineEmits(["closeModal"]);

const form = reactive({
  fullName: "",
  phoneNumber: "",
  select: "",
  message: "",
});

function cancelModal() {
  console.log("cancel");
}

function fetchModal() {
  console.log("fetch");
  emit("closeModal", false);
}

const selectData = [
  {
    value: "Ташкент",
    label: "Ташкент",
  },
  {
    value: "Андижон",
    label: "Андижон ",
  },
  {
    value: "Бухоро ",
    label: "Бухоро ",
  },
  {
    value: "Жиззах ",
    label: "Жиззах ",
  },
  {
    value: "Қашқадарё  ",
    label: "Қашқадарё  ",
  },
  {
    value: "Навоий",
    label: "Навоий",
  },
  {
    value: "Самарқанд ",
    label: "Самарқанд ",
  },
  {
    value: "Сурхондарё ",
    label: "Сурхондарё ",
  },
  {
    value: "Фарғона ",
    label: "Фарғона ",
  },
];
</script>

<style scoped>
.modal-class {
  overflow: visible;
  display: flex;
  width: 100%;
  height: 100vh;
  backdrop-filter: blur(2px);
}
</style>
