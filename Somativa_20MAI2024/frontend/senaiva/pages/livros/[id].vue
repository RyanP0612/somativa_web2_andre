<script setup>
const livroFound = ref([]);

    // acessamos o mecanismo de rotas do NUXT
    const route = useRoute();
    
    async function fetchBooks() {
  try {
    // Tenta fazer a requisição para a primeira URL
    const {data: livrosResponse} = await useFetch(`https://somativaweb2andre-production.up.railway.app/api/auth/livros/${route.params.id}`,{
      key: 'tarefaRequest' 
    });
    livroFound.value = livrosResponse.value;
  } catch (firstError) {
    console.error("Erro na primeira requisição:", firstError);

    try {
      // Caso a primeira requisição falhe, tenta a segunda URL
      const { data: livrosResponse } = await useFetch(`https://somativaweb2andre-production.up.railway.app/livros/${route.params.id}`, {
        key: 'livrosRequestFallback',
      });
      livroFound.value = livrosResponse.value;
    } catch (secondError) {
      console.error("Erro na segunda requisição:", secondError);

      // Se a segunda requisição também falhar, lança um erro
      throw new Error("Ambas as requisições falharam.");
    }
  }
}

fetchBooks();
    const paramsID = await route.params.id
    
</script>


<template>
    <div>
      <CustomLayout />
    <div class="page">
      
      <header class="page__header">
        <div class="stepper">
          <h1
           
            :key="livroFound.titulo"
          
          >
            {{ livroFound.titulo }} - {{ livroFound.valor }}
          </h1>
        </div>
      </header>
      <section class="page__content">
        <div>
      
        <h3>Sobre o livro: </h3>
        <p>Título: {{ livroFound.titulo }}</p>
        <p>Descrição: {{ livroFound.descricao }}</p>
        <p>Autor: {{ livroFound.autor }} </p>
        <p>Editora: {{ livroFound.editora }}</p>
</div><img class="image" :src="livroFound.fotoFK" :alt="livroFound.titulo + imagem">
<div>
        <h3>Classificações: </h3>
        <p>Classificação Indicativa: {{ livroFound.idade_display }}</p>
        <p>Categoria: {{ livroFound.categoria_display }}</p>
        <p>Formato: {{ livroFound.formato_display }}</p>
        <p>Data de Publicação: {{ livroFound.publicacao }}</p>
        <br>
        <h3>Mais Informações</h3>
        <h5>Valor de empréstimo: {{livroFound.valor}}</h5>
        <p>Número de páginas: {{ livroFound.numeroPaginas }}</p>
        <h5>Livros disponíveis: {{ livroFound.quantidade }}</h5>
        <p>Código do livro: {{ livroFound.codEdicao }}</p>
    </div>
    
        
      </section>
      
      
    </div>
    </div>
  </template>
  
  
  
  
  
  
  
  
  <style scoped>

  .page {
    overflow: hidden;
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url('assets/img/fundo.png');
  }
  
  .page__header {
    width: 100%;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #3a1d00;
  background-size: cover;
  border-bottom: 1px solid #ebab2d;
  }
  
  .stepper {
    width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 38px;
  font-size: 1vw;

  margin: 0;
  color: #ebab2d;
  font-weight: 1000;
  }

  
  .page__content {
    width: 90%;
  height: 80vh;
  margin-top: 48px;
  border: 1px solid #ebab2d;
  border-radius: 6px;
  padding: 18px;
  background: #3a1d00;

  /* margin-left: 8px; */
    font-size: 1vw;
  font-weight: 800;
  /* margin: 0; */
  color: #dda432;
    justify-content: space-around;

    display: flex;
  }
  .image {
  max-width: 380px; /* Manter a imagem dentro do container */
  max-height: 350px; /* Altura máxima da imagem para evitar distorção */
}

  
  .form__row {
    width: 100%;
    display: flex;
    gap: 18px;
  }
  
  .form__field {
    display: flex;
    flex-direction: column;
    flex: 1;
    gap: 8px;
  }



  
  .page__footer {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 48px;
    display: flex;
    justify-content: space-between;
    padding-left: 18px;
    padding-right: 18px;
  }
  .page__footer button {
    display: flex;
    justify-content: center;
    align-items: center;
    background: transparent;
    border: 1px solid #cecece;
    font-size: 1rem;
    color: #9e9e9e;
    padding: 12px;
    max-height: 32px;
    border-radius: 4px;
    cursor: pointer;
  }
  .page__footer button.btn-primary {
    border-color: #0ea5e9;
    color: #0ea5e9;
  }
  </style>