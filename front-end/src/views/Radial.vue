<template>
  <v-layout class="radial-layout">
    <!-- <v-card class="vote-card"> -->
    <!-- <h5>Total Votes</h5> -->
    <div id="chart">
      <p class="low-rate">0</p>
      <apexchart type="radialBar" :options="chartOptions" :series="series"></apexchart>
      <p class="high-rate">15M</p>
    </div>
    <!-- </v-card> -->
    <!-- <v-card class="register-card">
              <h5>Valid Votes</h5>
              <div id="chart">
        <apexchart type="radialBar" :options="chartOptions" :series="series"></apexchart>
      </div>
    </v-card>-->
  </v-layout>
</template>
<script>
import VueApexcharts from "vue-apexcharts";
export default {
  components: {
    apexchart: VueApexcharts
  },
  data() {
    return {
      series: [24],
      chartOptions: {
        chart: {
          type: "radialBar",
          offsetY: -10,
          sparkline: {
            enabled: true
          }
        },
        plotOptions: {
          radialBar: {
            startAngle: -90,
            endAngle: 90,
            width: 100,
            track: {
              background: "#000",
              strokeWidth: "100%",
              margin: 5, // margin is in pixels
              dropShadow: {
                enabled: true,
                top: 2,
                left: 0,
                color: "#000",
                opacity: 1,
                blur: 2
              }
            },
            dataLabels: {
              name: {
                show: false
              },
              value: {
                offsetY: -1,
                fontSize: "16px"
              }
            }
          }
        },
        grid: {
          padding: {
            top: 5
          }
        },
        // fill: {
        //   type: 'gradient',
        //   gradient: {
        //     shade: 'light',
        //     shadeIntensity: 0.4,
        //     inverseColors: false,
        //     opacityFrom: 1,
        //     opacityTo: 1,
        //     stops: [0, 0, 53, 91]
        //   },
        // },
        labels: ["Average Results"]
      }
    };
  }
};
</script>
<style>
.candidates-card h5,
.register-card h5,
.vote-card h5 {
  background-color: #f0a787;
  padding: 2px 10px;
}
.candidates-flex,
.register-flex {
  padding-left: 20px;
}
.candidates-card {
  border-radius: 0px;
  margin-bottom: 10px;
}
.theme--light.v-list,
.theme--light.v-sheet {
  background: #fcf8e5;
}
.list-block .v-list__tile {
  padding: 0 10px;
  border-left: 2px solid #d8d6cf;
  /* margin: 15px 0 0 10px; */
}
.list-block:first-child {
  margin: 0 0 0 10px;
}
.list-block {
  margin: 14px 0 0 10px;
}
.list-block p:first-child {
  font-size: 12px;
  margin-bottom: 10px;
  color: #118dff;
}
.list-block p {
  font-size: 14px;
  margin-bottom: 5px;
}
.register-card p {
  font-size: 30px;
  font-weight: 500;
  text-align: center;
  padding: 7px;
  margin-bottom: 0px;
}
/* .register-card p{
        font-size: 10px;
    } */
.radial-layout {
  display: block;
  padding-left: 25px;
}
.register-card {
  margin-bottom: 10px;
}
#chart {
  display: flex !important;
  padding-top: 12px;
}
.low-rate {
  margin-top: 20px;
  margin-left: 10px;
}
.high-rate {
  margin-top: 20px;
  margin-right: 10px;
}
</style>
