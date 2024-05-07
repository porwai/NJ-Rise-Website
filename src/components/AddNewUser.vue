<template>
  <div class="container mt-5">
    <div class="row">
      <!-- Left column: Existing user creation form -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <div class="text-center">
              <img src="/src/assets/RiseLogo.png" style="max-width: 8%" class="mb-4 mt-5" alt="NJ Rise logo">
              <h4 class="mb-5">Add New User</h4>
            </div>

            <form @submit.prevent="submitData">
              <div class="form-group">
                <input type="text" v-model="formData.username" class="form-control" placeholder="Username" required>
              </div>

              <div class="form-group">
                <input type="password" v-model="formData.password" class="form-control" placeholder="Password" required>
              </div>

              <div class="form-group">
                <select v-model="formData.userRole" class="form-control" required>
                  <option value="">Select User Role</option>
                  <option value="volunteer">Volunteer</option>
                  <option value="admin">Admin</option>
                </select>
              </div>

              <div class="text-center">
                <button type="submit" class="btn btn-primary mt-4">Add User</button>
              </div>

              <!-- Display status of add user operation -->
              <div class="text-center mt-2">
                <p>{{ status }}</p>
              </div>
            </form>
          </div>
        </div>
      </div>

      <!-- Right column: Display all current users -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="text-center mb-4">Current Users</h4>
            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col">Username</th>
                  <th scope="col">User Role</th>
                  <!-- <th scope="col">Password</th> -->
                  <th scope="col"></th> <!-- New column for delete button -->
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users" :key="user.username" class="table-light">
                  <td>{{ user.username }}</td>
                  <!-- <td>{{ user.password }}</td> -->
                  <td>{{ user.user_role }}</td>
                  <td>
                    <button @click="deleteUserConfirmation(user.username, user.password)" class="btn btn-danger">Delete</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <!-- Right column: Display all current users -->

    </div>
  </div>

    <!-- Modal for confirmation -->
    <div class="modal" id="confirmationModal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Confirmation</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          Are you sure you would like to delete this user from the database?
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-dismiss="modal">No</button>
          <button type="button" class="btn btn-danger" @click="confirmDelete">Yes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import store from '../main'
import $ from "jquery"
import {sha256} from 'crypto-hash';


const formData = ref({
  username: '',
  password: '',
  userRole: ''
});

const users = ref([]);
const status = ref('');
let userToDelete = {}; // Variable to hold the user to delete

// Hashing password with SHA 256
async function submitData() {
  try {
    const response = await fetch('/api/add_new_user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender_role: store.state.viewing_status,
        username: formData.value.username,
        password: await sha256(formData.value.password),
        user_role: formData.value.userRole
      })
    });
    const data = await response.json();
    if (data.status) {
      status.value = 'User added successfully.';
      fetchUsers();
    } else {
      status.value = 'Failed to add user. Please check your input and try again.';
    }
  } catch (error) {
    console.error('Error adding user:', error);
    status.value = 'An error occurred while adding user. Please try again later.';
  }
}

async function fetchUsers() {
  try {
    const response = await fetch('/api/read_all_users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender_role: store.state.viewing_status
      })
    });
    const data = await response.json();
    if (data.status) {
      users.value = data.user_list;
    } else {
      status.value = 'Failed to fetch users. Please try again.';
    }
  } catch (error) {
    console.error('Error fetching users:', error);
    status.value = 'An error occurred while fetching users. Please try again later.';
  }
}

async function deleteUserConfirmation(username, password) {
  userToDelete = { username, password };
  $('#confirmationModal').modal('show');
}

async function confirmDelete() {
  $('#confirmationModal').modal('hide'); // Hide the modal
  try {
    const response = await fetch('/api/remove_user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender_role: store.state.viewing_status,
        username: userToDelete.username,
        password: userToDelete.password
      })
    });
    const data = await response.json();
    if (data.status) {
      status.value = 'User removed successfully.';
      fetchUsers(); // Fetch updated user list
    } else {
      status.value = 'Failed to remove user. Please try again.';
    }
  } catch (error) {
    console.error('Error removing user:', error);
    status.value = 'An error occurred while removing user. Please try again later.';
  }
}

// Fetch all current users on component mount
onMounted(fetchUsers);
</script>

<style>
.table-hover tbody tr:hover td,
.table-hover tbody tr:hover th {
  background-color: #f2f2f2; /* Light gray background on hover */
  transition: background-color 0.5s; /* Smooth transition over 1 second */
}



.card {
  margin-bottom: 20px;
}
</style>
