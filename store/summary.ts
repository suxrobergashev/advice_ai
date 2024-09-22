import { defineStore } from "pinia";
import API from "../src/plugins/axios";
import { useToast } from "vue-toastification";
import { ISummary, ISummaryResponse } from "../src/types/summary";

const toast = useToast();

export const useSummaryStore = defineStore("summary", {
  state: () => ({
    summary: {} as ISummary,
    loading: false,
    error: false,
  }),
  actions: {
    async fetchSummary() {
      this.loading = true;
      try {
        const response = await API.get<ISummaryResponse>(`/summary/`);
        const data = response.data;
        if (data.ok) {
          this.summary = data.result;
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
