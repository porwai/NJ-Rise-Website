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
        login_status: "not_authorized",
        viewing_status: "not_authorized",
        master_db_view: false // Global boolean to toggle database view
      }
    },
    mutations: {
      log_in_admin (state) {
        state.login_status = "admin",
        state.viewing_status = "admin"
      },
      log_in_volunteer (state) {
        state.login_status = "volunteer",
        state.viewing_status = "volunteer"
      },
      log_out (state) {
        state.login_status = false
      },
      toggleMasterDBView(state) {
        state.master_db_view = !state.master_db_view; // Mutation to toggle DB view
    }
  }
})

const app = createApp(App)
app.use(router)
app.use(store)

app.mount('#app')
