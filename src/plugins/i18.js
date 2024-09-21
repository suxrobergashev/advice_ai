import { createI18n } from "vue-i18n";
import uz from "../language/uz.json";
import ru from "../language/ru.json";

const locale = localStorage.getItem("locale") || "uz";
// i18n.global.locale.value = locale;

const i18n = createI18n({
  locale,
  legacy: false,
  fallbackLocale: "uz",
  silentFallbackWarn: true,
  globalInjection: true,
  messages: {
    uz,
    ru,
  },
});

export default i18n;
