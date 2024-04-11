<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/navbar.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { ref } from 'vue';
const adminprivlage = ref(false); // Assumes that 
</script>

<style>
  body {
  color: #292b2d;
  background: #b0adad;
  font-family: 'Roboto', sans-serif;
  font-size: 20px;
  }
</style>

<template>
  <header>
    <NavBar />
  </header>

  <div class="container-fluid">
    <RouterView />
  </div>

  <footer>

  </footer>

</template>