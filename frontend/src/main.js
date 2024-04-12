import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'


// Create a new store instance.
const store = createStore({
    state () {
      return {
        login_status: false
      }
    },
    mutations: {
      log_in (state) {
        state.login_status = true
      },
      log_out (state) {
        state.login_status = false
      }
    }
  })


const app = createApp(App)
app.use(router)
app.use(store)

app.mount('#app')
