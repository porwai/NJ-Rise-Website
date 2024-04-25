<template>
    <br>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
            <h1 class="card-title">Monthly Empower Report</h1>
            <h2> Select Month of Empower Report</h2>
            <form @submit.prevent="submitForm1">
                <select v-model="selected">
                    <option disabled value="">Please select one</option>
                    <option value = 1>January</option>
                    <option value = 2>February</option>
                    <option value = 3>March</option>
                    <option value = 4>April</option>
                    <option value = 5>May</option>
                    <option value = 6>June</option>
                    <option value = 7>July</option>
                    <option value = 8>August</option>
                    <option value = 9>September</option>
                    <option value = 10>October</option>
                    <option value = 11>November</option>
                    <option value = 12>December</option>
                </select>
                <br>
                <div class="mb-3">
                  <label for="year" class="form-label">Year</label>
                  <input 
                    v-model="year" 
                    type="number" 
                    class="form-control"
                    id="year"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
          <h1 class="card-title"> Yearly Summary Report</h1>
            <h2> Select Year</h2>
            <form @submit.prevent="submitForm2">
                <div class="mb-3">
                  <label for="year2" class="form-label">Year</label>
                  <input 
                    v-model="year2" 
                    type="number" 
                    class="form-control"
                    id="year2"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
          </form>
          <h1 class="card-title"> Walk In Summary Report</h1>
            <h2> Select Year</h2>
            <form @submit.prevent="submitForm3">
                <div class="mb-3">
                  <label for="year3" class="form-label">Year</label>
                  <input 
                    v-model="year3" 
                    type="number" 
                    class="form-control"
                    id="year3"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        </div>
    </div>
  </template>
  
    <script>
      import axios from 'axios';
  
      export default {
        name: 'reports',
        data() {
          return {
            selected: null,
            year:0,
            year2:0,
          }
        },
        methods: {
          submitForm1: function () {
            const payload = {
                      month: this.selected,
                      year: this.year
                  };
            this.getMonthlyEmpower(payload);
          },
          getMonthlyEmpower(payload) {
                  axios.post('/api/monthEmpower', payload)
                  .then(response => {
                    const csv = response.data;
                    const link = document.createElement("a");
                    link.target = "_blank";
                    link.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
                    link.download = "monthlyEmpower.csv";
                    link.click();
                  }).catch((error) => {
                      console.error(error);
                      // Consider adding user-facing error handling here
                  });
              },
          submitForm2: function () {
            const payload = {
                      year: this.year2
                  };
            this.getYearlySummary(payload);
          },
          getYearlySummary(payload) {
                  axios.post('/api/monthSummary', payload)
                  .then(response => {
                    const csv = response.data;
                    const link = document.createElement("a");
                    link.target = "_blank";
                    link.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
                    link.download = "YearSummary.csv";
                    link.click();
                  }).catch((error) => {
                      console.error(error);
                      // Consider adding user-facing error handling here
                  });
              },
          submitForm3: function () {
            const payload = {
                      month: this.selected,
                      year: this.year3
                  };
            this.getWalkInReport(payload);
          },
          getWalkInReport(payload) {
                  axios.post('/api/walkInReport', payload)
                  .then(response => {
                    const csv = response.data;
                    const link = document.createElement("a");
                    link.target = "_blank";
                    link.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
                    link.download = "walkInReport.csv";
                    link.click();
                  }).catch((error) => {
                      console.error(error);
                      // Consider adding user-facing error handling here
                  });
              },
        },
      };
    </script>
  

