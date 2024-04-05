<!-- AddWalkIn.vue -->

<!-- <template>
    <div>
      <b-form @submit="onSubmit" v-if="show">
        <b-form-group
          id="first-name-group"
          label="First Name:"
          label-for="first-name"
        >
          <b-form-input
            id="first-name"
            v-model="form.firstname"
            type="text"
            placeholder="Enter first name"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-form-group id="last-name-group" label="Last Name:" label-for="last-name">
          <b-form-input
            id="last-name"
            v-model="form.lastname"
            placeholder="Enter last name"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-form-group id="dob-group" label="DOB:" label-for="dob">
          <b-form-select
            id="dob"
            v-model="form.dob"
            placeholder="Enter dob in MM/DD/YYYY format"
            required
          ></b-form-select>
        </b-form-group>
  
        <b-form-group id="phone-number-group" label="Phone Number:" label-for="phone-number">
          <b-form-input
            id="phone-number"
            v-model="form.phonenumber"
            placeholder="Enter phone number in format XXX-XXX-XXXX"
            required
          ></b-form-input>
        </b-form-group>
  
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </div>
  </template>
  
  <script>
    export default {
      data() {
        return {
          form: {
            email: '',
            name: '',
            food: null,
            checked: []
          },
          show: true
        }
      },
      methods: {
        onSubmit(event) {
          event.preventDefault()
          alert(JSON.stringify(this.form))
        },
        onReset(event) {
          event.preventDefault()
          // Reset our form values
          this.form.firstname = ''
          this.form.lastname = ''
          this.form.dob = ''
          this.form.checked = []
          // Trick to reset/clear native browser form validation state
          this.show = false
          this.$nextTick(() => {
            this.show = true
          })
        }
      }
    }
  </script> -->


<template>
    <div>
        <h1>Add Client Information and First Visit Information</h1>
      <form @submit.prevent="submitForm" v-if="!formSubmitted">
        <span>First Name</span><br>
        <input 
          v-model="firstname"
          type="text"
          placeholder="Enter your first name" 
        /><br>
        <span>Last Name</span><br>
        <input 
          v-model="lastname"
          type="text"
          placeholder="Enter your last name" 
        /><br>
        <span>DOB</span><br>
        <input 
          type="date" 
          v-model="dob" 
          value="Enter your date of birth" 
        /><br>
        <span>Phone Number</span><br>
        <input 
          v-model="phonenumber" 
          type="tel" 
          value="Enter your phone number" 
        /><br>
        <span>Email</span><br>
        <input 
          type="email" 
          v-model="email" 
          value="Enter your email" 
        /><br>
        <span>Date</span><br>
        <input 
          type="date" 
          v-model="date" 
          value="Enter the date the client walked in." 
        /><br>
        <span>Food Bags</span><br>
        <input 
          type="number" 
          v-model="foodbags" 
          value="Enter the number of food bags the client received." 
        /><br>
        
        <input 
          class="submit" 
          type="submit" 
          value="Submit"
        >
      </form>
      <div v-if="formSubmitted">
        <h3>Form Submitted</h3>
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
        }
      },
    };
  </script>
  <style>
    form {
      padding: 10px;
      border: 2px solid black;
      border-radius: 5px;
    }
  
    input {
      padding: 4px 8px;
      margin: 4px;
    }
  
    span {
      font-size: 18px;
      margin: 4px;
      font-weight: 500;
    }
  
    .submit {
      font-size: 15px;
      color: #fff;
      background: #222;
      padding: 6px 12px;
      border: none;
      margin-top: 8px;
      cursor: pointer;
      border-radius: 5px;
    }
  
  </style>



<!-- <template>
    <h2>Add Client Information</h2>
    <div class = "container-fluid">
        <h1>John Doe</h1>
        <h2>123456789</h2>
        <div class = "table-responsive" style="max-height: 300px; overflow-y: scroll;">


<b-table class = "table table-striped">
    <tbody>
        <tr v-for="detail in details" :key="detail.clientid">
            <td><b> phone </b></td>
            <td> {{detail.phone}} </td>
        </tr>
        <tr v-for="detail in details" :key="detail.clientid">
            <td><b> dependents </b></td>
            <td> {{detail.dependents}} </td>
        </tr>
    </tbody>
</b-table>
</div>

<h2>Visitation Log</h2>
        <div class = "table-responsive" style="max-height: 300px; overflow-y: scroll;">

        <b-table class ="table table-striped">
            <thead>
                <tr>
                    <th>Date/Time</th>
                    <th>Weekday</th>
                    <th>Food Bags</th>
                    <th>Baby Supplies</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="client in clients" :key="client.clientid">
                    <td> {{ client.date }}</td>
                    <td> {{ client.weekday }}</td>
                    <td> {{ client.foodbags }}</td>
                </tr>
            </tbody>
        </b-table>
    </div>
    </div>
</template>

<script>
    export default {
        name: 'userdetails',
        data() {
            return {
                details: [
                    {phone: '019283', dependents: 'wed'}
                ],
                clients: [
                    {date: '019283', weekday: 'wed', foodbags: '5'},
                    {date: '019283', weekday: 'wed', foodbags: '5'},
                    {date: '019283', weekday: 'wed', foodbags: '5'}
                ],
            };
        },
    }
</script> -->