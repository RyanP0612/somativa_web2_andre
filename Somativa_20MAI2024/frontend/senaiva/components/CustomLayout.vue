<template>
    <div>
      <div class="header">
        <NuxtLink to="/" exact :key="$route.path">
          <button class="btn-primary" id="home-button" @click="reloadPage">Home</button>
        </NuxtLink>
        <br>
        <NuxtLink to="/autor" exact :key="$route.path">
          <button class="btn-primary" id="autor-button" @click="reloadPage">Autor</button>
        </NuxtLink>
        <br>
        <NuxtLink to="/livros" exact :key="$route.path">
          <button class="btn-primary" id="livros-button">Livros</button>
        </NuxtLink>
        <br>
        <NuxtLink to="/biblioteca" exact :key="$route.path">
          <button class="btn-primary" id="autor-button" @click="reloadPage">bibliotecária</button>
        </NuxtLink>
      
        <button @click="openLink('http://127.0.0.1:8000/admin')" class="btn-primary">⚙️</button>
        <img class="ibagem" src="assets/img/logoInit.svg" alt="Profile Image">
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
      },
      openLink(url) {
      window.location.href = url;
    }
    }
  }
  </script>
  
  <style scoped>
  .header {
    width: 100%;
    height: 3rem;
    background-color: #291400;
    color: white;
    display: flex;
    justify-content:center;
    align-items: center;
    padding: 0 1rem;
  }
  .ibagem {
  width: 6vw;
  border-radius: 50%;
  margin-top: 25px; 
  margin-left: 80px;
}
  .section {
    width: 100%;
    height: 2rem;
    background-color: #291400;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #dda432;
  }

  .gradient_linha {
    width: 100%;
    height: 0.3rem;
    background: #dda432;
  }
  .btn-primary {
    width: auto;
  font-size: 1.5vh;
  padding: 10px 10px;
  margin: 20px;
  border: none;
  border-radius: 8px;
  box-sizing: border-box;
  outline: none;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 3px;
  color: #291400;
  background: #dda432;
  cursor: pointer;
  box-shadow: 0px 10px 40px -12px #70541c
 
}
  </style>
  