<style scoped>
/* Custom checkbox */

	.table-wrapper {
        background: #fff;
        padding: 20px 25px;
		border-radius: 3px;
        box-shadow: 0 1px 1px rgba(0,0,0,.05);
        margin: 20px 0;
        overflow-x: auto;
        overflow-y: auto;
    }
	.table-title {        
		background: #435d7d;
		color: #fff;
		padding: 16px 30px;
		margin: -20px -25px 10px;
		border-radius: 3px 3px 0 0;
    }    
    table.table tr th, table.table tr td {
    border-color: #e9e9e9;
		padding: 12px 15px;
		vertical-align: middle;
    }
	table.table tr th:last-child {
		width: 100px;
	}
    
    table.table th i {
        margin: 0 5px;
        cursor: pointer;
    }	
    table.table .actions {
        background-color: white;
        margin: 0 5px;
        position: sticky;
        right: 0;
        z-index: 100;
    }
	table.table td a {
		font-weight: bold;
		color: #566787;
		display: inline-block;
		text-decoration: none;
		outline: none !important;
	}

	table.table td a:hover {
		color: #2196F3;
	}
	table.table td a.edit {
        color: #FFC107;
    }
    table.table td a.delete {
        color: #F44336;
    }
    table.table td i {
        font-size: 19px;
    }
    
    .custom-checkbox {
		position: relative;
	}
	.custom-checkbox input[type="checkbox"] {    
		opacity: 0;
		position: absolute;
		margin: 5px 0 0 3px;
		z-index: 9;
	}
	.custom-checkbox label:before{
		width: 18px;
		height: 18px;
	}
	.custom-checkbox label:before {
		content: '';
		margin-right: 10px;
		display: inline-block;
		vertical-align: text-top;
		background: white;
		border: 1px solid #bbb;
		border-radius: 2px;
		box-sizing: border-box;
		z-index: 2;
	}
	.custom-checkbox input[type="checkbox"]:checked + label:after {
		content: '';
		position: absolute;
		left: 6px;
		top: 3px;
		width: 6px;
		height: 11px;
		border: solid #000;
		border-width: 0 3px 3px 0;
		transform: inherit;
		z-index: 3;
		transform: rotateZ(45deg);
	}
	.custom-checkbox input[type="checkbox"]:checked + label:before {
		border-color: #03A9F4;
		background: #03A9F4;
	}
	.custom-checkbox input[type="checkbox"]:checked + label:after {
		border-color: #fff;
	}
	.custom-checkbox input[type="checkbox"]:disabled + label:before {
		color: #b8b8b8;
		cursor: auto;
		box-shadow: none;
		background: #ddd;
	}

    .table-title .row {
      align-items: center; /* Aligns items vertically in the middle */
    }

    @media (max-width: 767px) {
        .table-title .text-right {
            text-align: left; /* Aligns button left on small devices */
            padding-top: 10px;
        }
    }

    .button-group .btn {
    width: 180px; /* Adjust the width as needed */
    margin-right: 30px; /* Adds spacing between the buttons */
    }

    .button-group .btn:last-child {
    margin-right: 0; /* Removes the margin from the last button */
    }

</style>

<template>
      <br>
      <!-- Inline form using Bootstrap's row and col classes -->
      <div class="row">
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="first_name" placeholder="First Name" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="last_name" placeholder="Last Name" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="client_id" placeholder="Client ID" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="phone" placeholder="Phone" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="month" placeholder="DOB: Month (MM)" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="day" placeholder="DOB: Day (DD)" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="year" placeholder="DOB: Year (YYYY)" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
      </div>
    
    <div class="table-wrapper">
        <div class="table-title">
            <div class="row align-items-center justify-content-between">
                <div class="col-auto">
                    <h1 style="padding-left: 15px; align-items: center;">{{ masterDBView ? 'Master Database ' : '' }}Query Matches: <b>{{clients.length}}</b></h1>
                </div>
                <div class="col-auto">
                    <div class="button-group" style="float: right;">
                        <button class="btn btn-info" @click="handleQueryEvent">
                            <span>Search</span>
                        </button>

                        <button class="btn btn-warning" @click="toggleDBView(); handleQueryEvent(); $emit('close-details');" v-if="adminStatus">
                            <span>MasterDB Toggle</span>
                        </button>

                        <router-link to="/addwalkin" class="btn btn-success">
                            <span>Add Walk-In Client</span>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="table-responsive">
        <table class="table table-bordered table-striped table-hover">
            <thead>
                <tr>
                    <template v-if="key !== 'transactional_id'">
                        <th 
                        v-for="(value, key) in clients[0]" :key="key" 
                        v-if="key !== 'transactional_id'">
                                {{ formatKey(key) }}
                        </th>
                    </template>
                    <th v-if="adminStatus" class="actions"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="client in clients" :key="client.transactional_id"
                :class="{ 'highlighted': client.transactional_id === activeRowId }">
                    <template v-if="key !== 'transactional_id'">
                        <td 
                        v-for="(value, key) in client" :key="key" 
                        v-if="key !== 'transactional_id'"
                        @click="handleClientDetailsEvent(client)">
                                {{ value }}
                        </td>
                    </template>
                    <td  v-if="adminStatus" class="actions">
                        <a class="delete" title="Delete" data-toggle="tooltip" @click="handleDelete(client.transactional_id)">
                            <i class="fas fa-trash mr-1"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</template>
  
<script>
    import axios from 'axios';

    export default {
        name: 'search',

        data() {
            return {
            first_name: '',
            last_name: '',
            client_id: '',
            phone: '',
            month: '',
            day: '',
            year: '',
            activeRowId: null,
            clients: []};
        },
        mounted() {
          this.handleQueryEvent();
          this.clients.forEach( client => client.selected = false);
        },
        methods: {
            queryClients(payload) {
                if (this.$store.state.login_status === "not_authorized") {
                    console.log("FALSE LOGIN")
                    this.$router.push({ path: '/login'})
                }
                axios.post('/api/search', payload)
                .then((response) => {
                    this.clients = response.data;
                }).catch((error) => {
                    console.error(error);
                    // Consider adding user-facing error handling here
                });
            },
            queryMasterDB(payload) {
                if (this.$store.state.login_status === "not_authorized") {
                    console.log("FALSE LOGIN")
                    this.$router.push({ path: '/login'})
                }
                if (this.$store.state.viewing_status !== "admin") {
                    alert("You must be an admin to query the master database.");
                    this.toggleDBView();
                    return;
                }
                axios.post('/api/query_masterdatabase', payload)
                .then((response) => {
                    this.clients = response.data;
                }).catch((error) => {
                    console.error(error);
                    // Consider adding user-facing error handling here
                });
            },
            handleQueryEvent() {
                const payload = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    client_id: this.client_id,
                    phone: this.phone,
                    month: this.month,
                    day: this.day,
                    year: this.year
                };
                if (this.masterDBView) {
                    this.queryMasterDB(payload);
                } else {
                    this.queryClients(payload);
                }
            },
            handleClientDetailsEvent(clientData) {
                if (this.showDetails == false) {
                    this.$emit('toggle-details')
                }
                this.$emit('new-client-request', clientData);
            },
            handleDelete(t_id) {
                const payload = {
                    transactional_id: t_id
                };
                if (this.$store.state.login_status === "not_authorized") {
                    console.log("FALSE LOGIN")
                    this.$router.push({ path: '/login'})
                    return;
                }
                if (this.$store.state.viewing_status !== "admin") {
                    alert("You must be an admin to delete the database.");
                    return;
                }
                axios.post('/api/delete_t_client', payload)
                .then((response) => {
                    console.log("Deletion successful:", response.data);
                    this.clients = this.clients.filter(client => client.transactional_id !== t_id);
                }).catch((error) => {
                    console.error("Error deleting client:", error);
                    // Consider adding user-facing error handling here
                });
            }, 
            selectAllClients() {
              let all_s = this.allSelected;
              this.clients.forEach( client => client.selected = !all_s );
            },
            setActiveRow(id) {
                this.activeRowId = id;
            },
            formatKey(key) {
              return key.split('_')
                        .map(part => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
                        .join(' ');
            },
            toggleDBView() {
                this.$store.commit('toggleMasterDBView'); // Mutating the state
            }
        },
        computed: { 
            masterDBView() {
                return this.$store.state.master_db_view; // Accessing the state
            }, 
            adminStatus() {
                return (this.$store.state.viewing_status === "admin");
            }
        }, 
        props: {
            showDetails: {
                type: Boolean,
                required: true
            }
        }
    }
</script>