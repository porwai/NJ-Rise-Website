import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'

import CanvasJSChart from '@canvasjs/vue-charts';


// Create a new store instance.
const store = createStore({
    state () {
      return {
        login_status: checkCookie("login_status"),
        viewing_status: checkCookie("viewing_status"),
        master_db_view: false
      }
    },
    mutations: {
      log_in_admin (state) {
        state.login_status = "admin";
        setCookie("login_status", "admin", 1);
        state.viewing_status = "admin";
        setCookie("viewing_status", "admin", 1);
      },
      log_in_volunteer (state) {
        state.login_status = "volunteer";
        setCookie("login_status", "volunteer", 1);
        state.viewing_status = "volunteer";
        setCookie("viewing_status", "volunteer", 1);
      },
      log_in_admin_volunteer_view (state) {
        state.login_status = "admin";
        setCookie("login_status", "admin", 1);
        state.viewing_status = "volunteer";
        setCookie("viewing_status", "volunteer", 1);
      },
      log_out (state) {
        state.login_status = "not_authorized";
        setCookie("login_status", "not_authorized", 1);
        state.viewing_status = "not_authorized";
        setCookie("viewing_status", "not_authorized", 1);
      },
      toggleMasterDBView(state) {
        state.master_db_view = !state.master_db_view; // Mutation to toggle DB view
      }
    }
  });

export default store;

const app = createApp(App);
app.use(router);
app.use(store);
app.use(CanvasJSChart); // install the CanvasJS Vuejs Chart Plugin


app.mount('#app');

// Function to getCookie with vanilla JS
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

// Check if a cookie has been set
function checkCookie(cname) {
  let value = getCookie(cname);

  if (value != "") {
    return value;
  } else {
    return "not_authorized";
  }
}

// Set a cookie for a given expiration day
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}