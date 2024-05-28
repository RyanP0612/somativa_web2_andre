<script setup>
import { ref } from 'vue';
import Carousel from 'primevue/carousel';
import 'primevue/resources/themes/saga-blue/theme.css'; // Tema do PrimeVue
import 'primevue/resources/primevue.min.css'; // Estilos gerais do PrimeVue
import 'primeicons/primeicons.css'; // Ícones do PrimeIcons

const { data } = await useFetch('http://localhost:8000/livros/?aprovado=A', {
  key: 'usuarioRequest',
});





</script>
<template>
    <div>
        <div class="tela">
      <CustomLayout />

        <Carousel :value="data" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" >
          <template #item="{ data: livro }">
            <div class="border-1 surface-border border-round m-2 p-3 car-card">
              <div class="mb-3">
                <div class="relative mx-auto">
                  <!-- Verifica se fotoFK é um array e se tem pelo menos um elemento -->
                  <img :src="livro.fotoFK" :alt="livro.titulo" class="w-full border-round image-card" />
                </div>
              </div>
              <div class="mb-3 font-medium">{{ livro.titulo }}</div>
              <div class="flex justify-content-between align-items-center">
                <div class="mt-0 font-semibold text-xl">COD: {{ livro.codEdicao }}</div>
                <span>
                  <NuxtLink :to="`/livros/${livro.id}`">
                  <Button  class="ml-2 p-button-rounded">🔎</Button> 
                </NuxtLink>
                  <Button  class="ml-2 p-button-rounded">🛒</Button> 
                </span>
              </div>
            </div>
          </template>
        </Carousel>


    </div>
</div>
  </template>

<style scoped>
.tela {
  width: 100%;
  height: 100vh;
  background-image: url('assets/img/fundo.png');
  background-repeat: repeat;
  background-size: cover;
  color: white;
  
}
.car-card {
  width: auto;
  background-color: #5a2e01;
  border-radius: 15px;
  padding: 20px 10px;
  margin: 10px;
  text-align: center;
  color: #dda432;
  font-weight: 800;
  font-size: 1.2vw ;
  letter-spacing: 2px;
}
.image-card {
  max-width: 100%; /* Manter a imagem dentro do container */
  max-height: 200px; /* Altura máxima da imagem para evitar distorção */
}
.p-button-rounded {
  border-radius: 20px; /* Arredondar bordas dos botões */
  padding: 0.5rem 1rem; /* Ajustar espaçamento interno dos botões */
  font-size: 1rem; /* Tamanho da fonte dos botões */
}
</style>
