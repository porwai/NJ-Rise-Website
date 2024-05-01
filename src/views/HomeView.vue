<script setup>
import { ref } from 'vue';
import UserDetails from '../components/UserDetails.vue'
import DataTable from '../components/DataTable.vue'

const showDetails = ref(false);

function UserDetailScreen() {
  showDetails.value = !showDetails.value; // Toggle visibility of UserDetails
}

function closeDetailsScreen() {
  if (showDetails.value) {
    showDetails.value = !showDetails.value;
  }
}

</script>

<template>
  <main>
    <!-- Desktop view -->
    <div class="container-fluid">
      <div class="row">
        <!-- Utilize computed classes for column sizes based on showDetails prop -->
        <div :class="showDetails ? 'col-6' : 'col-12'" v-if="!showDetails || !isMobile">
          <DataTable
            @new-client-request="handleNewClient"
            :show-details="showDetails"
            @toggle-details="UserDetailScreen"
            @close-details="closeDetailsScreen"
          />
        </div>
        <!-- Conditional rendering for UserDetails component -->
        <div :class="isMobile ? 'col-12' : 'col-6'" v-if="showDetails">
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
      curr_history: [], 
      isMobile: false, 
      showDetails: false
    };
  }, 
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
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
      axios.post('/api/history', payload)
      .then((response) => {
        this.curr_history = response.data;
      }).catch((error) => {
        console.error(error);
        // Consider adding user-facing error handling here
      });
    }, 
    onResize() { // Dynamic Display dependent on whether user is on mobile device
      if(window.innerWidth <= 1400) {
        this.isMobile = true
      } else {
        this.isMobile = false
      }
    }
  }
}
</script>