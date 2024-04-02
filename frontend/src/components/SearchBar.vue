<template>
    <div>
      <div class="mb-3" v-for="n in 4" :key="n">
        <input type="search" class="form-control" :placeholder="'Search ' + n" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBars',
  }
  </script>
  
  <style scoped>
  </style>
  