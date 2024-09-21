export interface ITariff {
  id: number;
  type: "simple" | "middle" | "gold";
  tariff: string;
  price: string;
  count: number;
  services: {
    id: number;
    title: string;
  }[];
}
