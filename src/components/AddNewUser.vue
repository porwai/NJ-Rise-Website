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
                <input type="text" v-model="formData.userRole" class="form-control" placeholder="User Role" required>
              </div>

              <div class="text-center">
                <button type="submit" class="btn btn-primary mt-4">Add User</button>
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
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Username</th>
                  <th scope="col">Password</th>
                  <th scope="col">User Role</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="user in users" :key="user.username">
                  <td>{{ user.username }}</td>
                  <td>{{ user.password }}</td>
                  <td>{{ user.user_role }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const formData = ref({
  username: '',
  password: '',
  userRole: ''
});

const users = ref([]);

async function submitData() {
  try {
    const response = await fetch('/api/add_new_user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender_role: 'admin',
        username: formData.value.username,
        password: formData.value.password,
        user_role: formData.value.userRole
      })
    });
    const data = await response.json();
    if (data.status) {
      alert('User added successfully.');
      // Optionally, you can redirect the user to another page after successful addition.
    } else {
      alert('Failed to add user. Please check your input and try again.');
    }
  } catch (error) {
    console.error('Error adding user:', error);
    alert('An error occurred while adding user. Please try again later.');
  }
}

// Fetch all current users on component mount
onMounted(async () => {
  try {
    const response = await fetch('/api/read_all_users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        sender_role: 'admin'
      })
    });
    const data = await response.json();
    if (data.status) {
      users.value = data.user_list;
    } else {
      alert('Failed to fetch users. Please try again.');
    }
  } catch (error) {
    console.error('Error fetching users:', error);
    alert('An error occurred while fetching users. Please try again later.');
  }
});
</script>

<style>
.card {
  margin-bottom: 20px;
}
</style>
