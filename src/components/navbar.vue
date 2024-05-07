<template>

<div class="menu-container">
  <nav class="collapse d-lg-block sidebar collapse bg-white" style="height: 100%;">
    <div class="position-sticky" style="display: flex; flex-direction: column; align-items: center; height: 100%">

      <div style="padding-top: 20px; justify-content: center">
        <a class="navbar-brand" href="/">
          <img src="/src/assets/RiseLogo.png" alt="NJ Rise logo" width="80">
        </a>
      </div>

      <div class="list-group list-group-flush mx-3 mt-4">
        <a href="#" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
          <i class="fas fa-tachometer-alt fa-fw me-3 mr-1"></i><span>Pantry Dashboard</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action py-2 ripple">
          <i class="fas fa-chart-area fa-fw me-3 mr-1"></i><span>Add Walk-In Client</span>
        </a>
        <a v-if = "this.$store.state.viewing_status === 'admin'" class="list-group-item list-group-item-action py-2 ripple" href="/registernewclient">
          <i class="fas fa-user-edit fa-fw me-3"></i>
          Register Client
        </a>
        <a href="#" class="list-group-item list-group-item-action py-2 ripple">
          <i class="fas fa-chart-area fa-fw me-3 mr-1"></i><span>Staff</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action py-2 ripple">
          <i class="fas fa-chart-area fa-fw me-3 mr-1"></i><span>Manage Staff</span>
        </a>
        <a href="#" class="list-group-item list-group-item-action py-2 ripple">
          <i class="fas fa-chart-area fa-fw me-3"></i><span>Reports</span>
        </a>
      </div>
    </div>
  </nav>
</div>

  <!-- Old menu -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">  

        <div class="collapse navbar-collapse justify-content-end" id="navbarMain">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <!-- Sliding toggle button -->
                    
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Pantry Dashboard
                      </a>
                      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="/addwalkin">
                  <i class="fas fa-user-plus mr-1"></i>
                  Add Walk In Client
                </a>
                
              </div>
            </li>
  
            <li class="nav-item">
              <a class="nav-link" href="/search">Client Search</a>
            </li>
  
            <li v-if = "this.$store.state.viewing_status === 'admin'" class="nav-item">
              <a class="nav-link" href="/reports">Reports</a>
            </li>
            
            <li v-if="this.$store.state.login_status === 'not_authorized'" class="nav-item">
              <router-link class="nav-link" to="/login"> Login</router-link>
            </li>
            
            <li v-else class="nav-item">
              <router-link class="nav-link" to="/login" @click="logoutClick"> Logout</router-link>
            </li>
            
            <li v-if = "this.$store.state.viewing_status === 'admin'" class="nav-item">
              <router-link class="nav-link" to="/addnewuser"> Add New Staff </router-link>
            </li>
            <div v-if = "this.$store.state.login_status === 'admin'" class="nav-item navbar-toggler-toggle" @click="toggleClick">
              <transition name="toggle-transition">
                <span v-if="this.$store.state.viewing_status === 'volunteer'" class="toggle-off">
                  <!-- SVG for toggle off state -->
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="60" height="60" class = "svgtoggle">
                    <!-- Your SVG path for toggle off state -->
                    <path d="M280-240q-100 0-170-70T40-480q0-100 70-170t170-70h400q100 0 170 70t70 170q0 100-70 170t-170 70H280Zm0-80h400q66 0 113-47t47-113q0-66-47-113t-113-47H280q-66 0-113 47t-47 113q0 66 47 113t113 47Zm0-40q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Zm200-120Z" />
                  </svg>
                </span>
                <span v-else class="toggle-on">
                  <!-- SVG for toggle on state -->
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" width="60" height="60" class = "svgtoggle">
                    <!-- Your SVG path for toggle off state -->
  
                    <path d="M280-240q-100 0-170-70T40-480q0-100 70-170t170-70h400q100 0 170 70t70 170q0 100-70 170t-170 70H280Zm0-80h400q66 0 113-47t47-113q0-66-47-113t-113-47H280q-66 0-113 47t-47 113q0 66 47 113t113 47Zm400-40q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35ZM480-480Z" />
                  </svg>
                </span>
              </transition>
            </div>
  
              <!-- Text next to toggle button -->
              <li v-if = "this.$store.state.login_status !== 'not_authorized'" class="nav-item">
                <a  v-if="this.$store.state.viewing_status === 'volunteer'" class="nav-link">View: Volunteer</a>
                <a  v-else class="nav-link">View: Administrator</a>
              </li>

          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavBar',
    data() {
      console.log("check init:", this.$store.state.viewing_status)
      return {
        // set togglePosition with ternary operator 
        // depending on whether admin is viewing login view or admin view
        togglePosition: this.$store.state.viewing_status === 'admin' ? 'right' : 'left',
        toggleText: this.$store.state.viewing_status === 'admin' ? 'Administrator' : 'Volunteer',
        login_status: "admin"
      };
    },
    methods: {
      toggleClick() {
        if (this.togglePosition === 'left') {
          console.log('click right');
          this.togglePosition = 'right';
          this.toggleText = "Administrator";
          this.$store.commit('log_in_admin')
          console.log("login status", this.$store.state.login_status)
          console.log("viewing status", this.$store.state.viewing_status)

        } else {
          console.log('click left');
          this.togglePosition = 'left';
          this.toggleText = "Volunteer";
          this.$store.commit('log_in_admin_volunteer_view')
          console.log("login status", this.$store.state.login_status)
          console.log("viewing status", this.$store.state.viewing_status)
          this.$router.go(0);


        }
      },
      // function to logout user
      logoutClick() {
        console.log("BEFORE login status", this.$store.state.login_status)
        console.log("viewing status", this.$store.state.viewing_status)
        this.$store.commit('log_out')
        console.log("login status", this.$store.state.login_status)
        console.log("viewing status", this.$store.state.viewing_status)
      }
    }
  }
  </script>
  
  <style>
  .menu-container{
    width: 20%; 
    float: left;
    display: flex; 
    height: 100vh;
    overflow: hidden;
  }

  .fas{
    margin-right: 5px;
  }

  .list-group{
    padding-top: 20px;
    display: flex; 
    flex-direction: column;  
    justify-content: center;
  }

  .list-group-item{
    font-size: 16px;
  }

  .navbar-toggler-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px; /* Increased width */
    cursor: pointer;
    margin-left: 300px; /* Shift to the right */
  }
  
  .toggle-on svg, .toggle-off svg {
    width: 80px; /* Larger size */
    height: 50px; /* Larger size */
    fill: #459bcd; /* Blue color */
  }
  
  .toggle-off svg {
    margin-right: 20px; /* Add margin for spacing */
  }

  .toggle-on svg {
    margin-right: 20px; /* Add margin for spacing */
  }
  
  .toggle-on svg:hover, .toggle-off svg:hover {
    fill: #19527c; /* Darker blue on hover */
  }
  </style>
  