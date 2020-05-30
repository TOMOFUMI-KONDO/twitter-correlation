import Vue from 'vue'
import VueRouter from 'vue-router'
import Search from '../views/Search.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/search',
    name: 'Search',
    component: Search
    // () => import('../views/Search.vue')
  },
  {
    path: '*',
    name: 'NotFound',
    component: NotFound
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
