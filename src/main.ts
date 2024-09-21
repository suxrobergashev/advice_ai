import { createApp } from "vue";
import App from "./App.vue";
import "@/styles/index.css";

import i18n from "./plugins/i18";
import router from "./router";

// toast notification
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

// pinia

const pinia = createPinia()

// maska;
import Maska from "maska";

// element plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

//aos animation
import AOS from "aos";
import "aos/dist/aos.css";

const app = createApp(App);
app.use(router);
app.use(Toast);
app.use(Maska);
app.use(i18n);
app.use(ElementPlus);
app.AOS = new AOS.init({ once: true });
app.mount("#app");
