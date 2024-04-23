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
    <!-- Desktop view -->
    <div class="container-fluid" v-if="!isMobile">
      <div class="row">
        <!-- Utilize computed classes for column sizes based on showDetails prop -->
        <div :class="showDetails ? 'col-6' : 'col-12'">
          <DataTable
            @new-client-request="handleNewClient"
            :show-details="showDetails"
            @toggle-details="UserDetailScreen"
          />
        </div>
        <!-- Conditional rendering for UserDetails component -->
        <div class="col-6" v-if="showDetails">
          <UserDetails 
            v-bind:curr_details="curr_details"
            @toggle-details="UserDetailScreen"
            v-bind:curr_history="curr_history"
            @get-history="getClientHistory"
          />
        </div>
      </div>
    </div>
    <!-- Mobile view -->
    <div class="container-fluid" v-else>
      <div class="row">

        <!-- Utilize computed classes for column sizes based on showDetails prop -->
        <div class="col" v-if="!showDetails">
          <DataTable
            @new-client-request="handleNewClient"
            :show-details="showDetails"
            @toggle-details="UserDetailScreen"
          />
        </div>
        <!-- Conditional rendering for UserDetails component -->
        <div class="col" v-if="showDetails">
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
      curr_history: [{
    "visit_date": "April 18, 2024",
    "food_bags": 3,
    "baby_supplies": 2,
    "cleaning": 1,
    "gift_items": 5,
    "personal_care": 4,
    "pet_food": 2,
    "pj": 1,
    "summer_feeding": 3,
    "winter": 4,
    "other": "Various items"
}], 
      isMobile: false
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
      console.log(this.isMobile)
    }
  }
}
</script>