<script setup>
import { ref } from 'vue';
import UserDetails from '../components/UserDetails.vue'
import DataTable from '../components/DataTable.vue'

const showDetails = ref(false);

function UserDetailScreen() {
  showDetails.value = !showDetails.value; // Toggle visibility of UserDetails
}
</script>

<template>
  <main>
    <div class="container-fluid">
      <div class="row">
        
        <!-- Utilize computed classes for column sizes based on showDetails prop -->
        <div :class="showDetails ? 'col' : 'col-sm-12'">
          <DataTable
            @new-client-request="handleNewClient"
            :show-details="showDetails"
            @toggle-details="UserDetailScreen"
          />
        </div>

        <!-- Conditional rendering for UserDetails component -->
        <div class="col-sm-6" v-if="showDetails">
          <UserDetails 
            v-bind:curr_details="curr_details"
            @toggle-details="UserDetailScreen"
            v-bind:curr_history="curr_history"
            @get-history="getClientHistory"
          />
        </div>
      </div>
    </div>
  </main>
</template>


<script>
import axios from 'axios';

export default {
  components: {
    DataTable, 
    UserDetails
  },
  data() {
    return {
      curr_details: {}, 
      curr_history: []
    };
  }, 
  methods: {
    handleNewClient(newDetails) {
      this.curr_details = newDetails; // Updating the prop value based on child's request
      this.getClientHistory();
    }, 
    getClientHistory() {
      const payload = {
        transactional_id: this.curr_details.transactional_id,
      };
      axios.post('http://127.0.0.1:5000/api/history', payload)
      .then((response) => {
        this.curr_history = response.data;
      }).catch((error) => {
        console.error(error);
        // Consider adding user-facing error handling here
      });
    }
  }
}
</script>