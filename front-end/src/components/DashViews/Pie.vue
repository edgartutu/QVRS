<template>
    <!-- <section class="chartss"> -->
      <div style="color:teal;">
        <v-card>

           <v-layout row wrap justify-space-around>
          <v-flex xs12 md12>
            <v-card  height="7"
              class="black ">
            </v-card>
          </v-flex>
          <v-flex xs12 md12>
            <v-card  height="6"
              class="yellow accent-2 ">
            </v-card>
          </v-flex>
          <v-flex xs12 md12>
            <v-card  height="6"
              class=" red accent-4 ">
            </v-card>
          </v-flex>
        </v-layout>

<!-- section animated candidate images  -->
        <v-layout wrap>
          <v-flex xs12 md12>
            <navis />
          </v-flex>
          <!-- <v-flex xs12 md12>
            <p style="font-size:20px;padding-left:35%;font-family:verdana;">The 2016 General Election</p>
          </v-flex> -->
        </v-layout>
        
        <marquee-text
        :duration="15"
        :repeat="3"
        dark
        class=" teal white--text mt-2"
        > 
        
            <v-layout row  justify-space-around>
               <v-flex xs10 md2>
                 <v-card
                    min-width="250"
                     max-height="120"
                    outlined
                    flat 
                        >
                      <v-row
                        class="fill-height"
                      >
                          <v-avatar
                            class="profile"
                            color="grey"
                            size="100"
                            tile
                          >
                          <img src="@/assets/img/besigye.jpg">
                          </v-avatar>
                          <strong>
                            <animated-number
                            :value="data.cand5"
                            :formatValue="formatTobes"
                            :duration="10000"
                            style="font-size:20px;color:#040ac7;"
                          />
                          </strong> votes
                          <div> <strong style="font-size:15px">FDC</strong> </div>
                      </v-row>
                  </v-card>
            </v-flex>
            <v-flex xs10 md2>
                   <v-card
                    min-width="250"
                     max-height="120"
                    outlined
                    flat
                        >
                      <v-row
                        
                        class="fill-height"
                      >
                          <v-avatar
                            class="profile"
                            color="grey"
                            size="100"
                            tile
                          >
                          <img src="@/assets/img/m7.jpg">
                          </v-avatar>
                          <strong>
                            <animated-number
                            :value="data.cand8"
                            :formatValue="formatToPrice"
                            :duration="10000"
                            style="font-size:20px;color:#cdd400;"
                          />
                          </strong> votes
                          <div> <strong style="font-size:15px">NRM</strong> </div>
                      </v-row>
                  </v-card>
            </v-flex>
              <v-flex xs10 md2>
                 <v-card
                min-width="250"
                 max-height="120"
                outlined
                flat
                    >
                  <v-row
                    class="fill-height"
                  >
                      <v-avatar
                        class="profile"
                        color="grey"
                        size="100"
                        tile
                      >
                      <img src="@/assets/img/ama.jpg">
                      
                      </v-avatar>
                      <strong>
                        <animated-number
                        :value="data.cand2"
                        :formatValue="formatToama"
                        :duration="10000"
                        style="font-size:20px;color:#d47c00;"
                      />
                      </strong> votes
                      <div> <strong style="font-size:15px">Go Forward</strong> </div>
                  </v-row>
              </v-card>
            </v-flex>
              <v-flex xs10 md2>
                 <v-card
                      min-width="250"
                       max-height="120"
                      outlined
                          flat
                          >
                        <v-row
                          class="fill-height"
                        >
                            <v-avatar
                              class="profile"
                              color="grey"
                              size="100"
                              tile
                            >
                            <img src="@/assets/img/barya.jpg">
                            
                            </v-avatar>
                            <strong>
                              <animated-number
                              :value="data.cand3"
                              :formatValue="formatTothers"
                              :duration="10000"
                              style="font-size:20px"
                            />
                            </strong> votes
                            <div> <strong style="font-size:15px">BARYA</strong> </div>
                        </v-row>
                    </v-card>
            </v-flex>       
              <v-flex xs10 md2>
                 <v-card
                    min-width="250"
                     max-height="120"
                    outlined
                    flat
                    >
                  <v-row
                    class="fill-height"
                  >
                      <v-avatar
                        class="profile"
                        color="grey"
                        size="100"
                        tile
                      >
                      <img src="@/assets/img/abed.jpg">
                      </v-avatar>
                      <strong>
                        <animated-number
                        :value="data.cand1"
                        :formatValue="formatTothers"
                        :duration="10000"
                        style="font-size:20px"
                      />
                      </strong> votes
                      <div> <strong style="font-size:15px">ABED</strong> </div>
                  </v-row>
              </v-card>
            </v-flex>
            <v-flex xs10 md2>
              <v-card
                  min-width="250"
                  max-height="120"
                  outlined
                  class="white"
                      flat
                      >
                        <v-avatar
                          size="100"
                          tile
                        >
                        <img src="@/assets/img/benon.jpg">
                        </v-avatar>
                        <strong>
                          <animated-number
                          :value="data.cand4"
                          :formatValue="formatTothers"
                          :duration="10000"
                          style="font-size:20px"
                        />
                        </strong> votes
                        <div> <strong style="font-size:15px">BENON</strong> </div>
                </v-card>
            </v-flex>
              <v-flex xs10 md2>
                <v-card
                min-width="250"
                 max-height="120"
                outlined
                    flat
                    >
                  <v-row
                    class="fill-height"
                  >
                    <v-avatar
                      class="profile"
                      color="grey"
                      size="100"
                      tile
                    >
                    <img src="@/assets/img/kyalya.png">
                    </v-avatar>
                    <strong>
                      <animated-number
                      :value="data.cand7"
                      :formatValue="formatTothers"
                      :duration="10000"
                      style="font-size:20px"
                    />
                    </strong> votes
                    <div> <strong style="font-size:15px">KYALYA</strong> </div>
                  </v-row>
              </v-card>
            </v-flex>
        </v-layout>
      </marquee-text>

<!-- section moving percentage badge -->
        <v-layout  row wrap justify-space-around>
          <v-flex xs12 md12 >
            <marquee-text
              :duration="15"
              :repeat="3"
              dark
              class=" white black--text mt-2"
            > 
              <v-btn small class="blue white--text">
                <span>35.6%</span>
              </v-btn>FDC
              <v-btn small flat class="yellow accent-4 white--text"> <span >60.2%</span> </v-btn>NRM
              <v-btn small flat class="green white--text"> <span >1.2%</span> </v-btn>AMAMA
              <v-btn small flat class="red white--text"> <span >0.2%</span> </v-btn>ABED
                <v-btn small flat class="pink white--text"> <span >0.03%</span> </v-btn>BARYA
                <v-btn small flat class="black white--text"> <span >1.2%</span> </v-btn>KYALYA
                  <v-btn small flat class="grey white--text"> <span >0.1%</span> </v-btn>JOSEPH
                  <v-btn small flat class="purple white--text"> <span >0.01%</span> </v-btn>BENON
            </marquee-text>
            </v-flex>
        </v-layout>

        <!-- section pie and district table  -->
        
        <v-layout row wrap justify-space-around>
            <v-flex xs12 md6>
              <v-card class="pa-3" outline max-width="800"  height="580px">
                  <div v-if="pieOptions.series[0].data.length">
                <vue-highcharts :options="pieOptions" ref="pieChart" class="pie"></vue-highcharts>
                  </div>
              </v-card>
            </v-flex>
            <v-flex xs12 md6>
              <v-card class="pa-3" outline max-width="800"  height="580px" style="overflow-y: auto;overflow-x: auto" >
                <v-data-table class="fb-table-elem"
                :headers="headers"
                :items="items"
                hide-actions
                dense
                item-key="name"
                >
                <template slot="items" slot-scope="{item}" >          
                    <td class="datatable-cell-wrapper"> <a href="#" style="color:#0702d4;">{{ item.name }}</a></td>
                    <td class="datatable-cell-wrapper"><div>{{ item.cand1}}</div></td>
                    <td class="datatable-cell-wrapper">{{ item.cand2 }}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand3}}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand4 }}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand5 }}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand6 }}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand7 }}</td>
                    <td class="datatable-cell-wrapper">{{ item.cand8 }}</td>
                  </template>
                </v-data-table>
              </v-card>
            </v-flex>
        </v-layout>

        </v-card>
       
         
      </div>
</template>
<script>
import Highcharts from 'highcharts'
import VueHighcharts from './VueHighcharts.vue'
import AnimatedNumber from "animated-number-vue";
import axios from 'axios'
import navis from './NavBar'
export default {
  props: ["data", "options"],
components: {
    VueHighcharts,
    AnimatedNumber,
    navis
  },

  data() {
    return {
      newData:null,
      banner:null,
        items: [
       
      ],
      headers: [
        {
          text: 'DistrictName',
          align: 'left',
          sortable: false,
          value: 'name',
        },
        { text: 'ABED', value: 'cand1' },
        { text: 'AMAMA', value: 'cand2' },
        { text: 'BARYA', value: 'cand3' },
        { text: 'BENON', value: 'cand4' },
        { text: 'KIZZA', value: 'cand5' },
        { text: 'JOSEPH', value: 'cand6' },
        { text: 'MAUREEN', value: 'cand7' },
        { text: 'YOWERI', value: 'cand8' },
        
      ],
      pieOptions:{

              chart: {
        type: 'pie',
         backgroundColor: null,
        options3d: {
            enabled: true,
            alpha: 50
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
            innerSize: 100,
            depth: 45
        }
    },
    series: [{
       
        data: this.newData,
         name: 'Total Votes',
    }]

      }
    }
  },
   mounted(){
           axios.get('http://127.0.0.1:5000/SendMapData',
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      this.items= response.data
     
      // console.log(this.items)

    })
                
  },
  created() {
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
      
      this.data=response.data
      this.banner=[
         {
                                name1: 'FDC',
                                color1: '#0200D0',
                                y1: parseInt(p.cand5, 10)
         },{
                                name2: 'NRM',
                                color2: '#ffe51f',
                                y2: parseInt(p.cand8, 10)
                            
         }, {
                                name3: 'AMAMA',
                                color3: '#00ab1f',
                                y3: parseInt(p.cand2, 10),
                            
         },{
                                name4: 'ABED',
                                color4: '#eb3434',
                                y4: parseInt(p.cand1, 10),
         },{    
                            
                                name5: 'BARYA',
                                color5: '#52024a',
                                y5: parseInt(p.cand3, 10),
                            
         },{       
                                name6: 'BENON',
                                color6: '#3e4a35',
                                y6: parseInt(p.cand4, 10),
                            
         },{         
                                name7: 'JOSEPH',
                                color7: '#adaca8',
                                y7: parseInt(p.cand6, 10),
                            
         },{            
                                name8: 'KYALYA',
                                color8: '#080a09',
                                y8: parseInt(p.cand7, 10)
                            }
            
      ]
      // console.log(this.banner)

    })
  },
 
  methods: {
    formatToPrice(value) {
      return `${value.toFixed(0)}`;
    },
    formatTobes(value1){
      return `${value1.toFixed(0)}`;
    },
     formatToama(value2){
      return `${value2.toFixed(0)}`;
    },

    formatTothers(value3){
      return `${value3.toFixed(0)}`;
    },

  },
}
</script>
<style  scoped>

.pie{
     min-height: 400px;
}
</style>
