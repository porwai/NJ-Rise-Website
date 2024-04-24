import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import UserDetails from '../components/UserDetails.vue';
import DataTable from '../components/DataTable.vue';
import LoginView from '../views/LoginView.vue';

import store from '../main'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        requiresAuth: true // Example: Home page requires authentication
      }
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/userdetails',
      name: 'userdetails',
      component: UserDetails,
      meta: {
        requiresAuth: true // Example: User details page requires authentication
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/addnewuser',
      name: 'addnewuser',
      component: () => import('../views/AddNewUserView.vue'),
      meta: {
        requiresAuth: true // Example: Add new user page requires authentication
      }
    },
    {
      path: '/search',
      name: 'search',
      component: HomeView,
      meta: {
        requiresAuth: true // Example: Search page requires authentication
      }
    },
    {
      path: '/addwalkin',
      name: 'addwalkin',
      component: () => import('../views/AddWalkIn.vue'),
      meta: {
        requiresAuth: true // Example: Add walk-in page requires authentication
      }
    }, 
    {
      path: '/registernewclient',
      name: 'registernewclient',
      component: () => import('../views/RegisterClient.vue'),
      meta: {
        requiresAuth: true // Example: Register new client page requires authentication
      }
    }
  ]
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = store.state.login_status !== 'not_authorized';

  console.log("in router:")
  console.log("login status", store.state.login_status)
  console.log("viewing status", store.state.viewing_status)

  if (requiresAuth && !isAuthenticated) {
    // Redirect to login page
    next('/login');
  } else {
    // Proceed to the next middleware or route
    next();
  }
});

export default router;
