<script setup>
import { ref } from 'vue';
import Carousel from 'primevue/carousel';
import 'primevue/resources/themes/saga-blue/theme.css'; // Tema do PrimeVue
import 'primevue/resources/primevue.min.css'; // Estilos gerais do PrimeVue
import 'primeicons/primeicons.css'; // Ícones do PrimeIcons

const produtos = ref([
  { name: 'sss', description: 'asmiksd', price: 555, image: 'https://cdn.oantagonista.com/uploads/2024/03/Neymar_Al-Hilal-scaled.webp' },
  { name: 'aaa', description: 'neymar', price: 999, image: 'https://cdn.oantagonista.com/uploads/2024/03/Neymar_Al-Hilal-scaled.webp'  },
  { name: 'a', description: 'aaa', price: 695, image: 'https://cdn.oantagonista.com/uploads/2024/03/Neymar_Al-Hilal-scaled.webp'  },
  { name: 'leticiaLinda', description: 'cristiano', price: 612, image: 'https://cdn.oantagonista.com/uploads/2024/03/Neymar_Al-Hilal-scaled.webp'  },
]);
const { data: teste } = await useFetch('http://localhost:8000/livros',{
      key: 'usuarioRequest' 
    });
</script>
<template>
    <div>
        <div class="tela">
      <CustomLayout />

        <Carousel :value="teste.results" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions">
          <template #item="{ data: livro }">
            <div class="border-1 surface-border border-round m-2 p-3 car-card">
              <div class="mb-3">
                <div class="relative mx-auto">
                  <!-- Verifica se fotoFK é um array e se tem pelo menos um elemento -->
                  <img :src="livro.fotoFK && livro.fotoFK.length > 0 ? livro.fotoFK[0] : ''" :alt="livro.titulo" class="w-full border-round image-card" />
                </div>
              </div>
              <div class="mb-3 font-medium">{{ livro.titulo }}</div>
              <div class="flex justify-content-between align-items-center">
                <div class="mt-0 font-semibold text-xl">COD: {{ livro.codEdicao }}</div>
                <span>
                  <Button icon="pi pi-heart" severity="secondary" outlined class="p-button-rounded p-button-outlined" />
                  <Button icon="pi pi-shopping-cart" class="ml-2 p-button-rounded" />
                </span>
              </div>
            </div>
          </template>
        </Carousel>

      <h4>Suas opções</h4>
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
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  text-align: center;
  color: black;
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
