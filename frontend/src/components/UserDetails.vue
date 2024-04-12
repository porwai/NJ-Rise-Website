<template>
	<div class="card h-100 w-100">
	  <div class="card-header d-flex justify-content-end">
      <button type="button" class="close" aria-label="Close" @click="closeCard" style="border: none; background-color: white;">
		  <span aria-hidden="true">&times;</span>
		</button>
	  </div>
	  <div class="card-body d-flex flex-column">
		<h1>{{curr_details.first_name + " " + curr_details.last_name}}</h1>
		<p>Client ID: {{curr_details.client_id}}</p>
        
		<table class="table">
        <tbody>
          <tr v-for="(value, key) in curr_details" :key="key" v-if="key !== 'transactional_id'" >
            <th>{{ key }}</th>
            <td>{{ value }}</td>
          </tr>
        </tbody>
    </table>

    <h1>Visit History</h1>

  <div class="table-responsive">
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>visit date</th>
                <th>food bags</th>
                <th>baby supplies</th>
                <th>cleaning</th>
                <th>gift items</th>
                <th>personal care</th>
                <th>pet food</th>
                <th>pj</th>
                <th>summer feeding</th>
                <th>winter</th>
                <th>other</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="visit_date in curr_history" :key="visit_date.transactional_id">
                <td>{{ visit_date.visit_date }}</td>
                <td>{{ visit_date.food_bags }}</td>
                <td>{{ visit_date.baby_supplies }}</td>
                <td>{{ visit_date.cleaning }}</td>
                <td>{{ visit_date.gift_items }}</td>
                <td>{{ visit_date.personal_care }}</td>
                <td>{{ visit_date.pet_food }}</td>
                <td>{{ visit_date.pj }}</td>
                <td>{{ visit_date.summer_feeding }}</td>
                <td>{{ visit_date.winter }}</td>
                <td>{{ visit_date.other }}</td>
            </tr>
        </tbody>
    </table>
  </div>

    <!-- Button to Open the Modal -->
    <button type="button" class="btn btn-success" data-toggle="modal" data-target="#newVisit">
      Add New Visit
    </button>

    <!-- The Modal -->
<div class="modal" id="newVisit">
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- Modal Header -->
      <div class="modal-header">
        <h4 class="modal-title">Add New Visit</h4>
        <button type="button" class="close" data-dismiss="modal">&times;</button>
      </div>

          <!-- Modal Body -->
      <div class="modal-body">
        <form id="visitForm">
          <div class="row">
            <!-- Column 1 -->
            <div class="col-md-6">
              <!-- Date -->
              <div class="form-group">
                <label for="new_visit_date">Date (yyyy-mm-dd)</label>
                <input type="date" class="form-control" id="new_visit_date" v-model="new_visit_date" placeholder="YYYY-MM-DD">
              </div>

              <!-- Food Bags -->
              <div class="form-group">
                <label for="foodBags">Food Bags</label>
                <input type="number" class="form-control" id="foodBags" v-model="f_bags" placeholder="Enter quantity">
              </div>

              <!-- Baby Supplies -->
              <div class="form-group">
                <label for="babySupplies">Baby Supplies</label>
                <input type="number" class="form-control" id="babySupplies" v-model="b_supplies" placeholder="Enter quantity">
              </div>

              <!-- Pet Food -->
              <div class="form-group">
                <label for="petFood">Pet Food</label>
                <input type="number" class="form-control" id="petFood" v-model="p_food" placeholder="Enter quantity">
              </div>

              <!-- Gift Items -->
              <div class="form-group">
                <label for="giftItems">Gift Items</label>
                <input type="number" class="form-control" id="giftItems" v-model="g_items" placeholder="Enter quantity">
              </div>

              <!-- Cleaning Supplies -->
              <div class="form-group">
                <label for="cleaningSupplies">Cleaning Supplies</label>
                <input type="number" class="form-control" id="cleaningSupplies" v-model="c" placeholder="Enter quantity">
              </div>
            </div>

            <!-- Column 2 -->
            <div class="col-md-6">
              <!-- Personal Care -->
              <div class="form-group">
                <label for="personalCare">Personal Care</label>
                <input type="number" class="form-control" id="personalCare" v-model="p_care" placeholder="Enter quantity">
              </div>

              <!-- Summer Feeding -->
              <div class="form-group">
                <label for="summerFeeding">Summer Feeding</label>
                <input type="number" class="form-control" id="summerFeeding" v-model="sf" placeholder="Enter quantity">
              </div>

              <!-- Kids Pajamas -->
              <div class="form-group">
                <label for="kidsPajamas">Kids Pajamas</label>
                <input type="number" class="form-control" id="kidsPajamas" v-model="pj" placeholder="Enter quantity">
              </div>

              <!-- Clothing -->
              <div class="form-group">
                <label for="clothing">Clothing</label>
                <input type="number" class="form-control" id="clothing" v-model="cloth" placeholder="Enter quantity">
              </div>

              <!-- Winter Coats -->
              <div class="form-group">
                <label for="winterCoats">Winter Coats</label>
                <input type="number" class="form-control" id="winterCoats" v-model="w" placeholder="Enter quantity">
              </div>

              <!-- Other Items -->
              <div class="form-group">
                <label for="otherItems">Other Items</label>
                <input type="text" class="form-control" id="otherItems" v-model="o" placeholder="Describe other items">
              </div>
            </div>
          </div>
        </form>
      </div>
      
      <!-- Modal footer -->
      <div class="modal-footer">
        <button type="button" class="btn btn-success" @click="addNewVisit()">Add New Visit</button>
      </div>

    </div>
  </div>
</div>

</div>
	</div>
  </template>
  
  <style scoped>
  .card {
	min-height: 87vh; /* Make card at least the height of the viewport */
	border-radius: 0.25rem; /* Rounded corners */
  }

  .card-body {
	padding: 1.25rem; /* Appropriate padding */
  }

  .card-header {
  background-color: white;
  border: none;
  border-bottom: 0; 
  padding-bottom: 0;
  margin-bottom: 0;
  }
  </style>

  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        transactional_id: -1,
        new_visit_date: null,
        f_bags: 0,
        b_supplies:0,
        p_food:0,
        g_items:0,
        c: 0,
        sf: 0,
        p_care: 0,
        p: 0,
        cloth: 0,
        w: 0,
        o: 0
      }
    }
  , 
	name: 'UserDetails',
	props: {
        curr_details: {
            type: Object,
            required: true,
            default: () => ({})  // Provides an empty object by default
        }, 
        curr_history: {
          type: Array,
          default: () => []
        }
    },
	methods: {
	  closeCard() {
		this.$emit('toggle-details')
	  }, 
    addNewVisit() {
      // Example of collecting form data
      const form = document.getElementById('visitForm');
      const formData = new FormData(form);
      const payload = {
        transactional_id: this.curr_details.transactional_id,
        new_visit_date: this.new_visit_date,
        f_bags: this.f_bags,
        b_supplies: this.b_supplies,
        p_food: this.p_food,
        g_items: this.g_items,
        c: this.c,
        sf: this.sf,
        p_care: this.p_care,
        p: this.p,
        cloth: this.cloth,
        w: this.w,
        o: this.o
      };

      console.log(payload);

      axios.post('http://127.0.0.1:5000/api/newdate', payload)
      .then(response => {
        // Updates to show new visit
        this.$emit('get-history')
        // Optionally close the modal if everything is fine
      }).catch(error => {
        console.error(error);
        alert("Failed to add new visit: " + error.message);  // User-facing error message
      });
    }
	}
  };
  </script>
  