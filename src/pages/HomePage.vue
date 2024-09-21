<template>
  <div>
    <SBanner id="main" />
    <SAbout id="about" />
    <SOpportunity id="opportunity" />
    <STariff id="tariff" />
    <SComment id="comment" />
    <SFAQ id="faq" />
    <SQrCode id="download" />
  </div>
</template>
<script setup lang="ts">
import SBanner from "@/sections/SBanner.vue";
import SComment from "@/sections/SComment.vue";
import SAbout from "@/sections/SAbout.vue";
import SOpportunity from "@/sections/SOpportunity.vue";
import STariff from "@/sections/STariff.vue";
import SFAQ from "@/sections/SFAQ.vue";
import SQrCode from "@/sections/SQrCode.vue";
</script>
