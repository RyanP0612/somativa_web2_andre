<script >
export default {
    name: 'indexAutor',

    data() {
        return {
            currentStep: 0,
            steps: [],
            livro: {
                titulo: '',
                valor: '',
                quantidade: '',
                autor: '',
                descricao: '',
                editora: '',
                idade: '',
                publicacao: '',
                categoria: '',
                url: '',
                n_pag: '',
                formato: '',
                Cod: '',
            }
        }
    },

    computed: {
        isFirstIndex() {
            return this.currentStep === 0
        },
        isLastIndex() {
            return this.currentStep === this.steps.length - 1
        }
    },
    created() {
        this.steps = [
            { title: 'Sobre o livro' },
            { title: 'Classificações' },
            { title: 'Informações finais' }
        ]
    },
    methods: {
        backToPrevStep() {
            if (!this.isFirstIndex) {
                this.currentStep -= 1
            }
        },
        goToNextStep() {
            if (!this.isLastIndex) {
                this.currentStep += 1
            }
        },
        submit() {
            console.log('save data', this.livro)
        }
    }
}
</script>
<template>
    
    <div class="page">
        <header class="page__header" >

            <div class="stepper">

                <span v-for="(step, index) in steps" :key="step.title" :class="{'stepper__item--active': currentStep == index}">
                    {{ index + 1  }} - {{ step.title }}

                
                </span>
            </div>

        </header>
        <section class="page__content">
            <form>
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
                            <input id="descricao" v-model="livro.descricao"  type="text">
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
                            <input id="categoria" v-model="livro.categoria"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="idade">Classificação Indicativa</label>
                            <input id="idade" v-model="livro.idade"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="formato">Formato</label>
                            <input id="formato" v-model="livro.formato"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="publicacao">Data de Publicação</label>
                            <input id="publicacao" v-model="livro.publicacao"  type="text">
                        </div>
                    </div>
                </template>
                <!-- etapa de informações adicionais -->
                <template v-if="currentStep == 2">
                    <div class="form__row">
                        <div class="form__field">
                            <label for="valor">Valor do livro para empréstimo</label>
                            <input id="valor" v-model="livro.valor"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="n_pag">Número de páginas</label>
                            <input id="n_pag" v-model="livro.n_pag"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="quantidade">Quantidade de livros disponíveis</label>
                            <input id="quantidade" v-model="livro.quantidade"  type="text">
                        </div>
                        <div class="form__field">
                            <label for="cod">Código do Livro</label>
                            <input id="cod" v-model="livro.Cod"  type="text">
                        </div>
                    </div>
                </template>
                
            </form>
            <div class="page__footer">
                <button type="button" class="btn-primary" :disabled="isFirstIndex"
                @click="backToPrevStep">
            Voltar</button>
            <button v-if="isLastIndex" type="button" class="btn-primary" @click="submit">
            Salvar</button>
            <button v-else
            type="button"
            class="btn-primary"
            @click="goToNextStep">
        Próximo</button>
            </div>

        </section>
    </div>
</template>







<style scoped>
.page {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #fafafa;
}

.page__header {
  width: 100%;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-bottom: 1px solid #ededed;
  box-shadow: 0 2px 8px #cecece;
}

.stepper {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 38px;
}
.stepper__item--active {
  color: #0ea5e9;
}

.page__content {
  width: 90%;
  height: 80vh;
  margin-top: 48px;
  border: 1px solid #ededed;
  border-radius: 6px;
  padding: 18px;
  background: #fff;
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
  font-size: 0.8rem;
  color: rgba(0, 0, 0, 0.75);
}
.form__field input,
.form__field select {
  width: 100%;
  background: #fafafa;
  border: 1px solid #ededed;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 1rem;
  outline: none;
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