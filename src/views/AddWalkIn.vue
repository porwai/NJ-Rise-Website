<template>
  <br>
  <div class="card">
      <div class="card-body d-flex flex-column" style="overflow-y: auto;">
          <h1 class="card-title">Add Walk-In Client and First Visit Information</h1>
          <form @submit.prevent="submitForm" v-if="!formSubmitted">
              <div class="mb-3">
                  <label for="firstname" class="form-label">First Name<span class="required-asterisk">*</span></label>
                  <input 
                    v-model="firstname"
                    type="text"
                    class="form-control"
                    id="firstname"
                    placeholder="Enter your first name" 
                    required
                  />
              </div>
              <div class="mb-3">
                  <label for="lastname" class="form-label">Last Name<span class="required-asterisk">*</span></label>
                  <input 
                    v-model="lastname"
                    type="text"
                    class="form-control"
                    id="lastname"
                    placeholder="Enter your last name" 
                    required
                  />
              </div>
              <div class="mb-3">
                  <label for="dob" class="form-label">Date of Birth<span class="required-asterisk">*</span></label>
                  <input 
                    type="date" 
                    v-model="dob" 
                    class="form-control"
                    id="dob"
                    required
                  />
              </div>
              <div class="mb-3">
                  <label for="phonenumber" class="form-label">Phone Number<span class="required-asterisk">*</span></label>
                  <input 
                    v-model="phonenumber" 
                    type="tel" 
                    class="form-control"
                    id="phonenumber"
                    required
                    @input="formatPhoneNumber"
                  />
              </div>
              <div class="mb-3">
                  <label for="date" class="form-label">Date</label>
                  <input 
                    type="date" 
                    v-model="date" 
                    class="form-control"
                    id="date"
                  />
              </div>
              <div class="mb-3">
                  <label for="foodbags" class="form-label">Food Bags</label>
                  <input 
                    type="number" 
                    min = "0" 
                    oninput="validity.valid||(value='');"
                    v-model="foodbags" 
                    class="form-control"
                    id="foodbags"
                  />
              </div>
              
              <button class="btn btn-primary" type="submit">Submit</button>
          </form>
      </div>
      <div v-if="formSubmitted" class="card-footer">
          <h3 class="card-title">Form Submitted</h3>
          <p>First Name: {{ firstname }}</p>
          <p>Last Name: {{ lastname }}</p>
          <p>DOB: {{ dob }}</p>
          <p>Phone Number: {{ phonenumber }}</p>
          <p>Date: {{ date }}</p>
          <p>Foodbags: {{ foodbags }}</p>
          <small><router-link to="/search">Click here to go back to Client Search.</router-link></small>
      </div>
  </div>
</template>

  <script>
    import axios from 'axios';

    export default {
      name: 'addwalkin',
      data() {
        return {
          firstname: "",
          lastname: "",
          dob: "",
          phonenumber: "",
          date: new Date().toISOString().slice(0,10),
          foodbags: "",
          formSubmitted: false
        };
      },
      methods: {
        submitForm: function () {
          const payload = {
                    first_name: this.firstname,
                    last_name: this.lastname,
                    phone: this.phonenumber,
                    dob: this.dob,
                    date:this.date,
                    foodbags:this.foodbags
                };
          this.addClients(payload);
        },
        addClients(payload) {
                axios.post('/api/add', payload)
                .then((response) => {
                  const output = response.data;
                  if (output[0] !== true){
                    alert(output[1]);
                  }
                  else {
                    this.formSubmitted = true
                  }
                }).catch((error) => {
                    console.error(error);
                    // Consider adding user-facing error handling here
                });
            },
        formatPhoneNumber() {
          let numbers = this.phonenumber.replace(/[^\d]/g, '');
          if (numbers.length > 3) {
            numbers = numbers.substring(0, 3) + '-' + numbers.substring(3);
          }
          if (numbers.length > 7) {
            numbers = numbers.substring(0, 7) + '-' + numbers.substring(7);
          }
          if (numbers.length > 12) {
            numbers = numbers.substring(0, 12);
          }
          this.phonenumber = numbers;
        }
      },
    };
  </script>

  <style>
  .required-asterisk {
  color: red;
}
</style>
