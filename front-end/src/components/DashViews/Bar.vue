
<template>
  <section class="charts">
    <v-layout wrap>
      <v-flex md12 sm12>
        <div v-if="soptions.series[0].data">
          <vue-highcharts :options="soptions" :highcharts="Highcharts" class="bar"></vue-highcharts>
        </div>
      </v-flex>
    </v-layout>
  </section>
</template>
<script>
import VueHighcharts from "./VueHighcharts.vue";
import Highcharts3D from "highcharts/highcharts-3d";
import Highcharts from "highcharts";
import axios from "axios";
import navis from "./NavBar";

Highcharts3D(Highcharts);

export default {
  props: ["data", "options"],
  components: {
    VueHighcharts,
    navis
  },

  data() {
    return {
      stuuf: null,
      data: null,
      soptions: {
        chart: {
          renderTo: "container",
          type: "column",
          height: 400,
          options3d: {
            enabled: true,
            alpha: 15,
            beta: 15,
            depth: 50,
            viewDistance: 25
          }
        },
        title: {
          text: null
        },

        plotOptions: {
          column: {
            depth: 50
          }
        },

        xAxis: {
          categories: [
            "ABED",
            "AMAMA",
            "BARYA",
            "BENON",
            "KIZZA",
            "JOSEPH",
            "MAUREEN",
            "YOWERI"
          ]
        },
        yAxis: {
          min: 0,
          title: {
            text: "Votes"
          }
        },
        credits: {
          enabled: false
        },
        series: [
          {
            data: this.stuuf,

            colorByPoint: true,
            name: "Total Votes"
            // showInLegend: false
          }
        ]
      },
      Highcharts
    };
  },
  created() {
    axios
      .get("http://127.0.0.1:5000/GetPresidentailCandidates", {
        headers: {
          "x-access-token": localStorage.getItem("token")
        }
      })
      .then(response => {
        let p = response.data;
        this.soptions.series[0].data = [
          {
            name: "ABED",
            y: p.cand1,
            color: "#eb3434"
          },
          {
            name: "AMAMA",
            y: p.cand2,
            color: "#00ab1f"
          },
          {
            name: "BARYA",
            y: p.cand3,
            color: "#52024a"
          },
          {
            name: "BENON",
            y: p.cand4,
            color: "#3e4a35"
          },
          {
            name: "KIZZA",
            y: p.cand5,
            color: "#0200D0"
          },
          {
            name: "JOSEPH",
            y: p.cand6,
            color: "#adaca8"
          },
          {
            name: "MAUREEN",
            y: p.cand7,
            color: "#080a09"
          },
          {
            name: "YOWERI",
            y: p.cand8,
            color: "#fce803"
          }
        ];

        this.data = response.data;

        // console.log(this.soptions.series[0].data)
      });
  }
};
</script>

<style scoped>
/* .bar {
  min-height: 600px;
} */
</style>