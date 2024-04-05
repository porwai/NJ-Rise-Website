<!-- DataTable.vue -->
<template>
      <!-- Inline form using Bootstrap's row and col classes -->
      <div class="row">
        <div class="col-12 mb-2">
          <input type="text" v-model="first_name" placeholder="Firstname" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-12 mb-2">
          <input type="text" v-model="last_name" placeholder="Lastname" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-12 mb-2">
          <input type="text" v-model="client_id" placeholder="Client ID" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-12 mb-2">
          <input type="text" v-model="phone" placeholder="Phone" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
        <div class="col-12 mb-2">
          <input type="text" v-model="dob" placeholder="dob" class="form-control" @keyup.enter="handleQueryEvent" />
        </div>
      </div>      


      <table class="table table-striped">
        <thead>
          <tr>
            <th v-if="clients.length > 0" v-for="header in Object.keys(clients[0])" :key="header">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in clients" :key="client.clientid" @click="rowClicked(client)">
            <td>{{ client.first_name }}</td>
            <td>{{ client.last_name }}</td>
            <td>{{ client.client_id }}</td>
            <td>{{ client.phone }}</td>
            <td>{{ client.dob }}</td>
          </tr>
        </tbody>
      </table>

      <!-- 
      <table class="table table-striped">
        <thead>
          <tr v-for="clients in clients[0]" :key="client.clientid">
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Client ID</th>
            <th>Phone</th>
            <th>dob</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in clients" :key="client.clientid" @click="rowClicked(client)">
            <td>{{ client.first_name }}</td>
            <td>{{ client.last_name }}</td>
            <td>{{ client.client_id }}</td>
            <td>{{ client.phone }}</td>
            <td>{{ client.dob }}</td>
          </tr>
        </tbody>
      </table>
      -->

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
            clients: [{name: 'John', phone: '019283', dependents: 'wed'}],
            };
        },

        methods: {
            queryClients(payload) {
                axios.post('http://127.0.0.1:5000/api/search', payload)
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
                this.handleClientDetailsEvent()
            },
            
            handleClientDetailsEvent() {
              this.$emit('toggle-details')
            }, 
        }
    }
</script>
