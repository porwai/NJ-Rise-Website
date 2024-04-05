<script setup>
import { ref } from 'vue';
import UserDetails from '../components/UserDetails.vue'
import DataTable from '../components/DataTable.vue'

const showDetails = ref(false);

function receiveDetails() {
  showDetails.value = !showDetails.value;
  console.log(showDetails.value)
}
</script>

<template>
  <main>
    <div class="container-fluid">
        <transition name="fade">
        <div class="row">
          <div :class="showDetails ? 'col-sm-6' : 'col-sm-12'">
            <DataTable @toggle-details="receiveDetails" />
          </div>
          <transition name="slide-fade">
            <div class="col-sm-6" v-if="showDetails">
              <UserDetails />
            </div>
          </transition>
        </div>
      </transition>
    </div>
  </main>
</template>

