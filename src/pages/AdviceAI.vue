<script setup lang="ts">
import TapirWidget from "vue-audio-tapir";
import "vue-audio-tapir/dist/vue-audio-tapir.css";
import { ref } from "vue";
import SButton from "@/components/SButton.vue";

const textAI = ref("");

const submitText = () => {
  console.log(textAI.value, "text ai value");
};

const uploadAudio = (audioBlob: Blob) => {
  console.log(audioBlob, "e blob");
};

const finishRecord = (audio: Blob) => {
  console.log(audio, "audio");
  document.querySelector(".vue-audio button")?.click();
};
</script>

<template>
  <div class="container pt-6 sm:pt-10 pb-12 sm:pb-[100px]">
    <div class="max-w-[65%] w-full mx-auto">
      <h1 class="text-black font-medium text-xl">Advice AI</h1>
      <tapir-widget
        :time="5"
        :customUpload="uploadAudio"
        :afterRecording="finishRecord"
        buttonColor="blue"
        class="vue-audio"
      />
      <div class="mt-4">
        <label
          for="ai"
          class="rounded-2xl block min-h-[200px] p-4 relative overflow-hidden w-full bg-white"
        >
          <textarea
            id="ai"
            name="ai"
            v-model="textAI"
            class="resize-none w-full min-h-[180px] text-gray-700 placeholder:text-gray-700"
            placeholder="Write your text..."
          ></textarea>
          <div class="absolute bottom-4 right-4 w-full flex justify-between">
            <div></div>
            <div class="flex items-center gap-4">
              <div class="group cursor-pointer">
                <i
                  class="fa-solid fa-microphone text-blue-500 transition-all duration-300 group-hover:text-blue-700 text-2xl"
                ></i>
              </div>
              <SButton @click="submitText" variant="blue" class="font-normal"
                >Yuborish</SButton
              >
            </div>
          </div>
        </label>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
