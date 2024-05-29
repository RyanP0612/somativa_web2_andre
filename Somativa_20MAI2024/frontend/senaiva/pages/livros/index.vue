<script setup>
import { ref } from 'vue';
import Carousel from 'primevue/carousel';
import 'primevue/resources/themes/saga-blue/theme.css'; // Tema do PrimeVue
import 'primevue/resources/primevue.min.css'; // Estilos gerais do PrimeVue
import 'primeicons/primeicons.css'; // Ícones do PrimeIcons

// Função para remover acentos
function removeAccents(str) {
  return str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

// Fazendo a requisição para obter os dados dos livros
const { data: livros } = await useFetch('http://localhost:8000/api/auth/livros/?aprovado=A', {
  key: 'livrosRequest',
});

// Filtrando os livros que contêm "leticia" no título (com ou sem acentos, maiúsculas ou minúsculas)
const filteredBooksCarousel = livros.value.filter(livro => 
  removeAccents(livro.titulo).toLowerCase().includes('leticia')
);
const filteredBooks = livros.value.filter(livro => 
  !removeAccents(livro.titulo).toLowerCase().includes('leticia')
);
</script>
<template>
    <div>
        <div class="tela">
      <CustomLayout />
      <h2 >🥃 Nossos MELHORES livros💖</h2>
        <Carousel :value="filteredBooksCarousel" :numVisible="4" :numScroll="1" :responsiveOptions="responsiveOptions" >
          <template #item="{ data: livro }">
            <div class="border-1 surface-border border-round m-2 p-3 car-card">
              <div class="mb-3">
                <div class="relative mx-auto">
                  <!-- Verifica se fotoFK é um array e se tem pelo menos um elemento -->
                  <img :src="livro.fotoFK" :alt="livro.titulo" class="w-full border-round image-card" />
                </div>
              </div>
              <div class="flex flex-row">
      <span>R${{ livro.valor }} - </span>
      <div class="ml-2">
        <label>Qtd. Disponível: </label>
        <span>{{ livro.quantidade }} </span>
      </div>
    
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
        <h2 >🥃 Nossos Produtos</h2>
        <div class="home-container flex  align-items-center">
        
        <Toast />
        <div v-for="(produto,index)  in livros" :key="produto.id" >
          <NuxtLink :to="`/livros/${produto.id}`">
            <ProdutoItem :key="index" class="col-3" :produto="produto" @eventoAdicionado="show" />
          </NuxtLink>
        </div>
      </div>
  </div>
    </div>

  </template>

<style scoped>
.home-container {
  align-items: center;
  justify-content: center;
  margin: 0;
  width: 100vw;
  display: flex;
 
  box-sizing: border-box;
  flex-wrap: wrap; /* Adiciona flex-wrap para itens que ultrapassam a largura */
  

}

.p-toast-summary		{
  padding: 1.5rem !important;
}
.tela {
  width: 100vw;
  height: auto;
  background-image: url('assets/img/fundo.png');
  background-repeat: repeat;
  background-size: cover;
  
  
}
.tela > h2{
  width: auto;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #291400;
  font-weight: 800;
  font-size: 1.5vw ;
  letter-spacing: 2px;
  background: #dda432;
}
.car-card {
  width: auto;
  background-color: #5a2e01;
  border-radius: 15px;
  padding: 25px 15px;
  margin: 15px;
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
