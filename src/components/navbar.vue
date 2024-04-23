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
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Pantry Dashboard
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="/addwalkin">
                            <i class="fas fa-user-plus mr-1"></i>
                            Add Walk In Client
                        </a>
                        <a class="dropdown-item" href="/registernewclient">
                            <i class="fas fa-user-edit mr-1"></i>
                            Register Client
                        </a>
                    </div>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="/search">Client Search</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="/reports">Reports</a>
                </li>

                <li class="nav-item">
                    <span class="nav-link disabled">Staff</span> <!-- Changed to span for semantics -->
                </li>

                <li class="nav-item">
                        <router-link class="nav-link" to="/login"> Login</router-link>
                </li>

                <li class="nav-item">
                        <router-link class="nav-link" to="/addnewuser"> Add New User </router-link>
                </li>
            </ul>
        </div>
    </div>
</nav>
</template>

<script>
export default {
    name: 'NavBar'
}
</script>