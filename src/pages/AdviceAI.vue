<script setup lang="ts">
import { onMounted, ref } from "vue";
import "vue-audio-tapir/dist/vue-audio-tapir.css";
import TapirWidget from "vue-audio-tapir";
import SButton from "@/components/SButton.vue";
import { useFirstQuestion } from "../../store/first-question";
import { useNextQuestion } from "../../store/next-question";
import { useToast } from "vue-toastification";
import SSpinner from "@/components/SSpinner.vue";

const toast = useToast();

const firstQuestionStore = useFirstQuestion();
const nextQuestionStore = useNextQuestion();

const textAI = ref("");
const audioPlay = ref();

const showText = ref("");
const copyText = ref("");

const writeFunction = () => {
  showText.value += copyText.value?.slice(0, 1);
  copyText.value = copyText.value?.substring(1);
};

const submitText = () => {
  nextQuestionStore
    .postAnswer(firstQuestionStore.first_question?.id, textAI.value, "text")
    .then(() => {
      textAI.value = "";
      showText.value = "";
      copyText.value = "";
      firstQuestionStore.first_question.question_audio = "";
      firstQuestionStore
        .fetchNextQuestion(firstQuestionStore.chatID)
        .then(() => {
          copyText.value = firstQuestionStore.first_question?.question;
          if (firstQuestionStore.first_question?.question_audio)
            setTimeout(() => audioPlay.value?.play(), 200);
        });
      // .catch(() => {
      //   toast.error("Something went wrong");
      // });
    })
    .catch((error) => {
      console.log(error);
      toast.error("Something went wrong");
    });
};

const uploadAudio = (audioBlob: Blob) => {
  console.log(audioBlob, "e blob");
};

const finishRecord = (audio: Blob) => {
  console.log(audio, "audio");
  document.querySelector(".vue-audio button")?.click();
};

onMounted(() => {
  firstQuestionStore.fetchFirstQuestion().then(() => {
    copyText.value = firstQuestionStore.first_question?.question;
    if (firstQuestionStore.first_question?.question_audio)
      setTimeout(() => audioPlay.value?.play(), 200);
  });

  setInterval(() => {
    if (copyText.value.length > 1) writeFunction();
  }, 40);
});
</script>

<template>
  <div class="container pt-6 sm:pt-10 pb-12 sm:pb-[100px]">
    <div class="max-w-[85%] w-full mx-auto">
      <h1 class="font-medium text-xl text-gray-700">Advice AI</h1>
      <div
        class="min-h-[40vh] border rounded-2xl p-4 bg-[#F0F0FC] mt-3 overflow-hidden relative"
      >
        <audio
          ref="audioPlay"
          autoplay
          controls
          v-if="firstQuestionStore.first_question.question_audio"
        >
          <source
            :src="firstQuestionStore.first_question?.question_audio"
            type="audio/mpeg"
          />
          <source
            :src="firstQuestionStore.first_question?.question_audio"
            type="audio/ogg"
          />
        </audio>
        <div class="text-gray-700">
          {{ showText }}
        </div>
      </div>
      <div class="mt-4 flex gap-4">
        <label
          for="ai"
          class="rounded-2xl block min-h-[180px] p-4 relative overflow-hidden bg-white w-full"
        >
          <textarea
            id="ai"
            name="ai"
            v-model="textAI"
            class="resize-none w-full min-h-[160px] text-gray-700 placeholder:text-gray-700"
            placeholder="Write your text..."
          ></textarea>
          <div class="absolute bottom-4 right-4 w-full flex justify-between">
            <div></div>
            <div class="flex items-center gap-4">
              <SButton
                @click="submitText"
                :disabled="textAI.length === 0"
                variant="blue"
                class="font-normal"
              >
                <SSpinner class="mr-[6px]" v-if="firstQuestionStore.loading" />
                Yuborish
              </SButton>
            </div>
          </div>
        </label>
        <tapir-widget
          :time="5"
          :customUpload="uploadAudio"
          :afterRecording="finishRecord"
          buttonColor="blue"
          class="vue-audio basis-[35%] rounded-2xl"
        />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
