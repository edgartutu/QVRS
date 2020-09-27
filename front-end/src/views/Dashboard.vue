<template>
  <div>
    <v-layout wrap v-sticky>
      <v-toolbar style="background-color:#a30b00;" flat small dense>
        <v-avatar tile size="40">
          <img src="@/assets/img/flag.png" />
        </v-avatar>
        <v-toolbar-title
          style="color:white;font-family:Arial, Helvetica, sans-serif"
          class="head"
          >ELECTIONS RESULTS PORTAL</v-toolbar-title
        >
        <v-spacer></v-spacer>
        <span>
          <v-avatar size="50">
            <img src="@/assets/img/EC.jpg" />
          </v-avatar>
        </span>

        <v-menu class="hidden-md-and-up">
          <v-toolbar-side-icon
            slot="activator"
            class="white--text"
          ></v-toolbar-side-icon>
          <v-list class="pa-3" style="background-color:#a30b00;">
            <v-list-group value="true">
              <template v-slot:activator>
                <v-list-tile-title
                  style="font-family:Palatino Linotype,Book Antiqua, Palatino, serif;font-size:10px;"
                  class="white--text"
                  >RESULTS</v-list-tile-title
                >
              </template>

              <v-layout>
                <v-flex md6>
                  <v-btn
                    small
                    style="font-size:10px;"
                    class="black white--text"
                    @click="presidential()"
                    >Presidential</v-btn
                  >
                </v-flex>
                <v-flex md6>
                  <v-btn small style="font-size:10px;" class="black white--text"
                    >Parliamentary</v-btn
                  >
                </v-flex>
              </v-layout>
            </v-list-group>
            <v-list-group value="true" style="background-color:#a30b00;">
              <template v-slot:activator>
                <v-list-tile-title
                  style="font-family:Palatino Linotype,Book Antiqua, Palatino, serif;font-size:10px;"
                  class="white--text"
                  >COMPARE</v-list-tile-title
                >
              </template>
            </v-list-group>
            <v-list-group value="true" style="background-color:#a30b00;">
              <template v-slot:activator>
                <v-list-tile-title
                  style="font-family:Palatino Linotype,Book Antiqua, Palatino, serif;font-size:10px;"
                  class="white--text"
                  >REPORTS</v-list-tile-title
                >
              </template>
            </v-list-group>
            <v-list-group value="true" style="background-color:#a30b00;">
              <template v-slot:activator>
                <v-list-tile-title
                  style="font-family:Palatino Linotype,Book Antiqua, Palatino, serif;font-size:10px;"
                  class="white--text"
                  >VOTER TURNOUT</v-list-tile-title
                >
              </template>
            </v-list-group>
          </v-list>
        </v-menu>
      </v-toolbar>

      <v-layout wrap justify-space-below>
        <!-- <v-flex md12 sm12> -->
        <!-- <img style="width:100%;height:260px;" max-height="300"  src="@/assets/img/uga.jpg" > -->
        <!-- <v-card style="width:100%;height:260px;" ></v-card> -->
        <!-- <div class="centered" >2016 GENERAL ELECTION</div> -->

        <!-- </v-flex> -->
        <v-flex md12 sm12>
          <v-card
            style="background-color:black;"
            small
            dense
            class="hidden-sm-and-down"
          >
            <!-- <v-toolbar-items class="hidden-sm-and-down" > -->
            <v-layout row>
              <v-flex md2>
                <!-- <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">-->
                <v-btn
                  flat
                  v-bind="attrs"
                  v-on="on"
                  @click="home"
                  class="mx-auto white--text"
                >
                  <span>HOME</span>
                </v-btn>
                <!-- </template>
                <br />
                <v-card
                  width="350"
                  style="background-color:#a30b00;"
                  small
                  dense
                  class="hidden-sm-and-down"S
                >
                  <v-layout>
                    <v-flex md6>
                      <v-btn class="black white--text" @click="presidential()">Presidential</v-btn>
                    </v-flex>
                    <v-flex md6>
                      <v-btn class="black white--text">Parliamentary</v-btn>
                    </v-flex>
                  </v-layout>
                </v-card>
                </v-menu>-->
              </v-flex>
              <v-flex md2>
                <!-- <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">-->
                <v-btn
                  flat
                  v-bind="attrs"
                  v-on="on"
                  @click="presidential()"
                  class="mx-auto white--text"
                >
                  <span>Presidential</span>
                </v-btn>
                <!-- </template>
                <v-card></v-card>
                </v-menu>-->
              </v-flex>
              <v-flex md2>
                <!-- <v-menu offset-y>
                <template v-slot:activator="{ on, attrs }">-->
                <v-btn
                  flat
                  v-bind="attrs"
                  v-on="on"
                  class="mx-auto white--text"
                >
                  <span>Parliamentary</span>
                </v-btn>
                <!-- </template>
                <v-card></v-card>
                </v-menu>-->
              </v-flex>
              <v-flex md2>
                <v-menu offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      flat
                      v-bind="attrs"
                      v-on="on"
                      class="mx-auto white--text"
                    >
                      <span>Compare</span>
                    </v-btn>
                  </template>
                  <v-card></v-card>
                </v-menu>
              </v-flex>
            </v-layout>
            <!-- </v-toolbar-items> -->
          </v-card>
        </v-flex>
      </v-layout>
    </v-layout>

    <v-layout justify-space-around>
      <v-flex>
        <v-card flat class="blue-grey lighten-4">
          <div
            style=" text-align: center;font-size:50px;color:#a30b00;font-family:Courier New,Courier,monospace;"
          >
            Election Results As At 2016
          </div>
        </v-card>
      </v-flex>
    </v-layout>
    <br />
    <v-container fluid>
      <v-layout wrap justify-space-around>
        <v-flex md10 sm12>
          <p id="demo"></p>
          <div
            style="font-weight:bold;font-size:25px;font-family:Palatino Linotype,Book Antiqua, Palatino, serif"
          >
            2016 General Election Results
          </div>
          <p>
            Uganda held its first ever televised presidential debate on 15
            January 2016.The debate took place at the Serena Hotel in Kampala
            and was led by BBC Newsday presenter Alan Kasujja and KTN journalist
            Nancy Kacungira. The presidential debate was attended by all
            presidential aspirants
          </p>
          <div
            style="font-weight:bold;font-size:25px;font-family:Palatino Linotype,Book Antiqua, Palatino, serif"
          >
            Presidential Election Results
          </div>
          <p>
            The 2016 presidential results presented by district performances.
          </p>
          <v-data-table
            class="fb-table-elem"
            :headers="headers"
            :items="items"
            :items-per-page="7"
            item-key="name"
          >
            <template slot="items" slot-scope="{ item, index }">
              <td class="datatable-cell-wrapper">
                <v-dialog v-model="dialog" width="500">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      @click="(distro = item.name), general(index)"
                      v-bind="attrs"
                      v-on="on"
                      small
                      flat
                      v-model="distro"
                      style="color:#a30b00;"
                      >{{ item.name }}</v-btn
                    >
                  </template>
                  <!-- <v-layout>
                    <v-flex xs12 md10>
                      <div v-if="pieOptions.series[0].data">
                        <highcharts :options="pieOptions" class="charts"></highcharts>
                      </div>
                    </v-flex>
                  </v-layout>-->
                  <v-card height="400" class="card">
                    <v-card-title class="headline grey lighten-2" primary-title>
                      Percentage Scores In
                      <div v-if="result" style="margin-left:0.5em;">
                        {{ result["name"] }}
                      </div>
                      <div v-else>null</div>
                    </v-card-title>
                    <v-layout>
                      <v-flex xs12 md10>
                        <div v-if="pieOptions.series[0].data">
                          <highcharts
                            :options="pieOptions"
                            class="charts"
                          ></highcharts>
                        </div>
                      </v-flex>
                    </v-layout>
                  </v-card>
                </v-dialog>
              </td>
              <td class="datatable-cell-wrapper">
                <div>{{ item.cand1 }}</div>
              </td>
              <td class="datatable-cell-wrapper">{{ item.cand2 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand3 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand4 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand5 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand6 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand7 }}</td>
              <td class="datatable-cell-wrapper">{{ item.cand8 }}</td>
            </template>
          </v-data-table>
        </v-flex>
        <v-flex md2 sm12>
          <v-card>
            <v-container>
              <div style="font-weight:bold;" class="mx-auto">
                ElECTORAL BODY
              </div>
              <p></p>
              presented By Uganda Electoral Commission
            </v-container>
          </v-card>
          <br />
          <v-card>
            <v-container>
              <div style="font-weight:bold;" class="mx-auto">JUST IN</div>
              <p>Eight candidates contested the presidential elections</p>
            </v-container>
          </v-card>
          <br />
          <v-card>
            <v-container>
              <div style="font-weight:bold;" class="mx-auto">NEWS</div>
              <p>User Guide</p>
              <small>
                The Electoral Commission has approved guidelines to apply during
                the election of village and parish/ward administrative unit
                chairpersons, and nomination and approval of executive committee
                members
              </small>
            </v-container>
          </v-card>
        </v-flex>
      </v-layout>
      <br />
    </v-container>

    <v-footer class="blue-grey lighten-4">
      <v-spacer></v-spacer>
      <div style=" text-align: center;">
        Copyright © 2020 Globe Trendz All rights reserved
      </div>
    </v-footer>

    <!-- <v-container fluid>
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
    
    </v-container>-->
  </div>
</template>
<script>
import axios from "axios";
import Sticky from "vue-sticky-directive";
import Highcharts from "highcharts";
import VueHighcharts from "../components/DashViews/VueHighcharts";
import VueStickyDirective from "@renatodeleao/vue-sticky-directive";

export default {
  components: {
    VueHighcharts,
  },
  directives: {
    Sticky,
    VueStickyDirective,
  },
  data() {
    return {
      isNavSticky: true,
      dialog: false,
      distro: "",
      itemz: [
        { text: "Presidential", route: "/map_dashboard" },
        { text: "Parliamentary", route: "/bar_dashboard" },
        // { text:'REPORTS',route:'/pie_dashboard'},
        //  { text:'TURNOUT',route:'votes_dashboard'},
      ],
      headers: [
        {
          text: "DistrictName",
          align: "left",
          sortable: true,
          value: "name",
        },
        { text: "ABED", value: "cand1" },
        { text: "AMAMA", value: "cand2" },
        { text: "BARYA", value: "cand3" },
        { text: "BENON", value: "cand4" },
        { text: "KIZZA", value: "cand5" },
        { text: "JOSEPH", value: "cand6" },
        { text: "MAUREEN", value: "cand7" },
        { text: "YOWERI", value: "cand8" },
      ],
      items: [],
      result: [],
      now: null,
      pieOptions: {
        chart: {
          type: "pie",
          width: 500,
          height: 300,
        },
        title: {
          text: null,
        },
        credits: {
          enabled: false,
        },
        series: [
          {
            data: this.now,
            name: "Votes",

            dataLabels: {
              format: "<b>{point.name}</b> {point.percentage:.1f}%",
            },
          },
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500,
              },
              pieOptions: {
                legend: {
                  align: "center",
                  verticalAlign: "bottom",
                  layout: "horizontal",
                },
                yAxis: {
                  labels: {
                    align: "left",
                    x: 0,
                    y: -5,
                  },
                  title: {
                    text: null,
                  },
                },
                subtitle: {
                  text: null,
                },
                credits: {
                  enabled: false,
                },
              },
            },
          ],
        },
      },
    };
  },

  // created() {
  //   const Sticky = {
  //     bind(el, binding) {
  //       setStyle(el, binding.value);
  //     },
  //     componentUpdated(el, binding) {
  //       setStyle(el, binding.value);
  //     }
  //   };

  //   const setStyle = (el, values) => {
  //     const defaults = {
  //       isSticky: true,
  //       offset: 200
  //     };

  //     const isSticky =
  //       values && values.isSticky !== undefined
  //         ? values.isSticky
  //         : defaults.isSticky;

  //     if (isSticky) {
  //       const offset = (values && values.offset) || defaults.offset;

  //       el.style.top = `${offset}px`;
  //       el.style.position = "sticky";
  //       el.style.position = "-webkit-sticky"; /* Safari */
  //     } else {
  //       el.style.cssText = null;
  //     }
  //   };
  // },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/SendMapData", {
        headers: {
          "x-access-token": localStorage.getItem("token"),
        },
      })
      .then((response) => {
        this.items = response.data;

        // console.log(this.items)
      });

    var d = new Date();
    document.getElementById("demo").innerHTML = d;
  },
  methods: {
    home() {
      window.location.reload();
    },
    general(index) {
      axios
        .post(
          "http://127.0.0.1:5000/Candidates",
          {
            Category: "PRESIDENTIAL",
            District: this.distro,
            Subconty: "",
            PARISH_NAME: "",
          },
          {
            headers: {
              "x-access-token": localStorage.getItem("token"),
            },
          }
        )
        .then((response) => {
          let d = response.data;
          this.result = response.data;

          this.pieOptions.series[0].data = [
            {
              name: "FDC",
              color: "#0200D0",
              y: parseInt(d.cand5, 10),
            },
            {
              name: "NRM",
              color: "#ffe51f",
              y: parseInt(d.cand8, 10),
            },
            {
              name: "AMAMA",
              color: "#00ab1f",
              y: parseInt(d.cand2, 10),
            },
            {
              name: "ABED",
              color: "#eb3434",
              y: parseInt(d.cand1, 10),
            },
            {
              name: "BARYA",
              color: "#52024a",
              y: parseInt(d.cand3, 10),
            },
            {
              name: "BENON",
              color: "#3e4a35",
              y: parseInt(d.cand4, 10),
            },
            {
              name: "JOSEPH",
              color: "#adaca8",
              y: parseInt(d.cand6, 10),
            },
            {
              name: "KYALYA",
              color: "#080a09",
              y: parseInt(d.cand7, 10),
            },
          ];

          console.log(this.result);
        });
    },
    logout() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/");
      });
    },
    presidential() {
      this.$router.push("/map_dashboard");
    },
  },
  beforeRouteLeave(to, from, next) {
    window.setTimeout(next, 300);
    this.dialog = false;
  },
};
</script>
<style>
.charts {
  display: table-cell;
  position: absolute;
  width: 100%;
}
@media screen and (min-width: 601px) {
  .head {
    font-size: 22px;
  }
}

@media screen and (max-width: 600px) {
  .head {
    font-size: 11px;
  }
}

.centered {
  position: absolute;
  color: white;
  top: 28%;
  left: 50%;
  transform: translate(-50%, -50%);

  font-family: "Segoe Regular" !important;
}
@media screen and (min-width: 601px) {
  .centered {
    font-size: 50px;
  }
}

@media screen and (max-width: 600px) {
  .centered {
    font-size: 22px;
  }
}

@media screen and (max-width: 600px) {
  .card {
    width: 500px;
  }
}
</style>
