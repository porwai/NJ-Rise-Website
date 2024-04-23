import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

import { createApp } from 'vue'
import { createStore } from 'vuex'

import App from './App.vue'
import router from './router'

import { Store } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

console.log("check cookie at start:", checkCookie())

window.addEventListener('onbeforeload', function() {
  // your code to set value here

});

// Create a new store instance.
const store = createStore({
    state () {
      return {
        login_status: checkCookie()
      }
    },
    mutations: {
      log_in (state) {
        state.login_status = true
        setCookie("login_status", true, 1);
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


// W3 Schools function to getCookie with vanilla JS
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
function checkCookie() {
  let username = getCookie("login_status");

  if (username != "") {
   return true
  } 
  else {
    return false
  }
}

// Set a cookie for a given expiration day
function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
