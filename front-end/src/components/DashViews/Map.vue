<template>
  <div>
    <v-card flat>
      <v-layout row wrap justify-space-around>
        <v-flex xs12 md12>
          <v-card height="6" class="black mx-auto"></v-card>
        </v-flex>
        <v-flex xs12 md12>
          <v-card height="5" class="yellow accent-2 mx-auto"></v-card>
        </v-flex>
        <v-flex xs12 md12>
          <v-card height="5" class="red accent-4 mx-auto"></v-card>
        </v-flex>
        <!-- <navis/> -->
      </v-layout>
      <v-layout>
        <v-flex xs12 md12>
          <navis />
        </v-flex>
      </v-layout>
      <v-layout row wrap justify-space-around>
        <v-flex xs12 md3>
          <!-- <v-hover v-slot:default="{ hover }"> -->
          <v-card class="pa-3" flat outline max-width="800" height="300px">
            <v-card class="register-card">
              <h5>Registered Voters</h5>
              <smallapex />
            </v-card>
            <v-card class="register-card">
              <h5>Total TurnOut</h5>
              <p>10M</p>
            </v-card>
            <v-card class="register-card">
              <h5>Valid Votes</h5>
              <p>9,851,812</p>
            </v-card>
          </v-card>
          <!-- </v-hover> -->
          <!-- <v-hover v-slot:default="{ hover }"> -->
          <v-card class="pa-3" flat outline max-width="800" height="300px">
            <v-card class="register-card">
              <h5>NationWide Score</h5>
              <smaller />
            </v-card>
          </v-card>
          <!-- </v-hover> -->
        </v-flex>
        <v-flex xs10 md9>
          <!-- <v-hover v-slot:default="{ hover }"> -->
          <v-card flat outline max-width="1000" height="600px">
            <v-layout>
              <v-flex md2 xs12>
                <v-btn class="red white--text" small @click="fetchEventsList()">2016 results</v-btn>
              </v-flex>
              <v-flex md10 xs12>
                <div class="ug">UGANDA PRESIDENTAIL ELECTION 2016 RESULTS</div>
              </v-flex>
            </v-layout>
            <v-layout wrap>
              <v-flex x12 md12>
                <highcharts :constructor-type="'mapChart'" :options="options" class="map"></highcharts>
              </v-flex>
            </v-layout>

            <!-- <div  style=" font-family: Avenir;color:#031273;font-size: 30px;">Summary of complaints </div> -->
          </v-card>

          <!-- </v-hover > -->
        </v-flex>
      </v-layout>
      <!-- <v-layout>
             <v-flex xs12 md12>
               <p style="font-size:20px;padding-left:32%;font-family:verdana;">UGANDA PRESIDENTAIL ELECTION 2016 RESULTS</p>
        </v-flex>


      </v-layout>-->

      <!-- <v-layout row wrap justify-space-around> -->
      <!-- <v-flex style="margin-top:20%;"> -->

      <!-- </v-flex> -->
      <!-- <v-flex xs12 md11> -->
      <!-- <div  v-if="options.series[1].data">

      </div>-->

      <!-- </v-flex > -->
      <v-flex sm2 class="cube">
        <box />
      </v-flex>

      <!-- </v-layout> -->
    </v-card>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import mapDatah from "../worldmap.js";
import axios from "axios";
import box from "./Box";
import navis from "./NavBar";
import smaller from "./SmallPie";
import smallapex from "../../views/Radial";

export default {
  components: {
    box,
    navis,
    smaller,
    smallapex
  },
  data() {
    return {
      Highcharts: Highcharts,
      stuff: null,
      timer: "",
      keys: [
        "ug-2789",
        "ug-2745",
        "ug-7056",
        "ug-7054",
        "ug-1682",
        "ug-7058",
        "ug-2787",
        "ug-7049",
        "ug-2763",
        "ug-2746",
        "ug-1684",
        "ug-7086",
        "ug-2780",
        "ug-7064",
        "ug-7073",
        "ug-7081",
        "ug-7067",
        "ug-2776",
        "ug-7083",
        "ug-2748",
        "ug-2770",
        "ug-3383",
        "ug-2781",
        "ug-2782",
        "ug-7069",
        "ug-7074",
        "ug-7078",
        "ug-2766",
        "ug-7070",
        "ug-2764",
        "ug-2771",
        "ug-3386",
        "ug-1680",
        "ug-3387",
        "ug-2744",
        "ug-2788",
        "ug-3392",
        "ug-2772",
        "ug-1678",
        "ug-2595",
        "ug-1683",
        "ug-7068",
        "ug-2754",
        "ug-1681",
        "ug-3385",
        "ug-3394",
        "ug-2775",
        "ug-3384",
        "ug-2785",
        "ug-1679",
        "ug-2774",
        "ug-2755",
        "ug-7082",
        "ug-3388",
        "ug-7052",
        "ug-3393",
        "ug-7051",
        "ug-2747",
        "ug-7053",
        "ug-2786",
        "ug-1677",
        "ug-7084",
        "ug-7072",
        "ug-7060",
        "ug-2773",
        "ug-2762",
        "ug-2765",
        "ug-7076",
        "ug-2758",
        "ug-7065",
        "ug-7066",
        "ug-2779",
        "ug-2753",
        "ug-3382",
        "ug-2768",
        "ug-2783",
        "ug-2778",
        "ug-3391",
        "ug-7062",
        "ug-2760",
        "ug-2790",
        "ug-2751",
        "ug-1690",
        "ug-2759",
        "ug-1687",
        "ug-2791",
        "ug-2761",
        "ug-2756",
        "ug-7075",
        "ug-1685",
        "ug-7057",
        "ug-2750",
        "ug-7080",
        "ug-7059",
        "ug-3389",
        "ug-2749",
        "ug-7055",
        "ug-2769",
        "ug-2767"
      ],
      names: [
        "ABIM",
        "ADJUMANI",
        "AGAGO",
        "ALEBTONG",
        "AMOLATAR",
        "AMUDAT",
        "AMURIA",
        "AMURU",
        "APAC",
        "ARUA",
        "BUDAKA",
        "BUDUDA",
        "BUGIRI",
        "BUHWEJU",
        "BUIKWE",
        "BUKEDEA",
        "BUKOMANSIMBI",
        "BUKWO",
        "BULAMBULI",
        "BULIISA",
        "BUNDIBUGYO",
        "BUSHENYI",
        "BUSIA",
        "BUTALEJA",
        "BUTAMBALA",
        "BUVUMA",
        "BUYENDE",
        "DOKOLO",
        "GOMBA",
        "GULU",
        "HOIMA",
        "IBANDA",
        "IGANGA",
        "ISINGIRO",
        "JINJA",
        "KAABONG",
        "KABALE",
        "KABAROLE",
        "KABERAMAIDO",
        "KALANGALA",
        "KALIRO",
        "KALUNGU",
        "KAMPALA",
        "KAMULI",
        "KAMWENGE",
        "KANUNGU",
        "KAPCHORWA",
        "KASESE",
        "KATAKWI",
        "KAYUNGA",
        "KIBAALE",
        "KIBOGA",
        "KIBUKU",
        "KIRUHURA",
        "KIRYANDONGO",
        "KISORO",
        "KITGUM",
        "KOBOKO",
        "KOLE",
        "KOTIDO",
        "KUMI",
        "KWEEN",
        "KYANKWANZI",
        "KYEGEGWA",
        "KYENJOJO",
        "LAMWO",
        "LIRA",
        "LUUKA",
        "LUWEERO",
        "LWENGO",
        "LYANTONDE",
        "MANAFWA",
        "MARACHA",
        "MASAKA",
        "MASINDI",
        "MAYUGE",
        "MBALE",
        "MBARARA",
        "MITOOMA",
        "MITYANA",
        "MOROTO",
        "MOYO",
        "MPIGI",
        "MUBENDE",
        "MUKONO",
        "NAKAPIRIPIRIT",
        "NAKASEKE",
        "NAKASONGOLA",
        "NAMAYINGO",
        "NAMUTUMBA",
        "NAPAK",
        "NEBBI",
        "NGORA",
        "NTOROKO",
        "NTUNGAMO",
        "NWOYA",
        "OTUKE",
        "OYAM",
        "PADER"
      ],
      percent: [
        3.632819,
        1.352952,
        0.848625,
        0.114415,
        0.352152,
        47.48752,
        0.462477,
        -0.3817,
        0.46328,
        0.690289,
        0.694617,
        0.623865,
        0.730145,
        6.05202,
        0.312545,
        0.587265,
        0.216563,
        3.806384,
        1.23191,
        1.376142,
        5.898241,
        1.319989,
        0.331563,
        0.429698,
        0.190639,
        0.473708,
        4.944796,
        0.179169,
        2.192218,
        -0.35401,
        2.152799,
        3.990369,
        0.625335,
        2.040064,
        0.074262,
        20.34601,
        1.012579,
        2.431825,
        0.37253,
        0.25755,
        4.513549,
        0.292961,
        -0.53038,
        1.472831,
        5.847225,
        0.960156,
        1.147714,
        -0.26596,
        1.033686,
        0.386811,
        3.938638,
        2.207782,
        1.364398,
        10.24476,
        2.648207,
        7.619963,
        0.144251,
        1.360548,
        0.377064,
        25.00613,
        0.313869,
        1.673185,
        3.167131,
        6.014366,
        5.65897,
        0.106516,
        -0.28999,
        1.697398,
        0.344699,
        0.765501,
        3.107084,
        0.732434,
        1.12273,
        -0.09777,
        1.555818,
        0.766537,
        -0.06882,
        1.52719,
        1.166465,
        0.793949,
        14.93701,
        0.71348,
        0.334851,
        2.811822,
        0.041879,
        25.97802,
        2.593925,
        5.127969,
        0.533916,
        1.734485,
        30.00851,
        1.487734,
        -0.08872,
        2.822207,
        1.210964,
        0.451009,
        1.211375,
        0.198403,
        -0.14276
      ],
      mapData: mapDatah,
      options: {
        chart: {
          type: "map",
          map: mapDatah,
          height: 540,

          // borderWidth: 1,
          // borderColor: 'silver',
          // borderRadius: 3,
          // shadow: true,
          backgroundColor: null,

          animation: {
            duration: 1000
          }

          // renderTo: 'container',
        },
        credits: {
          enabled: false
        },

        title: {
          text: null
        },
        // subtitle: {
        //     text: 'Source map: <a href="http://code.highcharts.com/mapdata/countries/ug/ug-all.js">Uganda</a>'
        // },

        legend: {
          title: {
            text:
              'Select candidate<br/><span style="font-size: 9px; color: #666; font-weight: normal">(Click to hide)</span>',
            style: {
              fontStyle: "verdana"
            }
          },
          align: "left",
          verticalAlign: "top",

          floating: true,
          borderRadius: 10,
          borderWidth: 1,
          layout: "vertical",
          itemMarginTop: 5,
          itemMarginBottom: 5,
          itemStyle: {
            lineHeight: "14px"
          },
          itemHoverStyle: {
            color: "#FF0000"
          },
          valueDecimals: 0,
          symbolPadding: 20,
          symbolWidth: 20,
          backgroundColor:
            // theme
            (Highcharts.defaultOptions &&
              Highcharts.defaultOptions.legend &&
              Highcharts.defaultOptions.legend.backgroundColor) ||
            "rgba(255, 255, 255, 0.85)"
        },

        mapNavigation: {
          enabled: true,
          enableButtons: true,
          buttonOptions: {
            align: "right"
          }
        },

        colorAxis: {
          dataClasses: [
            {
              from: -55,
              to: -45,
              color: "#0200D0",
              name: "KIZZA"
            },
            {
              from: -85,
              to: -75,
              color: "#fce803",
              name: "YOWERI"
            },
            ,
            {
              from: -15,
              to: -5,
              color: "#eb3434",
              name: "ABED"
            },
            {
              from: -35,
              to: -25,
              color: "#52024a",
              name: "BARYA"
            },
            {
              from: -45,
              to: -35,
              color: "#3e4a35",
              name: "BENON"
            },
            {
              from: -65,
              to: -55,
              color: "#adaca8",
              name: "JOSEPH"
            },
            {
              from: -75,
              to: -65,
              color: "#080a09",
              name: "KYALYA"
            },
            {
              from: -25,
              to: -15,
              color: "#00ab1f",
              name: "AMAMA"
            }
          ]
        },

        series: [
          {
            data: this.stuff,
            allowPointSelect: true,
            joinBy: "hc-key",
            dataLabels: {
              enabled: true,
              color: "#020536",
              format: "{point.name}",
              style: {
                textTransform: "uppercase",
                fontWeight: "bold"
              }
            },
            name: "Results For",
            point: {
              events: {
                select: function(e) {
                  var row = this.options.row,
                    $div = $("<div></div>")
                      .draggable({
                        containment: "parent",
                        scrollSensitivity: 100
                      })
                      .dialog({
                        title: this.name,
                        width: 320,
                        height: 300
                      });

                  window.chart = new Highcharts.Chart({
                    chart: {
                      renderTo: $div[0],
                      type: "pie",
                      width: 290,
                      height: 240
                    },
                    title: {
                      text: null
                    },
                    credits: {
                      enabled: false
                    },
                    series: [
                      {
                        name: "Votes",
                        type: "pie",
                        data: [
                          {
                            name: "FDC",
                            color: "#0200D0",
                            y: parseInt(this.cand5, 10)
                          },
                          {
                            name: "NRM",
                            color: "#ffe51f",
                            y: parseInt(this.cand8, 10)
                          },
                          {
                            name: "AMAMA",
                            color: "#00ab1f",
                            y: parseInt(this.cand2, 10)
                          },
                          {
                            name: "ABED",
                            color: "#eb3434",
                            y: parseInt(this.cand1, 10)
                          },
                          {
                            name: "BARYA",
                            color: "#52024a",
                            y: parseInt(this.cand3, 10)
                          },
                          {
                            name: "BENON",
                            color: "#3e4a35",
                            y: parseInt(this.cand4, 10)
                          },
                          {
                            name: "JOSEPH",
                            color: "#adaca8",
                            y: parseInt(this.cand6, 10)
                          },
                          {
                            name: "KYALYA",
                            color: "#080a09",
                            y: parseInt(this.cand7, 10)
                          }
                        ],
                        dataLabels: {
                          format: "<b>{point.name}</b> {point.percentage:.1f}%"
                        }
                      }
                    ]
                  });
                }
              }
            },
            tooltip: {
              headerFormat: "<b>{series.name}</b><br>",
              pointFormat:
                " <b>{point.name}</b><br><p>ABED</p> : {point.cand1}<br><p>AMAMA</p> : {point.cand2}<br><p>BARYA</p> : {point.cand3}<br><p>BENON</p> : {point.cand4}<br><p>KIZZA</p> : {point.cand5} <br><p>JOSEPH</p> : {point.cand6}<br><p>KYALYA</p> : {point.cand7}<br><p>YOWERI</p> : {point.cand8}"
            },
            cursor: "pointer"
          },
          //                 {
          // type: 'pie',
          // name: 'Total Votes',
          // center: [180, 400],
          // size: 150,
          // showInLegend: false,
          // dataLabels: {
          //      format: '<b>{point.name}</b> {point.percentage:.1f}%'
          // }

          // },

          {
            name: "Separators",
            type: "mapline",
            nullColor: "silver",
            showInLegend: false,
            enableMouseTracking: false
          }
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 800
              },

              // chart:{
              //     height: 200
              // },

              chartOptions: {
                legend: {
                  align: "left",
                  verticalAlign: "bottom",
                  layout: "horizontal",
                  x: -10,
                  y: 27,
                  width: 300,
                  borderRadius: null,
                  borderWidth: null,
                  itemStyle: {
                    fontSize: "10px"
                  }
                },
                yAxis: {
                  labels: {
                    align: "left",
                    x: 0,
                    y: -5
                  },
                  title: {
                    text: null
                  }
                },
                subtitle: {
                  text: null
                },
                credits: {
                  enabled: false
                }
              }
            }
          ]
        }
      }
    };
  },
  mounted() {},
  created() {
    // this.fetchpie();
    // this.timer = setInterval(this.fetchpie, 300000);
    // this.fetchEventsList();
    // this.timer = setInterval(this.fetchEventsList, 300000);
    //        axios.get('http://127.0.0.1:5000 /SendMapData',
    // {
    //   headers: {
    //     'x-access-token': localStorage.getItem('token')
    // }
    // }
    // ).then(response =>{
    //   let result= response.data
    //   this.stuff=result
    //   console.log(this.stuff)
    // })
  },
  methods: {
    fetchEventsList() {
      axios
        .get("http://127.0.0.1:5000/SendMapData", {
          headers: {
            "x-access-token": localStorage.getItem("token")
          }
        })
        .then(response => {
          let result = response.data;
          this.stuff = result;
          //   console.log(this.stuff)
        });
    },
    fetchpie() {
      axios
        .get("http://127.0.0.1:5000/GetPresidentailCandidates", {
          headers: {
            "x-access-token": localStorage.getItem("token")
          }
        })
        .then(response => {
          let p = response.data;
          this.options.series[1].data = [
            {
              name: "FDC",
              color: "#0200D0",
              y: parseInt(p.cand5, 10)
            },
            {
              name: "NRM",
              color: "#ffe51f",
              y: parseInt(p.cand8, 10)
            },
            {
              name: "AMAMA",
              color: "#00ab1f",
              y: parseInt(p.cand2, 10)
            },
            {
              name: "ABED",
              color: "#eb3434",
              y: parseInt(p.cand1, 10)
            },
            {
              name: "BARYA",
              color: "#52024a",
              y: parseInt(p.cand3, 10)
            },
            {
              name: "BENON",
              color: "#3e4a35",
              y: parseInt(p.cand4, 10)
            },
            {
              name: "JOSEPH",
              color: "#adaca8",
              y: parseInt(p.cand6, 10)
            },
            {
              name: "KYALYA",
              color: "#080a09",
              y: parseInt(p.cand7, 10)
            }
          ];
        });
    }
    // cancelAutoUpdate() {
    //   clearInterval(this.timer);
    // }
  },
  // beforeDestroy() {
  //   clearInterval(this.timer);
  // },

  watch: {
    stuff(newData) {
      const data = this.options;
      data.series[0].data = newData;
      this.options = { ...data };
    }
  }
};
</script>
<style scoped>
.map {
  /* min-height: 600px; */
  /* height: 200%;
  width: 50%; */
}
.register-card p {
  font-size: 30px;
  font-weight: 500;
  text-align: center;
  padding: 7px;
  margin-bottom: 0px;
}
.register-card {
  margin-bottom: 10px;
}
.register-card h5 {
  background-color: #a30b00;
  padding: 2px 10px;
  color: white;
}

@media screen and (min-width: 601px) {
  .cube {
    margin-top: -20%;
    margin-left: 85%;
  }
}

@media screen and (max-width: 600px) {
  .cube {
    margin-top: -20%;
  }
}
@media screen and (min-width: 601px) {
  .ug {
    font-size: 20px;
    padding-left: 10%;
    font-family: verdana;
  }
}

@media screen and (max-width: 600px) {
  .ug {
    font-size: 10px;
  }
}
</style>
