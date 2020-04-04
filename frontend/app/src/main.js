import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'

Vue.config.productionTip = false

const routes = [
  { path: '/', component: Home }
]

const router = new VueRouter({
  routes: routes
})

new Vue({
  router
}).$mount('#app')
