<!-- Login.vue -->

<script setup>

// console.log(this.$store.state.count)
// console.log($testglobal)

</script>
<template>
  <div class="card">
    <div class="card-body">
      <div class="text-center">
        <img src="/src/assets/RiseLogo.png" style="max-width: 8%" class="mb-4 mt-5" alt="NJ Rise logo">
        <h4 class="mb-5">Log in to Staff Dashboard</h4>
      </div>

      <form class="col-lg-4 offset-lg-4" @submit.prevent="submitData">
        <div class="form-group">
          <input type="username" v-model="formData.username" class="form-control" id="InputUsername" placeholder="Username">
        </div>

        <div class="form-group">
          <input type="password" v-model="formData.password" class="form-control" id="InputPwd" placeholder="Password">
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

<script>

import {sha256} from 'crypto-hash';

console.log('test 1');
export default {
  data() {
    console.log('test 2');
    return {
      formData: {
        username: "",
        password: "",
      },
      responseData: null
    };
  },
  methods: {
    async submitData() {

      // Hashing password with SHA 256
      let payload = {
        "username": this.formData.username,
        "password": await sha256(this.formData.password)
      };

      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
      });
      const responseData = await response.json();
      console.log(responseData["status"]);

      if (responseData["status"] == true) {
        // console.log("reached true login")
        if (responseData["role"] == "admin"){
          console.log("set to admin privelege")
          console.log(this.$store.state.login_status)
          this.$store.commit('log_in_admin')
          console.log(this.$store.state.login_status)
        }
        else if (responseData["role"] == "volunteer"){
          console.log("set to volunteer privelege")
          console.log(this.$store.state.login_status)
          this.$store.commit('log_in_volunteer')
        }
        else{
          this.formData.password = ""

        }
        
        this.$router.push({ path: '/search'})
      }


    }
  }
};
</script>