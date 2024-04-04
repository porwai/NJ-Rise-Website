<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/navbar.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
</script>

<template>
  <NavBar />
  <div class="container-fluid">
    <RouterView />
  </div>

  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/login">Log In</RouterLink> <!-- temp for testing -->
  </nav>
</template>
