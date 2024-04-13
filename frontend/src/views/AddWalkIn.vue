<template>
  <br>
  <div class="card">
      <div class="card-body">
          <h1 class="card-title">Add Client Information and First Visit Information</h1>
          <form @submit.prevent="submitForm" v-if="!formSubmitted">
              <div class="mb-3">
                  <label for="firstname" class="form-label">First Name</label>
                  <input 
                    v-model="firstname"
                    type="text"
                    class="form-control"
                    id="firstname"
                    placeholder="Enter your first name" 
                  />
              </div>
              <div class="mb-3">
                  <label for="lastname" class="form-label">Last Name</label>
                  <input 
                    v-model="lastname"
                    type="text"
                    class="form-control"
                    id="lastname"
                    placeholder="Enter your last name" 
                  />
              </div>
              <div class="mb-3">
                  <label for="dob" class="form-label">DOB</label>
                  <input 
                    type="date" 
                    v-model="dob" 
                    class="form-control"
                    id="dob"
                  />
              </div>
              <div class="mb-3">
                  <label for="phonenumber" class="form-label">Phone Number</label>
                  <input 
                    v-model="phonenumber" 
                    type="tel" 
                    class="form-control"
                    id="phonenumber"
                  />
              </div>
              <div class="mb-3">
                  <label for="email" class="form-label">Email</label>
                  <input 
                    type="email" 
                    v-model="email" 
                    class="form-control"
                    id="email"
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
          <p>Email: {{ email }}</p>
          <p>Date: {{ date }}</p>
          <p>Foodbags: {{ foodbags }}</p>
          <small>Click on run to launch the app again.</small>
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
          email: "",
          date: "",
          foodbags: "",
          formSubmitted: false
        };
      },
      methods: {
        submitForm: function () {
          this.formSubmitted = true
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
                if (this.$store.state.login_status === false) {
                          console.log("FALSE LOGIN")
                          this.$router.push({ path: '/login'})
                      }
                axios.post('/api/add', payload)
                .then(() => {
                }).catch((error) => {
                    console.error(error);
                    // Consider adding user-facing error handling here
                });
            }
      },
    };
  </script>
