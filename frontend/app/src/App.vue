<template>
  <div id="app">
    <router-view></router-view>  
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
body {
  margin: 0;
  background-repeat: no-repeat;
  overflow: hidden;
  background-size: cover;
  background-position: center center;
  background-image: url('./assets/wallpaper.jpg');
}
#app {
  margin: 0;
  width: 100vw;
  height: 100vh;
  background-color:rgba(0,0,0,0.8);
}
</style>
