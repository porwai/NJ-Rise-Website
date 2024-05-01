<template>
    <br>
    <div class="card">
        <div class="card-body d-flex flex-column" style="overflow-y: auto;">
          <h1 class="card-title">Please select the type of report you would like</h1>
          <!-- <select v-model="selectedSection" required>
                    <option disabled value="">Please select one</option>
                    <option value = "option1">Monthly Empower Report</option>
                    <option value = "option2">Yearly Summary Report</option>
                    <option value = "option3">Walk In Summary Report</option>
                    <option value = "option4">Visit History Basic Frequency Report</option>
                </select> -->
<div class="button-row">
                <button
                  v-for="button in buttons"
                  :key="button.id"
                  :class="{ pressed: currentButton === button.id }"
                  @click="toggleElement(button.id)"
                >
                {{ button.label }}
                </button>
                </div>
                <br>
          

            <!-- <div v-if="selectedSection === 'option1'"> -->
              <div v-if="currentElement === 'element1'">
            <h1 class="card-title">Monthly Empower Report</h1>
            <h3> Select Month</h3>
            <form @submit.prevent="submitForm1">
                <select v-model="selected" required>
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
                  <label for="year" class="form-label"><h3>Select Year</h3></label>
                  <input 
                    v-model="year" 
                    type="number" 
                    class="form-control"
                    id="year"
                    placeholder="YYYY"
                    required
                    min="0"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
          </div>

          <!-- <div v-if="selectedSection === 'option2'"> -->
            <div v-if="currentElement === 'element2'">
          <h1 class="card-title"> Yearly Summary Report</h1>
            <!-- <h2> Select Year</h2> -->
            <form @submit.prevent="submitForm2">
                <div class="mb-3">
                  <label for="year2" class="form-label"><h3>Select Year</h3></label>
                  <input 
                    v-model="year2" 
                    type="number" 
                    class="form-control"
                    id="year2"
                    placeholder="YYYY"
                    required
                    min="0"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        </div>


        <!-- <div v-if="selectedSection === 'option3'"> -->
          <div v-if="currentElement === 'element3'">
        <h1 class="card-title"> Walk In Summary Report</h1>
            <!-- <h2> Select Year</h2> -->
            <form @submit.prevent="submitForm3">
                <div class="mb-3">
                  <label for="year3" class="form-label"><h3>Select Year</h3></label>
                  <input 
                    v-model="year3" 
                    type="number" 
                    class="form-control"
                    id="year3"
                    placeholder="YYYY"
                    required
                    min="0"
                  />
              </div>
                <button class="btn btn-primary" type="submit">Submit</button>
          </form>
        </div>  

          
        <!-- <div v-if="selectedSection === 'option4'"> -->
          <div v-if="currentElement === 'element4'">
        <h1> Visit History Basic Frequency Report</h1>

          <form @submit.prevent = "numVisitReportBasic">
              <label for="basic_report_start_date" class="form-label"><h3>Select Start Date</h3></label>
              <input 
                v-model="basic_report_start_date" 
                type="date" 
                class="form-control"
                id="basic_report_start_date"
                required
              />
              <br>

              <label for="basic_report_end_date" class="form-label"><h3>Select End Date</h3></label>
              <input 
                v-model="basic_report_end_date" 
                type="date" 
                class="form-control"
                id="basic_report_end_date"
                required
              />

              <button class="btn btn-primary" type="submit">Submit</button>
          </form>

               <!-- Display sum and list of visit frequencies -->
            <div v-if="this.basic_report_sum !== null">
              <p>Sum of Visit Frequencies: {{ this.basic_report_sum }}</p>
            
            
            
                <!-- Slider to adjust the range -->
                <label for="range">Select Range:</label>
              <input 
                  type="range"
                  id="range"
                  v-model="selectedRange"
                  min="1"
                  :max="this.basic_report_list ? this.basic_report_list.length : 0"
                  class="full-width-slider"
                  @change="updateData"
              />
              <p>
                Min: 1 ; Current: {{ this.selectedRange}}; max: {{ this.basic_report_list ? this.basic_report_list.length : 0 }}
              </p>
            </div>
            

            <div v-if="this.basic_report_sum !== null">
            <CanvasJSChart :options="options" :style="styleOptions" @chart-ref="chartInstance"/>
          </div>
        </div>
          
          

      </div>

        </div>
    <!-- </div> -->
  </template>
  
    <script>
      import axios from 'axios';
  
      export default {
        name: 'reports',
        data() {
          return {
            // selectedSection: null,
            currentButton: null,
      currentElement: null,
      buttons: [
        { id: 'element1', label: 'Monthly Empower Report' },
        { id: 'element2', label: 'Yearly Summary Report' },
        { id: 'element3', label: 'Walk In Summary Report' },
        { id: 'element4', label: 'Visit History Basic Frequency Report' }
      ],
            selected: null,
            year:new Date().getFullYear(),
            year2:new Date().getFullYear(),
            year3:new Date().getFullYear(),
            basic_report_start_date: 0,
            basic_report_end_date: null,
            basic_report_sum: null,
            basic_report_list: null,

            // variables for displaying chart-js:
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
                  // maximum: this.basic_report_list ? this.basic_report_list.length : 0,
                  // interval: this.selectedRange,
                  viewportMaximum: 0
              },
            },
            styleOptions: {
              width: "100%",
              height: "360px"
            },

            // Used to dynamically update chart intervals
            // Init set at 1 day intervals
            selectedRange: 1, 
            // /////////////////////////////////////////////////////////
          }
        },
        methods: {
          toggleElement(elementId) {
      this.currentButton = elementId;
      this.currentElement = this.currentElement === elementId ? null : elementId;
    },
          submitForm1: function () {
            if (this.year.toString().length !== 4) {
              alert('Please enter a valid 4-digit year.')
            }
            else {
              const payload = {
                        month: this.selected,
                        year: this.year
                    };
              
              
              this.getMonthlyEmpower(payload);
            }
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
            if (this.year.toString().length !== 4) {
              alert('Please enter a valid 4-digit year.')
            }
            else {
              const payload = {
                        year: this.year2
                    };
              this.getYearlySummary(payload);
            }
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
            if (this.year.toString().length !== 4) {
              alert('Please enter a valid 4-digit year.')
            }
            else {
              const payload = {
                        month: this.selected,
                        year: this.year3
                    };
              this.getWalkInReport(payload);
                }
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
      

              // api call to receive number of visits between
              // a given start date and end date
              numVisitReportBasic() {
                this.basic_report_sum = null
                
                const payload = {
                      start_date: this.basic_report_start_date,
                      end_date: this.basic_report_end_date
                  };
                console.log(payload, "inside")
                axios.post('/api/report_basic', payload)
                  .then(response => {
                    this.basic_report_list = response.data;
                    this.selectedRange = this.basic_report_list.length || 1
                    console.log(this.selectedRange, 'selected range in axios post')
                    this.updateSlider(this.selectedRange)

                    // Compute sum using private helper function
                    
                    
                    this.basic_report_sum = this.sumValues(this.basic_report_list);
                    console.log('after basic report sum not null')
                    console.log("styleOptions at updateData:", this.styleOptions);
                    this.updateData()
                    console.log('after updateData')
                    return {
                      selectedRange: this.selectedRange
                      
                    }

                    
                  })
                  .catch(error => {
                    console.error('Error fetching basic report:', error);
                    // Consider adding user-facing error handling here
                  });
                  this.selectedRange = this.selectedRange
              },

          // private helper to compute sum for list of visit frequencies
          sumValues(list) {
            let sum = 0
            for (let i = 0; i < list.length; i++){
              sum += list[i]
            }

            return sum
          },

          updateSlider(newValue) {
            this.selectedRange = newValue;
            // const slider = document.getElementById('range');
            
            // console.log('slider', slider)
            // if (slider) {
            //   slider.style.width = '100%';
            // }
            
          },

          updateData() {


            // update the viewportMax based on slider selectRange val
            this.options.axisX.viewportMaximum = this.selectedRange
            
            console.log("in the update:")
            console.log("selectRange:", this.selectedRange)
            console.log("chartMaxX:", this.options.axisX.viewportMaximum)
            console.log("style options:", this.styleOptions);
              // Reset dataPoints array
              this.options.data[0].dataPoints = [];
              console.log('after reset array');

              if(!this.basic_report_list){
                return true
              }
              console.log('after return true');

              // Iterate over basic_report_list and add data points
              this.basic_report_list.forEach((value, index) => {
                  this.options.data[0].dataPoints.push({ x: index, y: value });
              });
              console.log('after iterate over lists');

              // Render the chart
              if (this.chart) {
                
                this.chart.render();
              }
              console.log('after render chart');
              
          },


          // functions to load chart from chart-js
          chartInstance(chart) {
              this.chart = chart;
              this.updateData();
            }
          },


          unmounted() {
            clearTimeout(this.timeout);
          },

          mounted() {
            this.updateSlider(this.basic_report_list ? this.basic_report_list.length : 0);
            this.updateData()
            
          }



          // computed: {
          //   maxValue() {
          //     return this.basic_report_list ? this.basic_report_list.length : 0;
          //   }
          // },

          // watch: {
          //   selectedRange(newRange, oldRange) {
          //     this.selectedRange = newRange
          //     // this.selectedRange = newList.length || 1;
          //     // console.log(this.selectedRange, 'watch basic report list')
          //   },
          //   immediate: true
          // }

      };
    </script>
  
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.custom-text {
  font-family: 'Roboto', sans-serif;
}

    .full-width-slider {
  width: 100%;
  /* Add additional styling for the thumb and track here */
}

  button {
    /* width: 300px; */
    padding: 10px;
    margin: 5px;
    flex: 1;
    border-radius: 8px;
  }

  .pressed {
    background-color: #6CB4EE;
    color: white;
  }

  .button-row {
    display: flex;        
  justify-content: center; 
  align-items: center;  
  margin-bottom: 20px;
  }



  </style>
