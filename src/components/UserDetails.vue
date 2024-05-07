<script setup>
import EditMasterDBmodal from './editMasterDBmodal.vue';
</script>

<template>
	<div class="card full-height full-width">
	  <div class="card-header d-flex justify-content-end">
      <button type="button" class="close" aria-label="Close" @click="closeCard" style="border: none; background-color: white;">
		  <span aria-hidden="true">&times;</span>
		</button>
	  </div>
    <!-- card body -->
	  <div class="card-body d-flex flex-column" style="overflow-y: auto;">
      
      <div class="row align-items-center justify-content-between">
        <div class="col">
          <h1>{{curr_details.first_name + " " + curr_details.last_name}}</h1>
        </div>
        <div class="col-auto">
          <EditMasterDBmodal 
          v-if="masterDBView == true" 
          :curr_details="curr_details"
          @query-database="$emit('query-database')"
          @update-currdetails="handleUpdateClientDetails"
          />
        </div>
      </div>
      
      <div class="row">
        <div class="table-responsive" style="max-height: 35vh; overflow-y: auto;">
              <table class="table table-striped table-bordered">
                  <tbody>
                    <template v-for="(value, key) in curr_details" :key="key">
                      <tr v-if="key !== 'transactional_id'">
                          <th style="white-space: nowrap;">{{ formatKey(key) }}</th>
                          <td>{{ value }}</td>
                      </tr>
                    </template>
                  </tbody>
              </table>
        </div>
      </div>
        
      <div class="row">
      <h1>Visit History</h1>
      <!-- Table -->
      <div class="table-responsive">
      <table class="table table-bordered table-hover">
          <thead>
              <tr>
                <th class="rotate visit-date" scope="col"><div><span>visit date</span></div></th>
                <th class="rotate food-bags" scope="col"><div><span>food bags</span></div></th>
                <th class="rotate baby-supplies" scope="col"><div><span>baby supplies</span></div></th>
                <th class="rotate cleaning" scope="col"><div><span>cleaning</span></div></th>
                <th class="rotate gift-items" scope="col"><div><span>gift items</span></div></th>
                <th class="rotate personal-care" scope="col"><div><span>personal care</span></div></th>
                <th class="rotate pet-food" scope="col"><div><span>pet food</span></div></th>
                <th class="rotate pj" scope="col"><div><span>pj</span></div></th>
                <th class="rotate clothing" scope="col"><div><span>clothing</span></div></th>
                <th class="rotate summer-feeding" scope="col"><div><span>summer feeding</span></div></th>
                <th class="rotate winter" scope="col"><div><span>winter</span></div></th>
                <th class="rotate other" scope="col"><div><span>other</span></div></th>
                <th class="actions" scope="col"></th>              </tr>
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
                  <td>{{ visit_date.clothing }}</td>
                  <td>{{ visit_date.summer_feeding }}</td>
                  <td>{{ visit_date.winter }}</td>
                  <td>{{ visit_date.other }}</td>
                  <td>
                    <a class="delete" title="Delete" @click="handleVisitHistoryDelete(visit_date.t_id, visit_date.visit_id)"><i class="fas fa-trash mr-1"></i></a>
                  </td>
              </tr>
          </tbody>
      </table>
      </div>

      <!-- Button to Open the Modal -->
      <button type="button" class="btn btn-success" data-toggle="modal" data-target="#newVisit">
        Add New Visit
      </button>
      </div>

      <!-- The Modal -->
    <div class="modal" id="newVisit">
    <div class="modal-dialog">
      <div class="modal-content">

        <!-- Modal Header -->
        <div class="modal-header">
          <h4 class="modal-title">Add New Visit</h4>
          <button type="button" class="close" data-dismiss="modal" ref="closeModalButton" @click="clearInputForm()">&times;</button>
        </div>

            <!-- Modal Body -->
        <div class="modal-body">
          <form id="visitForm">
            <div class="row">
              <!-- Column 1 -->
              <div class="col-md-6">
                <!-- Date -->
                <div class="form-group">
                  <label for="new_visit_date">Date</label>
                  <input
                  type="date" class="form-control" id="new_visit_date" v-model="new_visit_date" placeholder="">
                </div>

                <!-- Food Bags -->
                <div class="form-group">
                  <label for="foodBags">Food Bags</label>
                  <input
                  type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="foodBags" v-model="f_bags" placeholder="Enter quantity">
                </div>

                <!-- Baby Supplies -->
                <div class="form-group">
                  <label for="babySupplies">Baby Supplies</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="babySupplies" v-model="b_supplies" placeholder="Enter quantity">
                </div>

                <!-- Pet Food -->
                <div class="form-group">
                  <label for="petFood">Pet Food</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="petFood" v-model="p_food" placeholder="Enter quantity">
                </div>

                <!-- Gift Items -->
                <div class="form-group">
                  <label for="giftItems">Gift Items</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="giftItems" v-model="g_items" placeholder="Enter quantity">
                </div>

                <!-- Cleaning Supplies -->
                <div class="form-group">
                  <label for="cleaningSupplies">Cleaning Supplies</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="cleaningSupplies" v-model="c" placeholder="Enter quantity">
                </div>
              </div>

              <!-- Column 2 -->
              <div class="col-md-6">
                <!-- Personal Care -->
                <div class="form-group">
                  <label for="personalCare">Personal Care</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="personalCare" v-model="p_care" placeholder="Enter quantity">
                </div>

                <!-- Summer Feeding -->
                <div class="form-group">
                  <label for="summerFeeding">Summer Feeding</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="summerFeeding" v-model="sf" placeholder="Enter quantity">
                </div>

                <!-- Kids Pajamas -->
                <div class="form-group">
                  <label for="kidsPajamas">Kids Pajamas</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="kidsPajamas" v-model="pj" placeholder="Enter quantity">
                </div>

                <!-- Clothing -->
                <div class="form-group">
                  <label for="clothing">Clothing</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="clothing" v-model="cloth" placeholder="Enter quantity">
                </div>

                <!-- Winter Coats -->
                <div class="form-group">
                  <label for="winterCoats">Winter Coats</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="winterCoats" v-model="w" placeholder="Enter quantity">
                </div>

                <!-- Other Items -->
                <div class="form-group">
                  <label for="otherItems">Other Items</label>
                  <input type="number" class="form-control" min = "0" oninput="validity.valid||(value='');" id="otherItems" v-model="o" placeholder="Describe other items">
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
    <!-- card end -->
	</div>
</template>
  
<style scoped>
  .card-header {
  background-color: white;
  border: none;
  border-bottom: 0; 
  padding-bottom: 0;
  margin-bottom: 0;
  }

  /* Optional: Striped rows for better readability */
  .table-striped > tbody > tr:nth-of-type(odd) {
      background-color: rgba(53, 49, 49, 0.05);
  }

  .table-responsive {
    padding: 0; /* Optional: Adjusts padding inside the container to fit the table neatly */
  }

  table.table td a.edit {
        color: #FFC107;
  }
  table.table td a.delete {
        color: #F44336;
  }

  .visit-date { background-color: #f4cccc; }
  .food-bags { background-color: #fce5cd; }
  .baby-supplies { background-color: #fff2cc; }
  .cleaning { background-color: #d9ead3; }
  .gift-items { background-color: #d0e0e3; }
  .personal-care { background-color: #c9daf8; }
  .pet-food { background-color: #cfe2f3; }
  .pj { background-color: #d9d2e9; }
  .summer-feeding { background-color: #ead1dc; }
  .clothing { background-color: #af16c4; }
  .winter { background-color: #e6b8af; }
  .other { background-color: #f9cb9c; }
  .actions { background-color: #fff; } /* Different color or keep as default */

</style>

<script>
  import axios from 'axios';

  export default {
  components: {
    EditMasterDBmodal
  },
  data() {
      return {
        transactional_id: -1,
        new_visit_date: new Date().toISOString().slice(0,10),
        f_bags: 0,
        b_supplies:0,
        p_food:0,
        g_items:0,
        c: 0,
        sf: 0,
        p_care: 0,
        pj: 0,
        cloth: 0,
        w: 0,
        o: 0, 
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
  computed: { 
    masterDBView() {
      return this.$store.state.master_db_view; // Accessing the state
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
        pj: this.pj,
        cloth: this.cloth,
        w: this.w,
        o: this.o
      };

      axios.post('/api/newdate', payload)
      .then(response => {
        // Updates to show new visit
        const output = response.data
        if (output[0] !== true){
          alert(output[1]);
        }
        else {
          this.$emit('get-history');
          alert("Added New Client Success");  // User-facing error message
        }
        this.$refs.closeModalButton.click();
        this.clearInputForm();
      }).catch(error => {
        console.error(error);
        alert("Failed to add new visit: " + error.message);  // User-facing error message
        this.$refs.closeModalButton.click();
        this.clearInputForm();
      });
    }, 
    formatKey(key) {
      return key.split('_')
                .map(part => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
                .join(' ');
    }, 
    clearInputForm() {
      this.f_bags = 0;
      this.b_supplies = 0;
      this.p_food = 0;
      this.g_items = 0;
      this.c = 0;
      this.sf = 0;
      this.p_care = 0;
      this.pj = 0;
      this.cloth= 0;
      this.w = 0;
      this.o = 0;
    }
    , 
    handleVisitHistoryDelete(transactional_id, visit_id) {
      const payload = {
        transactional_id: transactional_id, 
        visit_id: visit_id
      };
      if (this.$store.state.login_status === "not_authorized") {
        console.log("FALSE LOGIN")
        this.$router.push({ path: '/login'})
        return;
      }
      axios.post('/api/delete_client_visithistory', payload)
      .then((response) => {
        console.log("Deletion successful:", response.data);
        this.$emit('get-history')
        alert("Client Visit History Successfully Deleted!");
      }).catch((error) => {
        console.error("Error deleting client:", error);
        alert("Error Deleting Visit History!");
      });
    },
    handleUpdateClientDetails(payload) {
      this.$emit('update-currdetails', payload);
    } 
	}
  };
</script>
  