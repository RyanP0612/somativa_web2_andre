// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  modules: [
    'nuxt-primevue',
    'vue3-carousel-nuxt'
  ],
  carousel: {
    prefix: 'MyPrefix'
  },
  primevue: {
    components: {
      include: ['carousel', 'Carousel', 'toast', 'Toast']
    }
  },

css: [
  'primeicons/primeicons.css', //css dos ícones do primevue
  'primevue/resources/themes/aura-light-green/theme.css', // css tema dos componentes primevue
  '~/assets/style/global-project.scss',  //css global customizado para toda a aplicação
],
plugins: [
  '@/plugins/primevue' // Importa e registra o PrimeVue globalmente
]

})