<template>
    <br>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
            <h1 class="card-title">Monthly Empower Report</h1>
            <h2> Select Month of Empower Report</h2>
            <form @submit.prevent="submitForm">
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

          <h2> Visit History Basic Frequency Report</h2>

          <form @submit.prevent = "numVisitReportBasic">
              <label for="basic_report_start_date" class="form-label">Start Date</label>
              <input 
                v-model="basic_report_start_date" 
                type="date" 
                class="form-control"
                id="basic_report_start_date"
              />

              <label for="basic_report_end_date" class="form-label">End Date</label>
              <input 
                v-model="basic_report_end_date" 
                type="date" 
                class="form-control"
                id="basic_report_end_date"
              />

              <button class="btn btn-primary" type="submit">Submit</button>
          </form>

               <!-- Display sum and list of visit frequencies -->
            <div v-if="this.basic_report_sum !== null">
              <p>Sum of Visit Frequencies: {{ this.basic_report_sum }}</p>
            </div>

                <!-- Slider to adjust the range -->
              <label for="range">Select Range:</label>
              <input 
                  type="range" 
                  id="range" 
                  v-model="selectedRange" 
                  min="1" 
                  :max="basic_report_list.length" 
                  @change="updateData"
              />
              <p>
                Min: 1 ; Current: {{ this.selectedRange}}; max: {{ this.basic_report_list.length }}
              </p>

            <CanvasJSChart :options="options" :style="styleOptions" @chart-ref="chartInstance"/>



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
            basic_report_start_date: 0,
            basic_report_end_date: null,
            basic_report_sum: null,
            basic_report_list: [],

            // /////////////////////////////////////////////////////////
            // variables for displaying chart-js:
            // SEE DETAILED CHART-JS DOCS HERE:
            // https://canvasjs.com/vuejs-charts/dynamic-live-line-chart/
            // /////////////////////////////////////////////////////////
            chart: null,
            xValue: 1,
            yValue: 10,
            newDataCount: 10,
            timeout: null,
            options: {
              theme: "light2",
              title:{
                text: "Live Data"
              },
              data: [{
                type: "line",
                dataPoints: []
              }],
              axisX: {
                  title: "Days",
                  maximum: this.basic_report_list ? this.basic_report_list.length : 0,
                  interval: this.selectedRange,
              },
              axisY: {
                  title: "Number of Visits",
                  maximum: 3,
                  interval: 1
              },
            },
            styleOptions: {
              width: "100%",
              height: "560px"
            },

            // Used to dynamically update chart intervals
            // Init set at 1 day intervals
            selectedRange: 1, 

            // /////////////////////////////////////////////////////////
          }
        },
        methods: {
          submitForm: function () {
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

              // api call to receive number of visits between
              // a given start date and end date
              numVisitReportBasic() {
                const payload = {
                      start_date: this.basic_report_start_date,
                      end_date: this.basic_report_end_date
                  };
                console.log(payload, "inside")
                axios.post('/api/report_basic', payload)
                  .then(response => {
                    this.basic_report_list = response.data;

                    // Compute sum using private helper function
                    this.basic_report_sum = this.sumValues(this.basic_report_list);
                    this.updateData();

                  })
                  .catch(error => {
                    console.error('Error fetching basic report:', error);
                    // Consider adding user-facing error handling here
                  });
              },

          // private helper to compute sum for list of visit frequencies
          sumValues(list) {
            let sum = 0
            for (let i = 0; i < list.length; i++){
              sum += list[i]
            }

            return sum
          },

          updateData() {
            console.log("reached update data")
            if (!this.basic_report_list) {
                console.warn('basic_report_list is null. No data to update.');
                return;
            }

            // Reset dataPoints array
            this.options.data[0].dataPoints = [];

            // Iterate over basic_report_list based on selectedRange
            // for (let i = 0; i < this.basic_report_list.length; i += this.selectedRange) {
            //     this.options.data[0].dataPoints.push({ x: i, y: this.basic_report_list[i] });
            // }

            this.basic_report_list.forEach((value, index) => {
                this.options.data[0].dataPoints.push({ x: index, y: value });
            });

            // Render the chart
            this.chart.render();
        },

          // functions to load chart from chart-js
          chartInstance(chart) {
              this.chart = chart;
              this.updateData();
            }
          },


          unmounted() {
            clearTimeout(this.timeout);
          }
      };
    </script>
  

