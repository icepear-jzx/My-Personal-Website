<template>
  <div class="home">
    <div class="slogan">
      <p>While the world sleeps,</p>
      <p>you dream</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.slogan {
  margin: auto;
  color: white;
  text-align: center; 
  font-family: Arial,"Microsoft YaHei";
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
  font-weight: bold;
}
</style>
