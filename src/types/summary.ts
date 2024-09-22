export interface ISummary {
  id: number;
  user: number;
  summary_audio: string;
  summary: string;
}

export interface ISummaryResponse {
  ok: boolean;
  result: ISummary;
}
