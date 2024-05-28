<template>
  <section class="cartao flex flex-column align-items-center justify-content-center" v-if="true">
    <div class="check text-right">      
      <!-- <Checkbox v-model=" :binary="true" :readonly="true"/> -->
    </div>
    <div class="produto-imagem">
      <img :src="produto.fotoFK" />
    </div>
    <div>
      <!-- Adiciona a classe limite-linhas condicionalmente -->
      <h4 :class="{ 'limite-linhas': produto.titulo.length > 25 }" class="produto-nome">{{ produto.titulo }}</h4>
    </div>
    <div class="flex flex-row">
      <span>R${{ produto.valor }} - </span>
      <div class="ml-2">
        <label>Qtd. Disponível: </label>
        <span>{{ produto.quantidade }} </span>
      </div>
    </div>
    <Button class="botao-add" label="Adicionar"  />
  </section>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

type Livro = {
  id: number;
  titulo: string;
  nota: number;
  valor: number;
  quantidade: number;
  autor: string;
  descricao: string;
  editora: string;
  idade: string;
  dataLancamento: string;
  publicacao: string;
  categoria: string;
  fotoFK: string;
  numeroPaginas: number;
  formato: string;
  codEdicao: string;
  aprovado: string;
};

const props = defineProps<{
  produto: Livro;
}>();
</script>

<style scoped lang="scss">
.cartao {
  width: 350px;
  border: 3px solid #1a0e01; 
  height: 400px;
 
  background-color: #5a2e01;
  border-radius: 15px;
  padding: 20px 10px;
  margin: 40px;
  text-align: center;
  color: #dda432;
  font-weight: 800;
  font-size: 1.2vw ;
  letter-spacing: 2px;
  
  cursor: pointer;
  box-sizing: border-box;

  &:hover {
    transform: scale(1.1);
    transition: 2s;
    box-shadow: 0px 10px 40px #00000056;
    border: 3px solid #dda432;
  }

  .produto-imagem {
    width: 90%;
    height: 55%;
    max-width: 200px;
    max-height: 230px;
    box-sizing: border-box;
  
    img {
      width: 100%;
      height: 100%;
    }
  }

  .produto-nome {
    margin: 0.5rem;
  }

  .botao-add {
    width: 80%;
    height: 2rem;
    margin: 1rem;
  }

  .check {
    width: 95%;
  }

  .limite-linhas {
    /* Define o número máximo de linhas para o título */
    max-height: 3.6rem; /* Ajuste conforme necessário */
    overflow: hidden;
    text-overflow: ellipsis;
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: pre-wrap;
  }
}
</style>
