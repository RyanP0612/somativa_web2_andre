<script setup>
import { useToast } from "primevue/usetoast";
const toast = useToast();

const show = (severity, summary, detail ) => {
    toast.add({ severity: severity, summary: summary, detail: detail, life: 3000 });
};
import { ref, computed } from 'vue';

const steps = ref([
  { title: 'Sobre o livro' },
  { title: 'Classificações' },
  { title: 'Informações finais' }
]);

const currentStep = ref(0);
const livro = ref({
  titulo: '',
  autor: '',
  editora: '',
  descricao: '',
  url: '',
  categoria: '',
  idade: '',
  formato: '',
  publicacao: '',
  valor: null,
  n_pag: null,
  quantidade: null,
  Cod: ''
});

const isFirstIndex = computed(() => currentStep.value === 0);
const isLastIndex = computed(() => currentStep.value === steps.value.length - 1);

const backToPrevStep = () => {
  if (!isFirstIndex.value) {
    currentStep.value -= 1;
  }
};

const goToNextStep = () => {
  if (!isLastIndex.value) {
    currentStep.value += 1;
  }
};



const validateForm = () => {
  let valid = true;

  // Validação para a primeira etapa
  if (currentStep.value === 0) {
    if (!livro.value.titulo || !livro.value.autor || !livro.value.editora || !livro.value.descricao || !livro.value.url) {
      valid = false;
    }
  }

  // Validação para a segunda etapa
  if (currentStep.value === 1) {
    if (!livro.value.categoria || !livro.value.idade || !livro.value.formato || !livro.value.publicacao) {
      valid = false;
    }
  }

  // Validação para a terceira etapa
  if (currentStep.value === 2) {
    if (!livro.value.valor || !livro.value.n_pag || !livro.value.quantidade || !livro.value.Cod) {
      valid = false;
    }
  }

  return valid;
};
const handleSubmit = async () => {
  if (validateForm()) {
    console.log('Formulário válido:', livro.value);
    
    try {
      const response = await fetch('http://localhost:8000/livros/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          titulo: livro.value.titulo,
          autor: livro.value.autor,
          editora: livro.value.editora,
          descricao: livro.value.descricao,
          fotoFK: livro.value.url,
          categoria: livro.value.categoria,
          idade: livro.value.idade,
          formato: livro.value.formato,
          publicacao: livro.value.publicacao,
          valor: livro.value.valor,
          numeroPaginas: livro.value.n_pag,
          quantidade: livro.value.quantidade,
          codEdicao: livro.value.publicacao
        }),
      });

      const data = await response.json();
      console.log('Resposta do servidor:', data);
      show('success', 'Campos preenchidos', 'Dados enviados com sucesso!');
    } catch (error) {
      console.error('Erro ao enviar dados:', error);
      show('error', 'Erro', 'Ocorreu um erro ao enviar os dados.');
    }
  } else {
    console.log('Por favor, preencha todos os campos.');
    show('error', 'Campos não preenchidos', 'Por favor preencha todos os campos!!!');
  }
};

</script>

<template>
  <div>
    <CustomLayout />
  <div class="page">
    
    <header class="page__header">
      <div class="stepper">
        <span
          v-for="(step, index) in steps"
          :key="step.title"
          :class="{'stepper__item--active': currentStep === index}"
        >
          {{ index + 1 }} - {{ step.title }}
        </span>
      </div>
    </header>
    <section class="page__content">
      <form @submit.prevent="handleSubmit">
        <!-- Etapa sobre o livro -->
        <template v-if="currentStep == 0">
                    <div class="form__row">
                        <div class="form__field">
                            <label for="titulo">Título</label>
                            <input id="titulo" v-model="livro.titulo"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="autor">Autor</label>
                            <input id="autor" v-model="livro.autor"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="editora">Editora</label>
                            <input id="editora" v-model="livro.editora"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="descricao">Descrição</label>
                            <textarea
                            id="descricao"
                            v-model="livro.descricao"
                            class="auto-resize"
                            @input="resizeTextarea"
                            rows="1"
                            ></textarea>
                        </div>
                        <div class="form__field">
                            <label for="fotoFK">Foto(url)</label>
                            <input id="fotoFK" v-model="livro.url"  type="text">
                        </div>
                    </div>
                </template>
                
                <!-- etapa de classificação -->
                <template v-if="currentStep == 1">
                    <div class="form__row">
                        <div class="form__field">
                            <label for="categoria">Categoria</label>
                            <!-- <input id="categoria" v-model="livro.categoria"  type="text">
                             -->
                             <select name="categorias" id="categoria" v-model="livro.categoria">
                                <option value="T" >Terror😱</option>
                                <option value="R">Romance💓</option>
                                <option value="A">Aventura🧗</option>
                                <option value="M">Mistério🕵️‍♂️</option>
                                <option value="FC" >Ficção científica🧟</option>
                                <option value="D">Drama😭</option>
                                <option value="C" >Crime🦹</option>
                                <option value="H">História📖</option>
                                <option value="B">Biografia👴</option>
                                <option value="E">Ensino✍️</option>
                                <option value="AA" >Autoajuda🧘‍♀️</option>
                                <option value="F">Fantasia🥷</option>
                                <option value="LIJ">Infanto-juvenil👨‍👩‍👧‍👦</option>
          
                            </select>
                             
                        </div>
                        <div class="form__field">
                            <label for="idade">Classificação Indicativa</label>
                            <!-- <input id="idade" v-model="livro.idade"  type="text"> -->
                            <select name="idades" id="idade" v-model="livro.idade">
                                <option value="L" >Livre</option>
                                <option value="10">10 anos</option>
                                <option value="12">12 anos</option>
                                <option value="14">14 anos</option>
                                <option value="16" >16 anos</option>
                                <option value="18">18 anos</option>
          
                            </select>
                            
                        </div>
                        <div class="form__field">
                            <label for="formato">Formato</label>
                            <!-- <input id="formato" v-model="livro.formato"  type="text"> -->
                            <select name="formatos" id="formatinho" v-model="livro.formato">
                                <option value="E" >EBOOK</option>
                                <option value="F">Físico</option>
                       
                            </select>
                        </div>
                        <div class="form__field">
                            <label for="publicacao">Data de Publicação</label>
                            <input id="publicacao" v-model="livro.publicacao"  type="date">
                        </div>
                    </div>
                </template>
                <!-- etapa de informações adicionais -->
                <template v-if="currentStep == 2">
                    <div class="form__row">
                        <div class="form__field">
                            <label for="valor">Valor do livro para empréstimo</label>
                            <input id="valor" v-model="livro.valor"  type="number">
                        </div>
                        <div class="form__field">
                            <label for="n_pag">Número de páginas</label>
                            <input id="n_pag" v-model="livro.n_pag"  type="number" step="1">
                        </div>
                        <div class="form__field">
                            <label for="quantidade">Quantidade de livros disponíveis</label>
                            <input id="quantidade" v-model="livro.quantidade"  type="number" step="1">
                        </div>
                        <div class="form__field">
                            <label for="cod">Código do Livro</label>
                            <input id="cod" v-model="livro.Cod"  type="text">
                        </div>
                        <div class="card flex justify-content-center">

    </div>
                    </div>
                    
                </template>
      </form>
      <div class="page__footer">
        <button type="button" class="btn-primary" :disabled="isFirstIndex" @click="backToPrevStep">
          Voltar
        </button> 
       
        <Toast />
        <button v-if="isLastIndex" type="button" class="btn-primary" @click="handleSubmit">
          Salvar
        </button>
        
        <button v-else type="button" class="btn-primary" @click="goToNextStep">
        
          Próximo
        </button>
       
        
        
        
      </div>
    </section>
    
  </div>
  </div>
</template>







<style scoped>
.auto-resize {
  width: 100%;
  box-sizing: border-box; 
  /* overflow: hidden;  */
  /* resize: none;  */
}
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
  /* box-shadow: 0 2px 8px #cecece; */
}

.stepper {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 38px;
  font-size: 1vw;
  font-weight: 800;
  margin: 0;
  color: #1a0e01;
}
.stepper__item--active {
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
  position: relative;
}

form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 18px;
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
.form__field label {
  margin-left: 8px;
  font-size: 1vw;
  font-weight: 800;
  margin: 0;
  color: #dda432;
}
.form__field input,
.form__field textarea,
.form__field select {
  width: 100%;
  border: none;
  border-radius: 10px;
  padding: 15px;
  background: #8a786694;
  color: #f0ffffde;
  font-size: 12pt;
  box-shadow: 0px 10px 40px #00000056;
  outline: none;
  box-sizing: border-box;
}
.form__field input:focus,
.form__field select:focus {
  border-color: #0ea5e9;
}
.form__field-error {
  font-size: 0.7rem;
  color: red;
}

.page__footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 70px;
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
  box-sizing: border-box;
}
.page__footer button.btn-primary {
  width: auto;
  font-size: 2vh;
  padding: 16px 10px;
  margin: 20px;
  border: none;
  border-radius: 8px;
  box-sizing: border-box;
  outline: none;
  text-transform: uppercase;
  font-weight: 800;
  letter-spacing: 2.2px;
  color: #291400;
  background: #dda432;
  cursor: pointer;
  box-shadow: 0px 10px 40px -12px #70541c;
}
</style>
