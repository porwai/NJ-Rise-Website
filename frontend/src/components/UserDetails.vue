<template>
	<br>
	<div class="card h-100 w-100">
	  <div class="card-header">
		<button type="button" class="close" aria-label="Close" @click="closeCard">
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
  