<template>
  <Teleport to="body">
    <div class="load-wrapp">
      <div class="load-3">
        <!--          <p>loading</p>-->
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.load-wrapp {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 10000;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  margin: 0 10px 10px 0;
  padding: 20px 20px 20px;
  border-radius: 5px;
  text-align: center;
  background-color: #ff6600;
  /*  background: linear-gradient(265.79deg, #341289 -16.8%, #9949FF 89.61%);*/
}

.line {
  display: inline-block;
  width: 15px;
  height: 15px;
  border-radius: 15px;
  margin-left: 8px;
  background-color: #fff;
}

.load-3 .line:nth-last-child(1) {
  animation: loadingC 0.6s 0.1s linear infinite;
}
.load-3 .line:nth-last-child(2) {
  animation: loadingC 0.6s 0.2s linear infinite;
}
.load-3 .line:nth-last-child(3) {
  animation: loadingC 0.6s 0.3s linear infinite;
}

@keyframes loadingC {
  0 {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(0, 15px);
  }
  100% {
    transform: translate(0, 0);
  }
}
</style>
