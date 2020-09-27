<template>
  <!-- <v-row> -->
  <!-- <v-col cols="12" sm="6" offset-sm="3"> -->
  <!-- <v-card height="200px"> -->
  <!-- <v-card-title class="blue white--text"> -->
  <!-- <span class="headline">Menu</span> -->

  <!-- <v-spacer></v-spacer> -->

  <v-toolbar style="background-color:#a30b00;" small dense>
    <v-toolbar-title style="color:#faee02;" class="tie"
      >ELECTIONS RESULTS PORTAL</v-toolbar-title
    >
    <v-divider class="mx-4 white" vertical></v-divider>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-layout row>
        <v-btn
          flat
          small
          class="mx-2 white--text"
          v-for="link in items"
          :key="link.text"
          router
          :to="link.route"
        >
          <span>{{ link.text }}</span>
        </v-btn>
      </v-layout>
    </v-toolbar-items>
    <v-spacer></v-spacer>
    <p></p>
    <v-menu class="hidden-md-and-up">
      <v-toolbar-side-icon
        slot="activator"
        class="white--text"
      ></v-toolbar-side-icon>
      <v-list style="background-color:#a30b00;">
        <v-list-tile
          v-for="link in items"
          :key="link.text"
          router
          :to="link.route"
        >
          <v-list-tile-content>
            <v-btn
              flat
              small
              style="background-color:black;"
              class="white--text"
              >{{ link.text }}</v-btn
            >
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
  </v-menu>-->
  <!-- </v-card-title> -->

  <!-- </v-card> -->
  <!-- </v-col> -->
  <!-- </v-row> -->
</template>
<script>
export default {
  data: () => ({
    items: [
      { text: "Home", route: "/dashboard" },
      { text: "Analysis", route: "/map_dashboard" },
      // { text: "Graph", route: "/bar_dashboard" },
      { text: "Feeds", route: "/pie_dashboard" },
      { text: "Reports", route: "votes_dashboard" },
    ],
  }),
};
</script>
<style scoped>
@media screen and (min-width: 601px) {
  .tie {
    font-size: 20px;
  }
}

@media screen and (max-width: 600px) {
  .tie {
    font-size: 10px;
  }
}
</style>
