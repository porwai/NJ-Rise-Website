<template>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <!-- Logo on the left -->
            <router-link class="navbar-brand" to="/">
                <img src="/src/assets/RiseLogo.png" width="80" height="auto" alt="NJ Rise logo">
            </router-link>

            <!-- Toggler button -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Navigation links on the right -->
            <div class="collapse navbar-collapse justify-content-end" id="navbarMain">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">

                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Pantry Dashboard
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="/addwalkin">Add Walk In Client</a>
                        <a class="dropdown-item" href="/">Register Client</a>
                        </div>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link" to="/search">Client Search</router-link>
                    </li>

                    <li class="nav-item">
                        <router-link class="nav-link" to="/reports">Reports</router-link>
                    </li>
                    
                    <li class="nav-item">
                        <span class="nav-link disabled">Staff</span> <!-- Changed to span for semantics -->
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/login"> Login</router-link>
                    </li>
                </ul>
            </div><!--/.nav-collapse -->
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>