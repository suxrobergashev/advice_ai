import { defineStore } from "pinia";
import API from "../src/plugins/axios";
import { IFirstQuestion, IFirstQuestionResponse } from "@/types/first-question";
import { useToast } from "vue-toastification";

const toast = useToast();

export const useFirstQuestion = defineStore("firstQuestion", {
  state: () => ({
    first_question: {} as IFirstQuestion,
    chatID: 0,
    end: false,
    loading: false,
    error: false,
  }),
  actions: {
    async fetchFirstQuestion() {
      this.loading = true;
      try {
        const response = await API.get<IFirstQuestionResponse>("/questions/");
        const data = response.data;
        if (data.ok) {
          this.first_question = data.result;
          this.chatID = data.chat;
          this.end = data.end;
        }
      } catch {
        this.error = true;
        toast.error("Something went wrong");
      } finally {
        this.loading = false;
      }
    },
    async fetchNextQuestion(id: number) {
      this.loading = true;
      try {
        const response = await API.get<IFirstQuestionResponse>(
          `/questions/next/${id}/`
        );
        const data = response.data;
        if (data.ok) {
          this.first_question = data.result;
          this.chatID = data.chat;
          this.end = data.end;
        }
      } catch {
        this.error = true;
        toast.error("Something went wrong");
      } finally {
        this.loading = false;
      }
    },
  },
});
