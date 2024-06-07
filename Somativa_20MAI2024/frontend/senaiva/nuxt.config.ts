// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  
  modules: [
    'nuxt-primevue',
    'vue3-carousel-nuxt',
    '@sidebase/nuxt-auth'
    // '@pinia/nuxt'
  ],
  carousel: {
    prefix: 'MyPrefix'
  },
  primevue: {
    components: {
      include: ['carousel', 'Carousel', 'toast', 'Toast','Checkbox']
    }
  },
  vite: {
    server: {
      fs: {
        strict: false
      }
    }
  },

css: [
  'primeicons/primeicons.css', //css dos ícones do primevue
  'primevue/resources/themes/aura-light-green/theme.css', // css tema dos componentes primevue
  '~/assets/style/global-project.scss',  //css global customizado para toda a aplicação
],
plugins: [
  '@/plugins/primevue' // Importa e registra o PrimeVue globalmente
],
auth: {
  baseURL: 'https://somativaweb2andre-production.up.railway.app',
  provider: {
    type: 'local',
    endpoints: {
      signIn: { path: '/token/login', method: 'post' },
      signOut: { path: '/token/logout', method: 'post' },
      getSession: { path: '/usuarios', method: 'get' },
    },
    token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
    pages: { login: '/' },
    sessionDataType: {
      results: 'Array'
    }
  }
}
})