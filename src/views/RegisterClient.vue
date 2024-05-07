<template>
    <br>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
            <h1 class="card-title">Register New Client</h1>
            <form v-if="!formSubmitted" @submit.prevent="submitForm">
                <div v-for="(field, key) in formData" :key="key" class="form-group">
                    <label :for="key">{{ formatLabel(key) }}<span v-if="field.required" class="required-asterisk">*</span></label>
                    
                    <input v-if="field.type === 'string'"
                        :id="key"
                        class="form-control"
                        type="text"
                        v-model="field.value"
                        :required="field.required" />

                    <input v-if="field.type === 'phone'"
                        :id="key"
                        class="form-control"
                        type="text"
                        v-model="field.value"
                        :required="field.required"
                        @input="formatPhoneNumber" />

                    <input v-if="field.type === 'number'"
                        :id="key"
                        class="form-control"
                        type="number"
                        v-model="field.value"
                        :required="field.required" />
                        
                    <input v-if="field.type === 'date'"
                        :id="key"
                        class="form-control"
                        type="date"
                        v-model="field.value"
                        :required="field.required" />
                    
                    <div v-if="field.type === 'checkbox'" class="form-check">
                        <input :id="key" type="checkbox" class="form-check-input" v-model="field.value">
                        <label class="form-check-label" :for="key">{{ field.label || 'Check this option' }}</label>
                    </div>
                    
                    <select v-if="field.type === 'dropdown'"
                            :id="key"
                            class="custom-select mr-sm-2"
                            v-model="field.value"
                            :required="field.required">
                    <option v-for="option in field.options" :key="option">{{ option }}</option>
              
                    </select>
                    
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        <div v-if="formSubmitted" class="card-footer">
            <h3 class="card-title">Form Submitted</h3>
            <p>First Name: {{ formData.first_name.value }}</p>
            <p>Last Name: {{ formData.last_name.value }}</p>
            <p>DOB: {{ formData.head_of_household_date_of_birth.value }}</p>
            <p>Phone Number: {{ formData.phone_number.value }}</p>
            <p>Client ID: {{ formData.client_id.value }}</p>
            <!-- <p>Email: {{ email }}</p> -->
            <!-- <p>Date: {{ date }}</p> -->
            <!-- <p>Foodbags: {{ foodbags }}</p> -->
            <small><router-link to="/search">Click here to go back to Client Search.</router-link></small>
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
              "client_id": {"value": "", "type": "string", "required": "true"},
              "last_name": {"value": "", "type": "string", "required": "true"},
              "first_name": {"value": "", "type": "string", "required": "true"},
              "middle_initial": {"value": "", "type": "string"},
              "total_family_members": {"value": 0, "type": "number"},
              "case_manager_initials": {"value": "", "type": "string"},
              "client_type": {"value": "", "type": "dropdown", "options": ["not eligible", "Empower", "TEFAP", "Neighbor"], "required": "true"},
              "renewal_date": {"value": "", "type": "date"},
              "gender_head_of_household": {"value": "", "type": "string"},
              "head_of_household_date_of_birth": {"value": "", "type": "date", "required": "true"},
              "household_number_of_adults": {"value": 0, "type": "number"},
              "household_number_of_children": {"value": 0, "type": "number"},
              "household_number_of_children_under_18": {"value": 0, "type": "number"},
              "additional_family_members_first_name": {"value": "", "type": "string"},
              "additional_family_members_last_name": {"value": "", "type": "string"},
              "additional_family_member_middle_initial": {"value": "", "type": "string"},
              "additional_family_members_date_of_birth": {"value": "", "type": "date"},
              "city": {"value": "", "type": "string"},
              "state": {"value": "", "type": "string"},
              "zip_code": {"value": "", "type": "string"},
              "country_of_origin": {"value": "", "type": "string"},
              "residence_hightstown": {"value": 0, "type": "number"},
              "residence_east_windsor": {"value": 0, "type": "number"},
              "residence_cranbury": {"value": 0, "type": "number"},
              "residence_other": {"value": 0, "type": "number"},
              "housing_own": {"value": 0, "type": "number"},
              "housing_rent": {"value": 0, "type": "number"},
              "housing_other_permanent": {"value": 0, "type": "number"},
              "homeless": {"value": 0, "type": "number"},
              "date_file_opened": {"value": "", "type": "date"},
              "renewal_return_date": {"value": "", "type": "date"},
              "return_client": {"value": 0, "type": "number"},
              "new_client": {"value": 0, "type": "number"},
              "new_client_intake_date": {"value": "", "type": "date"},
              "phone_number": {"value": "", "type": "phone", "required": "true"},
              "affected_by_covid": {"value": 0, "type": "number"},
              "household_single": {"value": 0, "type": "number"},
              "household_two_adults_no_children": {"value": 0, "type": "number"},
              "household_single_parent_female": {"value": 0, "type": "number"},
              "household_single_parent_male": {"value": 0, "type": "number"},
              "household_two_parent": {"value": 0, "type": "number"},
              "household_non_related_adults_no_children": {"value": 0, "type": "number"},
              "household_multi_generational": {"value": 0, "type": "number"},
              "household_other": {"value": 0, "type": "number"},
              "household_not_reported": {"value": 0, "type": "number"},
              "ethnicity_hispanic_latino": {"value": 0, "type": "number"},
              "ethnicity_non_hispanic_latino": {"value": 0, "type": "number"},
              "ethnicity_unknown": {"value": 0, "type": "number"},
              "ethnicity_american_indian": {"value": 0, "type": "number"},
              "ethnicity_alaska_native": {"value": 0, "type": "number"},
              "ethnicity_asian": {"value": 0, "type": "number"},
              "ethnicity_black_african": {"value": 0, "type": "number"},
              "ethnicity_white": {"value": 0, "type": "number"},
              "ethnicity_other": {"value": 0, "type": "number"},
              "ethnicity_multi_race": {"value": 0, "type": "number"},
              "ethnicity_unknown_not_reported": {"value": 0, "type": "number"},
              "adults_in_household_female": {"value": 0, "type": "number"},
              "adults_in_household_pregnant_female": {"value": 0, "type": "number"},
              "adults_in_household_pregnant_due_date": {"value": "", "type": "date"},
              "adults_in_household_male": {"value": 0, "type": "number"},
              "adults_in_household_other": {"value": 0, "type": "number"},
              "adults_in_household_unknown_not_reported": {"value": 0, "type": "number"},
              "adults_in_household_disabled": {"value": 0, "type": "number"},
              "adults_in_household_aged": {"value": 0, "type": "number"},
              "adults_in_household_veteran": {"value": 0, "type": "number"},
              "adults_in_household_veteran_active": {"value": 0, "type": "number"},
              "household_total_number_of_children": {"value": 0, "type": "number"},
              "household_total_number_of_female_children": {"value": 0, "type": "number"},
              "household_total_number_of_male_children": {"value": 0, "type": "number"},
              "household_total_number_of_disabled_children": {"value": 0, "type": "number"},
              "household_children_0_5_years_old": {"value": 0, "type": "number"},
              "household_children_6_13_years_old": {"value": 0, "type": "number"},
              "household_children_14_17_years_old": {"value": 0, "type": "number"},
              "education_9_12_grade_non_graduate": {"value": 0, "type": "number"},
              "education_graduate_or_equivalent_diploma": {"value": 0, "type": "number"},
              "education_12th_grade_and_some_post_secondary_school": {"value": 0, "type": "number"},
              "education_2_4_year_college_graduate": {"value": 0, "type": "number"},
              "education_graduate_and_post_secondary_school": {"value": 0, "type": "number"},
              "education_graduate_and_post_secondary_school_over_25_years_old": {"value": 0, "type": "number"},
              "annual_income": {"value": '0', "type": "string"},
              "full_time_employment": {"value": 0, "type": "number"},
              "part_time_employment": {"value": 0, "type": "number"},
              "migrant_or_seasonal_worker": {"value": 0, "type": "number"},
              "unemployed_short_term_6_months_or_less": {"value": 0, "type": "number"},
              "unemployed_long_term_over_6_months": {"value": 0, "type": "number"},
              "not_in_labor_force": {"value": 0, "type": "number"},
              "retired": {"value": 0, "type": "number"},
              "unknown_or_not_reported_employment": {"value": 0, "type": "number"},
              "obtained_job_through_rise": {"value": 0, "type": "number"},
              "poverty_guidelines_125": {"value": 0, "type": "number"},
              "poverty_guidelines_185": {"value": 0, "type": "number"},
              "poverty_guidelines_200": {"value": 0, "type": "number"},
              "poverty_guidelines_over_200": {"value": 0, "type": "number"},
              "total_family_receiving_fs_snap": {"value": 0, "type": "number"},
              "total_family_receiving_tanf": {"value": 0, "type": "number"},
              "total_family_receiving_alimony": {"value": 0, "type": "number"},
              "total_family_receiving_lheap": {"value": 0, "type": "number"},
              "total_family_receiving_ga": {"value": 0, "type": "number"},
              "total_family_receiving_medicaid_njfc": {"value": 0, "type": "number"},
              "total_family_receiving_child_support": {"value": 0, "type": "number"},
              "total_family_receiving_pension": {"value": 0, "type": "number"},
              "total_family_receiving_ssa": {"value": 0, "type": "number"},
              "total_family_receiving_ssi": {"value": 0, "type": "number"},
              "total_family_receiving_ssdi": {"value": 0, "type": "number"},
              "total_family_receiving_wic": {"value": 0, "type": "number"},
              "total_family_receiving_workers_comp": {"value": 0, "type": "number"},
              "total_family_receiving_temporary_disability": {"value": 0, "type": "number"},
              "total_family_receiving_unemployment": {"value": 0, "type": "number"}
          },
            formSubmitted: false
          };
        },
        methods: {
          submitForm: function () {
            if (this.$store.state.login_status === "not_authorized") {
              console.log("FALSE LOGIN")
              this.$router.push({ path: '/login'})
            }
            if (this.$store.state.viewing_status !== "admin") {
              alert("You must be an admin to query the master database.");
              return;
            }
            this.formSubmitted = true
            const payload = {};
            for (const key in this.formData) {
                if (this.formData.hasOwnProperty(key)) {
                  payload[key] = this.formData[key].value;
                }
            }
            this.registerNewClient(payload);
          },
          registerNewClient(payload) {
                  axios.post('/api/register_new_client', payload)
                  .then(() => {
                  }).catch((error) => {
                      console.error(error);
                      alert('Error: Failed to register client. Please try again.' + error)
                      // Consider adding user-facing error handling here
                  });
        }, 
        formatPhoneNumber() {
          let numbers = this.formData["phone_number"].value.replace(/[^\d]/g, '');
          if (numbers.length > 3) {
            numbers = numbers.substring(0, 3) + '-' + numbers.substring(3);
          }
          if (numbers.length > 7) {
            numbers = numbers.substring(0, 7) + '-' + numbers.substring(7);
          }
          if (numbers.length > 12) {
            numbers = numbers.substring(0, 12);
          }
          this.formData["phone_number"].value = numbers;
        },
        formatLabel(label) {
            return label
            .replace(/_/g, ' ')    // Replace all underscores with spaces
            .replace(/\b\w/g, c => c.toUpperCase()); // Capitalize the first letter of each word
        }
        },
      };
    </script>

    <style>
    .required-asterisk {
    color: red;
  }
  </style>