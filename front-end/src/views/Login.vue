<template>
      <div class="log">
        <v-container>
          <v-layout wrap row justify-space-around>
            <v-flex xs12 md12>

                  <v-toolbar style="background-color:#363940" flat  dense floating>
          <h3 class="white--text" style="font-size:2vw">ElECTRONIC RESULTS VISUALISATION SYSTEM</h3>
         <v-spacer></v-spacer>
            <v-avatar size="68" >
                <img
                    src="@/assets/img/vote.png"
                    alt="EC"
                   
                >
                </v-avatar>
           <v-toolbar-title style="color:#faee02;" >QVRS</v-toolbar-title>
          
           <!-- <p></p>
           <p></p>
            <v-toolbar-items class="hidden-sm-and-down" >
                <v-layout  row >
                <v-btn  flat small  class=" mx-2 white--text" v-for="link in links" :key="link.text" router :to="link.route">
                    <span>{{link.text}}</span>
                </v-btn>
                </v-layout>
            </v-toolbar-items>
            <v-spacer></v-spacer>
                <p></p>
                 <v-menu class="hidden-md-and-up">
                    <v-toolbar-side-icon slot="activator" class="purple--text"   ></v-toolbar-side-icon>
                    <v-list>
                    <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                        <v-list-tile-content>
                        <v-list-tile-title class="purple--text">{{ link.text}}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>   
                    </v-list>
                </v-menu>
                <router-link v-ripple  to="/dashboard">
					<v-icon class="mx-2" color="white">mdi-home</v-icon><br>
				</router-link>
                <v-menu bottom left content-class offset-y transition="slide-y-transition">
					<router-link v-ripple slot="activator"  to="/projects">
						<v-badge color="#f73b3b" overlap>
					        <template slot="badge"  >
                               {{projects.length}}
                                </template>
					            <v-icon class="mx-2" color="white">mdi-bell</v-icon>
				        </v-badge>
					</router-link> -->
					<!-- <v-card> -->
						<!-- <v-list dense>
							<v-list-tile v-for="notification in notifications" :key="notification" @click="onClick">
								<v-list-tile-title v-text="notification"/>
							</v-list-tile>
						</v-list> -->
					<!-- </v-card> -->
				<!-- </v-menu>
                     <v-btn flat class="white--text" @click=" logout()">
                    <span style="color:#faee02;">SignOut</span>
                    <v-icon>exit_to_app</v-icon>
                    </v-btn>  -->
        </v-toolbar>

            </v-flex>

                  
        <!-- <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="6"
            sm="8"
            md="4"
          > -->
           <v-spacer></v-spacer>
          <br>
          <br>
          <br><br>
          
         
            <v-flex sm12 md12>
                <v-card class="elevation-12 right"   >
                  <v-container>
                     <!-- <v-toolbar
               style="background-color:#363940;"
                dark
                flat
              >
                <v-toolbar-title class="white--text">Login </v-toolbar-title>
                <div class="flex-grow-1"></div>
                <v-spacer></v-spacer>
                
              </v-toolbar> -->
             
              <v-card-title style="font-weight:bold;font-size:18px;">User Login</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-form>
                  <v-text-field
                    label="Login"
                    name="login"
                    v-model="username"
                    :rules="[() => !!username || 'This field is required']"
                    prepend-icon="person"
                    type="text"
                  ></v-text-field>

                  <v-text-field
                    ref="password"
                  v-model="password"
                  :rules="[() => !!password || 'This field is required']"
                  :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                  :type="showPassword ? 'text' : 'password'"
                  prepend-icon="mdi-lock"
                  label="Password"
                  placeholder="*********"
                  counter
                  required
                  @keydown.enter="login"
                  @click:append="showPassword = !showPassword"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                
                <v-btn class="mx-auto green darken-2" color="primary" @click="login">Sign In</v-btn>
              </v-card-actions>
               <v-snackbar
              v-model="snackbar"
              :color="color"
              :top='true'
            >
              {{ errorMessages }}
              <v-btn
                dark
                flat
                @click="snackbar = false"
              >
                Close
              </v-btn>
            </v-snackbar>

                  </v-container>
             
            </v-card>

            </v-flex>
          </v-layout>
            
          <!-- </v-col>
        </v-row> -->
            
         


        </v-container>
        
        </div>
</template>

<script>
import axios from 'axios'
  export default {
    props: {
      source: String,
    },
    data: function(){
      return{
        drawer: null,
        username:'',
        password:'',
        snackbar: false,
         color: 'general',
          errorMessages: 'Incorrect login credentials',
          showPassword: false
      }
      
    },
    methods: {
    login: function () {
      let username = this.username
      let password = this.password
      this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/dashboard'))
        .catch(err => {
        console.log(err)
        this.snackbar= true
        }
        )
    }
  }
  }
</script>
<style >
.log{
  background-image: url('../assets/img/frame.jpg');
  background-size: cover;
  height:700px;
  background-color:rgb(90, 133, 253);
}
</style>