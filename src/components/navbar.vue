<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <!-- Logo on the left -->
        <a class="navbar-brand" href="/">
          <img src="/src/assets/RiseLogo.png" alt="NJ Rise logo" width="80">
        </a>
  
                <!-- Toggler button -->
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        

        <!-- Navigation links on the right -->
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
                <a v-if = "this.$store.state.viewing_status === 'admin'" class="dropdown-item" href="/registernewclient">
                  <i class="fas fa-user-edit mr-1"></i>
                  Register Client
                </a>
                <a v-if = "this.$store.state.viewing_status === 'admin'" class="dropdown-item" href="/import">
                  <i class="fas fa-user-edit mr-1"></i>
                  Import CSV File
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

            <!-- Text next to toggle button -->
              <li v-if = "this.$store.state.login_status !== 'not_authorized'" class="nav-item">
                <a  v-if="this.$store.state.viewing_status === 'volunteer'" class="nav-link">View: Volunteer</a>
                <a  v-else class="nav-link">View: Administrator</a>
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
  