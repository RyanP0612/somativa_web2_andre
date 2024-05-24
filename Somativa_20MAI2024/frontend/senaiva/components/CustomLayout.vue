<template>
    <div>
      <div class="header">
        <NuxtLink to="/" exact :key="$route.path">
          <button id="home-button" @click="reloadPage">Home</button>
        </NuxtLink>
        <br>
        <NuxtLink to="/autor" exact :key="$route.path">
          <button id="autor-button" @click="reloadPage">Autor</button>
        </NuxtLink>
        <br>
        <NuxtLink to="/livros" exact :key="$route.path">
          <button id="livros-button" @click="reloadPage">Livros</button>
        </NuxtLink>
        <img class="ibagem" src="assets/img/biblio.png" alt="Profile Image">
      </div>
      <div class="section">
        <h2>Senaiva</h2>
      </div>
      <div class="gradient_linha"></div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      reloadPage(event) {
        const link = event.currentTarget.closest('a').getAttribute('href');
        if (link === this.$route.path) {
          window.location.reload();
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .header {
    width: 100%;
    height: 3rem;
    background-color: #010200;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 1rem;
  }
  .ibagem {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-left: 1rem;
  }
  .section {
    width: 100%;
    height: 2rem;
    background-color: #000000;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .gradient_linha {
    width: 100%;
    height: 0.3rem;
    background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet);
  }
  </style>
  