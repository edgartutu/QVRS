<template>
    <v-app>
		
      <!-- <v-content > -->
			  <router-view />  
      <!-- </v-content> -->
		<!-- <navis style="margin-top:-500%;"/> -->
	
    </v-app>
 
</template>

<style >
	
</style>
<script>
import navis from './components/DashViews/NavBar'
// import navbar from './components/DashViews/NavBar'
// import Clock from 'vue-clock2';
import {
  
  mapState
} from 'vuex'
	// checks to see if auth jwt token is valid or has expired, if it gets back 401 error log out
	export default {
		components:{
    			 navis
				},
				
				computed:{
					...mapState(['snackbar'])
				},

		





		created: function () {
			this.$http.interceptors.response.use( (response) => {
        return response;
      }, (error) => {
          if (401 === error.response.status) {
						if (this.$store.getters.authorized) {
							this.$store.dispatch('refreshtoken')
							}else {
              return Promise.reject(error);
          }
						
					} else {
              return Promise.reject(error);
          }
				});
		}
	};
</script>
