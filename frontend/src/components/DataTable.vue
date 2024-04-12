<style>
/* Custom checkbox */

	.table-wrapper {
		min-width: 1000px;
        background: #fff;
        padding: 20px 25px;
		border-radius: 3px;
        box-shadow: 0 1px 1px rgba(0,0,0,.05);
        margin: 20px 0;
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
	table.table tr th:first-child {
		width: 55px;
	}
	table.table tr th:last-child {
		width: 100px;
	}
    table.table-striped tbody tr:nth-of-type(odd) {
    	background-color: #fcfcfc;
	}
	table.table-striped.table-hover tbody tr:hover {
		background: #f5f5f5;
	}
    table.table th i {
        font-size: 13px;
        margin: 0 5px;
        cursor: pointer;
    }	
    table.table td:last-child i {
		opacity: 0.9;
		font-size: 22px;
        margin: 0 5px;
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

    .highlighted {
    background-color: #747baf; /* Yellow background for highlighting */
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
          <input type="text" v-model="first_name" placeholder="Firstname" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="last_name" placeholder="Lastname" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="client_id" placeholder="Client ID" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="phone" placeholder="Phone" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-md-12 col-lg mb-2">
          <input type="text" v-model="dob" placeholder="Date of Birth" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
      </div>      
    
  <div class="table-wrapper scrollable-table">
    <div class="table-title">
        <div class="row">
            <div class="col-auto">
                <h1 style="padding-left: 15px;">Query Matches: <b>{{clients.length}}</b></h1>
            </div>
            <div class="col button-group d-flex justify-content-end">
                <router-link to="/search" class="btn btn-warning" data-toggle="modal">
                    <font-awesome-icon :icon="['fas', 'plus']" /> <span>Advanced Search</span>
                </router-link>

                <router-link to="/addwalkin" class="btn btn-success" data-toggle="modal">
                    <font-awesome-icon :icon="['fas', 'plus']" /> <span>Add Walk-In Client</span>
                </router-link>
            </div>
        </div>
    </div>
    <br>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th><input type="checkbox" class="checkbox" :checked="allSelected" @click="selectAllClients"/></th>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Client ID</th>
                <th>Phone</th>
                <th>dob</th>
                <th>actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="client in clients" :key="client.transactional_id"
            :class="{ 'highlighted': client.transactional_id === activeRowId }">
                <td><input type="checkbox" class="checkbox" v-model="client.selected"/></td>
                <td @click="handleClientDetailsEvent(client)">{{ client.first_name }}</td>
                <td @click="handleClientDetailsEvent(client)">{{ client.last_name }}</td>
                <td @click="handleClientDetailsEvent(client)">{{ client.client_id }}</td>
                <td @click="handleClientDetailsEvent(client)">{{ client.phone }}</td>
                <td @click="handleClientDetailsEvent(client)">{{ client.dob }}</td>
                <td>
                    <a class="edit" title="Edit" data-toggle="tooltip"><i class="material-icons">e</i></a>
                    <a class="delete" title="Delete" data-toggle="tooltip"><i class="material-icons">d</i></a>
                </td>
            </tr>
        </tbody>
    </table>
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
            dob: '',
            activeRowId: null,
            clients: []
            };
        },
        mounted() {
          this.clients.forEach( client => client.selected = false);
        },
        methods: {
            queryClients(payload) {
                if (this.$store.state.login_status === false) {
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
            handleQueryEvent() {
                const payload = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    client_id: this.client_id,
                    phone: this.phone,
                    dob: this.dob,
                };
                this.queryClients(payload);
            },
            handleClientDetailsEvent(clientData) {
                if (this.showDetails == false) {
                    this.$emit('toggle-details')
                }
                this.$emit('new-client-request', clientData);
            }, 
            handleDelete() {
              
            }, 
            selectAllClients() {
              let all_s = this.allSelected;
              this.clients.forEach( client => client.selected = !all_s );
            },
            setActiveRow(id) {
                this.activeRowId = id;
            }
        },
        computed: {
        allSelected() {
          return this.clients.every(client => client.selected);
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