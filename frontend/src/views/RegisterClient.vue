<template>
    <br>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
            <h1 class="card-title">Register New Client</h1>
            <form @submit.prevent="handleSubmit">
                <div v-for="(field, key) in formData" :key="key" class="form-group">
                    <label :for="key">{{ formatLabel(key) }}</label>
                    
                    <input v-if="field.type === 'string'"
                        :id="key"
                        class="form-control"
                        type="text"
                        v-model="field.value" />

                    <input v-if="field.type === 'number'"
                        :id="key"
                        class="form-control"
                        type="number"
                        v-model="field.value" />
                        
                    <input v-if="field.type === 'date'"
                        :id="key"
                        class="form-control"
                        type="date"
                        v-model="field.value" />
                    
                    <div class="form-check">
                        <input v-if="field.type === 'checkbox'"
                                :id="key"
                                type="checkbox"
                                class="form-check-input"
                                v-model="field.value" />
                    </div>
                    
                    <select v-if="field.type === 'dropdown'"
                            :id="key"
                            class="form-control"
                            v-model="field.value">
                    <option v-for="option in field.options" :key="option">{{ option }}</option>
                    </select>
                    
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        <div v-if="formSubmitted" class="card-footer">
            <h3 class="card-title">Form Submitted</h3>
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
      import axios from 'axios';
  
      export default {
        name: 'addwalkin',
        data() {
          return {
            formData: {
                case_manager_initials: { value: "", type: "string" },
                date: { value: "", type: "date" },
                client_status: { value: "", type: "dropdown", options: ["New Client", "Renew"] },
                tefap: { value: false, type: "checkbox" },
                empower: { value: false, type: "checkbox" },
                inhouse_file: { value: false, type: "checkbox" },
                tefap_qualifying_code: { value: "", type: "string" },
                last_name: { value: "", type: "string" },
                first_name: { value: "", type: "string" },
                middle_initial: { value: "", type: "string" },
                gender_head_of_household: { value: "", type: "string" },
                dob_head_of_household: { value: "", type: "date" },
                total_adults: { value: 0, type: "number" },
                total_children: { value: 0, type: "number" },
                total_overall: { value: 0, type: "number" },
                additional_members: { value: [], type: "complex" }, // Complex type for handling nested data
                address: { value: "", type: "string" },
                city: { value: "", type: "string" },
                state: { value: "", type: "string" },
                zip: { value: "", type: "string" },
                country_of_origin: { value: "", type: "string" },
                city_town: { value: "", type: "dropdown", options: ["HIGHTSTOWN", "EAST WINDSOR", "CRANBURY", "Other"] },
                housing: { value: "", type: "dropdown", options: ["Own", "Rent", "Other Permanent Housing", "Homeless", "Other", "Unknown / Not reported"] },
                date_file_opened: { value: "", type: "date" },
                intake_date_fy22_23: { value: "", type: "date" },
                email: { value: "", type: "string" },
                phone: { value: "", type: "string" },
                affected_by_covid: { value: false, type: "checkbox" },
                household_level_characteristics: { value: "", type: "dropdown", options: ["Single Person", "Two Adults NO Children", "Single Parent Female", "Single Parent Male", "Two Parent Household", "Non-related Adults with Children", "Multi-Generational Household", "Other", "Unknown/Not Reported"] }
                },
            formSubmitted: false
          };
        },
        methods: {
          submitForm: function () {
            this.formSubmitted = true
            const payload = {
                      first_name: this.firstname,
                      last_name: this.lastname,
                      phone: this.phonenumber,
                      dob: this.dob,
                      date:this.date,
                      foodbags:this.foodbags
                  };
            this.addClients(payload);
          },
          addClients(payload) {
                  axios.post('/api/add', payload)
                  .then(() => {
                  }).catch((error) => {
                      console.error(error);
                      // Consider adding user-facing error handling here
                  });
        }, 
        formatLabel(label) {
            return label
            .replace(/_/g, ' ')    // Replace all underscores with spaces
            .replace(/\b\w/g, c => c.toUpperCase()); // Capitalize the first letter of each word
        }
        },
      };
    </script>
  