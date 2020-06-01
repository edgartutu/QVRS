<template>
    <div>
        <div v-if="pieOptions.series[0].data">
                <highcharts :options="pieOptions" ref="pieChart" class="pie"></highcharts>
                  </div>
    </div>
</template>
<script>
import VueHighcharts from './VueHighcharts.vue'
import Highcharts from 'highcharts'
import axios from 'axios'
export default {
    components: {
    VueHighcharts
   
  },
    data(){
        return{
                     pieOptions:{

              chart: {
        type: 'pie',
      
         backgroundColor: null,
        options3d: {
            enabled: true,
            alpha: 0
        }
    },
     credits: {
    enabled: false
  },
    title: {
        text: null
    },
    // subtitle: {
    //     text: '3D donut in Highcharts'
    // },
    plotOptions: {
        pie: {
            innerSize: 0,
            depth: 45
        }
    },
    series: [{
       
        data: null,
         name: 'Total Votes',
    }]

      }
        }
    },
    created(){
        
    axios.get('http://127.0.0.1:5000/GetPresidentailCandidates',
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     let p=response.data
      this.pieOptions.series[0].data=  [
          {
                                name: 'FDC',
                                color: '#0200D0',
                                y: parseInt(p.cand5, 10)
                            }, {
                                name: 'NRM',
                                color: '#ffe51f',
                                y: parseInt(p.cand8, 10)
                            },
                            {
                                name: 'AMAMA',
                                color: '#00ab1f',
                                y: parseInt(p.cand2, 10)
                            },
                            {
                                name: 'ABED',
                                color: '#eb3434',
                                y: parseInt(p.cand1, 10)
                            },
                            {
                                name: 'BARYA',
                                color: '#52024a',
                                y: parseInt(p.cand3, 10)
                            },
                            {
                                name: 'BENON',
                                color: '#3e4a35',
                                y: parseInt(p.cand4, 10)
                            },
                            {
                                name: 'JOSEPH',
                                color: '#adaca8',
                                y: parseInt(p.cand6, 10)
                            },
                             {
                                name: 'KYALYA',
                                color: '#080a09',
                                y: parseInt(p.cand7, 10)
                            }
            
        ]
      
    
    
    })
    }
}
</script>
<style scoped>
.pie{
     min-height: 250px;
     margin-left:-80%;
     margin-top:-100%;
}
</style> 

