/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
import store from '../store'
export default [
  {
    path: '*',
    meta: {
      name: '',
      requiresAuth: false
    },
    redirect: {
      path: '/dashboard'
    }
  },
  // This  allows you to have pages apart of the app but no rendered inside the dash
   {
     path: '/',
     meta: {
       name: '',
       requiresAuth: false
     },
  
    
     component: () =>
       import(/* webpackChunkName: "routes" */ `@/views/Login.vue`),
    // redirect if already signed in
     beforeEnter: (to, from, next) => {
       if (store.getters.authorized) {
         next('/dashboard')
        
       }
     
      
       else {
           next()
       }
     },
     children: [
       {
         path: '/',
         component: () => import('@/views/Login.vue')
       }
     ]
   },
  // add any extra routes that you want rendered in the dashboard as a child below. Change toolbar names here
  {
    path: '/dashboard',
    meta: {
      name: 'Dashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/Dashboard.vue`),
    
  },
  
  {
    path: '/map_dashboard',
    meta: {
      name: 'mapDashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/DashboardView.vue`),
    
  },

  {
    path: '/pie_dashboard',
    meta: {
      name: 'pieDashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/DashPieView.vue`),
    
  },
  {
    path: '/bar_dashboard',
    meta: {
      name: 'barDashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/BarView.vue`),
    
  },
  {
    path: '/votes_dashboard',
    meta: {
      name: 'votesDashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/VotesView.vue`),
    
  },
  {
    path: '/files_dashboard',
    meta: {
      name: 'filesDashboard',
      requiresAuth: true
    },
    component: () => import(`@/views/AllFiles.vue`),
    
  },
 
 



  
]
