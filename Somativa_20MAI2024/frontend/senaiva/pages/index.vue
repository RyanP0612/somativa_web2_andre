<script setup >

import { reactive, ref } from 'vue';
const { signIn } = useAuth();

const libraria = () => {
  window.location.href = 'https://somativa-web2-andre.vercel.app/livros';
}

const teste = ref(false); 

const bot = () =>
{
    teste.value = !teste.value; 
}



const credenciais = reactive({
    username: '',
    password: ''
});
const mensagemErro = ref('');

const fazerLogin = () => {
    console.log("login: ", credenciais);
    signIn(credenciais, { redirect: false })
        .then(() => {
            console.log("logado com sucesso....");
            navigateTo('/livros');
        })
        .catch((error) => {
            console.error("error: ", error);
            console.error("aaaaa: ", mensagemErro);
            mensagemErro.value = 'Não foi possível fazer o login com estas credenciais...';
            setTimeout(() => {
                mensagemErro.value = '';
                credenciais.email = '';
                credenciais.password = '';
            }, 3000);
        })
}

const painel = ref();



</script>


<template>
    <div class="main-login">

      <div class="left-login">
        <h1>Faça LOGIN <br> e entre para nosso clube de leitura</h1>
        <img src="assets/img/logoInit.svg" class="left-login-img" alt="logo de uma mulher lendo">
      </div>
      <div class="right-login">
        
        <div class="card-login">
          <h1>LOGIN</h1>
          <div class="text-field">
            <label for="usuario">Usuário</label>
            <input v-model="credenciais.username" type="text" name="usuario" placeholder="Usuário">
            
          </div>
          <div class="text-field">
            <label for="senha">Senha</label>
            <input  v-model="credenciais.password" type="password" name="senha" placeholder="Senha">
            
          </div>
          <button @click="fazerLogin" class="btn-login">Login</button>
          
          <button @click="libraria" class="btn-login" >Ver livros</button>
          <button @click="bot" class="btn-login" >BOT🤖</button>
          
          
      
        
        </div>
        <div v-if="teste">
            <iframe
    allow="microphone;"
    width="320"
    height="350"
    src="https://console.dialogflow.com/api-client/demo/embedded/1a42e1f4-c0cc-42e7-ab38-e9a2067df8e2">
</iframe>
          </div>

      </div>
       

       
   
</div>
  </template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Elymaic&family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap');
.main-login{
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  background: #291400;
  display: flex;
  justify-content: center;
  align-items: center;
}
.left-login{
  width: 50vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.left-login > h1{
  margin-top: 65px;
padding: 20px 20px;
  font-size: 3vw ;
  color: #ebab2d;
}
.left-login-img{
  width: 35vw;
  margin-top: -100px;
}
.right-login{
  width: 50vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.card-login{
  margin: 15px;
  width: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 10px 15px;
  background: #3a1d00;
  border-radius: 20px;
  box-shadow: 0px 10px 40px #00000056;
  
}
.card-login > h1{
  color: #dda432;
  font-weight: 800;
  margin: 0;
}

.text-field{
  width: 100%;
  display: flex;
  flex-direction: column; /* Inverte o justify content de X para Y e o align-items de Y para X */
  align-items: flex-start;
  justify-content: center;
  margin: 10px 0px;
  
}

.text-field > input{
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

.text-field > label{
  color: #f0ffffde;
  margin-bottom: 10px;
}
.text-field > input::placeholder{
  color: #f0ffff94;
}

.btn-login{
  width: 100%;
  padding: 10px 0px;
  margin: 10px;
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
  box-shadow: 0px 10px 40px -12px #70541c;
}
@media only screen and (max-width: 850px){
  .card-login{
    width: 85%;
  }
}
@media only screen and (max-width: 650px){
  .main-login{
    flex-direction: column;
  }
  .left-login > h1{
    display: none;

  }
  .left-login{
    width: 100%;
    height: auto;
  }
  .right-login{
    width: 100%;
    height: auto;
  }
  .left-login-img{
    width: 50vh;
  }
  .card-login{
    width: 90%;
    box-sizing: border-box
  }
}

</style>
