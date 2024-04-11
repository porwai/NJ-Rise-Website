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
          />
        </div>
      </div>
    </div>
  </main>
</template>


<script>
export default {
  components: {
    DataTable, 
    UserDetails
  },
  data() {
    return {
      curr_details: {Por : "dfs"}
    };
  }, 
  methods: {
    handleNewClient(newDetails) {
      this.curr_details = newDetails; // Updating the prop value based on child's request
    }
  }
}
</script>