<template>
  <!-- <v-row> -->
    <!-- <v-col cols="12" sm="6" offset-sm="3"> -->
      <!-- <v-card height="200px"> -->
        <!-- <v-card-title class="blue white--text"> -->
          <!-- <span class="headline">Menu</span> -->

          <!-- <v-spacer></v-spacer> -->

          <v-toolbar  style="background-color:#a30b00;" small  dense floating>
            <v-toolbar-title style="color:#faee02;" >QVRS</v-toolbar-title>
            <v-toolbar-items class="hidden-sm-and-down" >
                <v-layout  row >
                <v-btn  flat small  class=" mx-2 white--text" v-for="link in items" :key="link.text" router :to="link.route">
                    <span>{{link.text}}</span>
                </v-btn>
                </v-layout>
            </v-toolbar-items>
            <v-spacer></v-spacer>
                <p></p>
                 <v-menu class="hidden-md-and-up">
                    <v-toolbar-side-icon slot="activator" class="white--text"   ></v-toolbar-side-icon>
                    <v-list>
                    <v-list-tile v-for="link in items" :key="link.text" router :to="link.route">
                        <v-list-tile-content>
                        <v-list-tile-title class="black--text">{{ link.text}}</v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>   
                    </v-list>
                </v-menu>
             
               
					
			
        </v-toolbar>

          <!-- <v-menu bottom left>
            <template v-slot:activator="{ on }">
              <v-btn
                dark
                icon
                v-on="on"
                class="black"
              >
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-tile
                v-for="item in items"
                :key="item.text"
                
                router 
                :to="item.route"
               
              >
                <v-list-tile-content>
                <v-btn  flat small  class=" mx-2 black--text" >
                    <span>{{item.text}}</span>
                    </v-btn>
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
          </v-menu> -->
        <!-- </v-card-title> -->

        
      <!-- </v-card> -->
    <!-- </v-col> -->
  <!-- </v-row> -->
</template>
<script>
  export default {
    data: () => ({
       items: [
         { text:'Home', route:'/dashboard'},
       { text:'Map', route:'/map_dashboard'},
                { text:'Graph', route:'/bar_dashboard'},
                { text:'Candidates',route:'/pie_dashboard'},
                 { text:'Overall view',route:'votes_dashboard'},
               
      ],
    }),
  }
</script>