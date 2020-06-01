<template>
<div >
    <v-container fluid>
        <v-layout row wrap justify-space-around>

         <v-flex xs12 md12>
        <v-card  height="5"
         
          class="black mx-auto">
          

        </v-card>
      </v-flex>
       <v-flex xs12 md12>
        <v-card  height="5"
         
          class="yellow accent-2 mx-auto">

        </v-card>
      </v-flex>
       <v-flex xs12 md12>
        <v-card  height="5"
         
          class=" red accent-4 mx-auto">

        </v-card>
      </v-flex>

    </v-layout>
    <v-layout>
      <v-flex>
        <v-btn small style="background-color:#2c566b;" class="right  white--text" @click="logout()">LogOut</v-btn>
      </v-flex>
    </v-layout>
   
    
    
    <v-layout>
      <v-flex xs12 md12>
        <v-card
    class="mx-auto"
    height="450"
    max-width="400"
    style="margin-top:20px;background-color:#2c566b;"
  >
    <!-- <v-navigation-drawer
      absolute
      dark
      src="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
      permanent
    > -->
      <v-list>
        <v-list-tile
          v-for="link in items"
          :key="link.text"
          link
        router 
        :to="link.route"
        >
          

          <v-list-tile-content>
           <v-btn  flat small  class=" mx-2 black--text" >
            <span>{{link.text}}</span>
            </v-btn>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    <!-- </v-navigation-drawer> -->
    <div style="margin-top:4%;margin-left:30%;">
        <v-avatar size="170" >
                <img
                    src="@/assets/img/vote.png"
                    alt="EC"
                   
                >
                </v-avatar>
        
    </div>
    
  </v-card>

      </v-flex>
    </v-layout>
    
   </v-container>
    
</div>
  
</template>
<script>

  export default {
    
    data: () => ({
      items: [
       { text:'Map', route:'/map_dashboard'},
                { text:'Graph', route:'/bar_dashboard'},
                { text:'Candidates',route:'/pie_dashboard'},
                 { text:'Overall view',route:'votes_dashboard'},
               
      ],
    }),
    methods:{
              logout() {
				this.$store.dispatch("logout").then(() => {
					this.$router.push("/");
				});
            },
    }
  }
</script>