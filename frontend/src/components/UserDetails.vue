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
          <tr v-for="(value, key) in curr_details" :key="key">
            <th>{{ key }}</th>
            <td>{{ value }}</td>
          </tr>
        </tbody>
    </table>

    <h1>Visit History</h1>

    <table class="table">
        <tbody>
          <tr v-for="(value, key) in curr_details" :key="key">
            <th>{{ key }}</th>
            <td>{{ value }}</td>
          </tr>
        </tbody>
    </table>

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
        <form>
          <div class="row">
            <!-- Column 1 -->
            <div class="col-md-6">
              <!-- Food Bags -->
              <div class="form-group">
                <label for="foodBags">Food Bags</label>
                <input type="number" class="form-control" id="foodBags" placeholder="Enter quantity">
              </div>

              <!-- Baby Supplies -->
              <div class="form-group">
                <label for="babySupplies">Baby Supplies</label>
                <input type="number" class="form-control" id="babySupplies" placeholder="Enter quantity">
              </div>

              <!-- Pet Food -->
              <div class="form-group">
                <label for="petFood">Pet Food</label>
                <input type="number" class="form-control" id="petFood" placeholder="Enter quantity">
              </div>

              <!-- Gift Items -->
              <div class="form-group">
                <label for="giftItems">Gift Items</label>
                <input type="number" class="form-control" id="giftItems" placeholder="Enter quantity">
              </div>

              <!-- Cleaning Supplies -->
              <div class="form-group">
                <label for="cleaningSupplies">Cleaning Supplies</label>
                <input type="number" class="form-control" id="cleaningSupplies" placeholder="Enter quantity">
              </div>
            </div>

            <!-- Column 2 -->
            <div class="col-md-6">
              <!-- Personal Care -->
              <div class="form-group">
                <label for="personalCare">Personal Care</label>
                <input type="number" class="form-control" id="personalCare" placeholder="Enter quantity">
              </div>

              <!-- Summer Feeding -->
              <div class="form-group">
                <label for="summerFeeding">Summer Feeding</label>
                <input type="number" class="form-control" id="summerFeeding" placeholder="Enter quantity">
              </div>

              <!-- Kids Pajamas -->
              <div class="form-group">
                <label for="kidsPajamas">Kids Pajamas</label>
                <input type="number" class="form-control" id="kidsPajamas" placeholder="Enter quantity">
              </div>

              <!-- Clothing -->
              <div class="form-group">
                <label for="clothing">Clothing</label>
                <input type="number" class="form-control" id="clothing" placeholder="Enter quantity">
              </div>

              <!-- Winter Coats -->
              <div class="form-group">
                <label for="winterCoats">Winter Coats</label>
                <input type="number" class="form-control" id="winterCoats" placeholder="Enter quantity">
              </div>

              <!-- Other Items -->
              <div class="form-group">
                <label for="otherItems">Other Items</label>
                <input type="text" class="form-control" id="otherItems" placeholder="Describe other items">
              </div>
            </div>
          </div>
        </form>
      </div>

      <!-- Modal footer -->
      <div class="modal-footer">
        <button type="button" class="btn btn-success" data-dismiss="modal">Add New Visit</button>
      </div>

    </div>
  </div>
</div>

    #yyyy-mm-dd


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
  export default {
    data() {
        return {
            test_data: {"por" : "sdf"}
        };
    },
	name: 'UserDetails',
	props: {
        curr_details: {
            type: Object,
            required: true,
            default: () => ({})  // Provides an empty object by default
        }
    },
	methods: {
	  closeCard() {
		this.$emit('toggle-details')
	  }
	}
  };
  </script>
  