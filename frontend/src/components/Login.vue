<!-- Login.vue -->
<template>
  <div class="card">
    <div class="card-body">
      <div class="text-center">
        <img src="/src/assets/RiseLogo.png" style="max-width: 8%" class="mb-4 mt-5" alt="NJ Rise logo">
        <h4 class="mb-5">Log in to Staff Dashboard</h4>
      </div>

      <form class="col-lg-4 offset-lg-4">
        <div class="form-group">
          <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Email">
        </div>

        <div class="form-group">
          <input type="password" class="form-control" id="InputPwd" placeholder="Password">
          <a href="#" class="small float-right" for="InputPwd">Forget your password?</a>
        </div>

        <div class="text-center">
          <button type="submit" class="btn btn-primary mt-4">Log In</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style>
  .card {
    background-color: white; /* Sets card background to white */
    margin: 20px; /* Adds margin around the card for spacing */
    height: 80vh;
  }
</style>

<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>
