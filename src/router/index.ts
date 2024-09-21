import { createRouter, createWebHistory } from "vue-router";
import LDefault from "@/layout/LDefault.vue";
import LSingle from "@/layout/LSingle.vue";
import LAuth from "@/layout/LAuth.vue";

const routes = [
  {
    path: "/",
    name: "home",
    meta: { layout: LDefault },
    component: () => import("@/pages/HomePage.vue"),
  },
  {
    path: "/privacy_police",
    mame: "privacy",
    meta: { layout: LSingle },
    component: () => import("@/pages/PrivacyPolice.vue"),
  },
  {
    path: "/terms_use",
    mame: "use",
    meta: { layout: LSingle },
    component: () => import("@/pages/TermUse.vue"),
  },
  {
    path: "/faq",
    name: "faq",
    meta: { layout: LSingle },
    component: () => import("@/pages/FaqPage.vue"),
  },
  {
    path: "/login",
    name: "sign-in",
    meta: { layout: LAuth },
    component: () => import("@/pages/auth/SLogin.vue"),
  },
  {
    path: "/sign-up",
    name: "sign-up",
    meta: { layout: LAuth },
    component: () => import("@/pages/auth/SRegister.vue"),
  },
  {
    path: "/forgot",
    name: "forgot",
    meta: { layout: LAuth },
    component: () => import("@/pages/auth/ResetPassword/FirstStep.vue"),
  },
  {
    path: "/forgot/step1",
    name: "forgot-step1",
    meta: { layout: LAuth },
    component: () => import("@/pages/auth/ResetPassword/SecondStep.vue"),
  },
  {
    path: "/reset",
    name: "reset",
    meta: { layout: LAuth },
    component: () => import("@/pages/auth/ResetPassword.vue"),
  },
  {
    path: "/advice",
    name: "advice-chat",
    meta: { layout: LDefault },
    component: () => import("@/pages/AdviceAI.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),

  scrollBehavior() {
    return { top: 0 };
  },
  routes,
});

export default router;
