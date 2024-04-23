import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserDetails from '../components/UserDetails.vue'
import DataTable from '../components/DataTable.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
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
      component: UserDetails
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/addnewuser',
      name: 'addnewuser',
      // route level code-splitting
      component: () => import('../views/AddNewUserView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/addwalkin',
      name: 'addwalkin',
      component: () => import('../views/AddWalkIn.vue')
    }, 
    {
      path: '/registernewclient',
      name: 'registernewclient',
      component: () => import('../views/RegisterClient.vue')
    }
  ]
})

export default router
