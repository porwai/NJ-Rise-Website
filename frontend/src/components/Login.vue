<!-- Login.vue -->

<template>
  <div class="text-center">
    <img src="/src/assets/RiseLogo.png" style="max-width: 8%" class="mb-4 mt-5" alt="NJ Rise logo">
    
    <h4 class="mb-5">Log in to Staff Dashboard </h4>    
  </div>

  <form>
    <div class="form-group">
      <input type="email" class="form-control" id="InputEmail" aria-describedby="emailHelp" placeholder="Email">
    </div>
    <div class="form-group">
      <input type="password" class="form-control" id="InputPwd" placeholder="Password">
      <a class="small float-right" for="InputPwd">Forget your password?</a>
    </div>

    <div class="text-center">
      <button type="submit" class="btn btn-primary mt-4">Log In</button>
    </div>
  </form>
</template>

<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>
