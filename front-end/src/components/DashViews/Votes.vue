<template>
    <div>
      <v-card  style="background-color:teal;overflow-x: auto;">
        <!-- flag section -->
      <v-layout row wrap justify-space-around>
        <v-flex xs12 md12>
          <v-card  height="7"
            class="black mx-auto">
          </v-card>
      </v-flex>
       <v-flex xs12 md12>
          <v-card  height="5"
            class="yellow accent-2 mx-auto">
          </v-card>
        </v-flex>
       <v-flex xs12 md12>
          <v-card  height="6"
            class=" red accent-4 mx-auto">
          </v-card>
        </v-flex>
      </v-layout>
      <v-container fluid >
       <v-layout wrap >
         <v-flex xs12 md12>
            <navbar/>
          </v-flex>
          <!-- <v-flex xs12 md12>
              <p style="font-size:2.5vw;padding-left:50%;font-family:verdana;color:white;">The 2016 General Election</p> 
          </v-flex> -->
       </v-layout>
      
    <!-- section dropdown buttons      -->
        <v-layout row wrap justify-space-around>
              <v-flex xs12  md3>
                  <!-- <v-col cols="4" sm="4"> -->
                  <v-overflow-btn
                    class="my-3"
                    color="purple"
                    :items="dropdown_icon"
                    v-model="cat"
                    label="Choose Election Category"
                    item-value="text"
                    width="50"
                    @input="pushToArray(),general(), candidates(),pushToArray3()"
                  ></v-overflow-btn>
                  <div v-if="cat">
                      <v-overflow-btn
                    class="my-3"
                    color="purple"
                    :items="dropdown_icon1"
                  v-model="dist"
                  id="container"
                    label="Choose District"
                    @input="  pushToArray3(), pushToArray2(),general(),district()"
                  item-value="text"
                  style="-webkit-overflow-scrolling: touch;"
                  v-dragscroll.y="true"
                    width="50"
                    hint="District"
                  ></v-overflow-btn>

                    <div v-if="dist && cat">
                    <v-overflow-btn
                    class="my-3"
                    color="purple"
                    :items="dropdown_icon2"
                    v-model="county"
                    label="Choose Sub-County"
                    @input=" pushToArray3(),general(),pasrish()"
                  item-value="text"
                    style="-webkit-overflow-scrolling: touch;"
                      v-dragscroll.y="true"
                    width="50"
                    hint="Sub-County"
                  ></v-overflow-btn>

                  <div v-if="dist && cat && county">
                    <v-overflow-btn
                    class="my-3"
                    color="purple"
                    :items="dropdown_icon3"
                    v-model="poll"
                    label="Choose Parish"
                    item-value="text"
                    style="-webkit-overflow-scrolling: touch;"
                      v-dragscroll.y="true"
                    width="50"
                    @input="general(),polling()"
                    hint="Parish"
                  ></v-overflow-btn>
                </div>
                      </div>
                  
                </div>
        <!-- </v-col> -->
              </v-flex>
<!-- results section -->
             <v-flex xs12 md8>
                <div v-if="cat==='Presidential'">
                  <v-expand-x-transition >
                  <v-card
                    flat
                    height="610"
                    class="mx-auto"
                    style="overflow-y: auto;background-color:white;overflow-x: auto;"
                   
                  >
                  <v-container fluid>
                    <v-layout >
                      <v-flex xs12 md12>
                        <div v-if="things.cand1">
                          <a href="#" style="font-size:25px" class=" teal--text text--darken-4">{{title}}</a>
                        </div>
                        </v-flex>
                        
                      <!-- pariamentraey -->
                     
                      <div v-if="dist ">
                        <p style="font-size:15px;" class="red--text text--darken-4">{{result.name}} </p>
                      </div>
                        <div v-if="county">
                        <p style="font-size:15px;" class="red--text text--darken-4">{{result.SCOUNTY_NAME}}</p>
                      </div>
                      <div v-if="poll">
                        <p style="font-size:15px;" class="red--text text--darken-4">{{result.PARISH_NAME}}</p>
                      </div>
                        <!-- <p style="font-size:20px;margin-left:40%;" class="red--text text--darken-4">{{result.name}} {{result.SCOUNTY_NAME}} {{result.PARISH_NAME}}</p> -->
                      
                      </v-layout>
                      <v-layout >
                      <v-flex xs6 md4>
                          <v-container>
                            
                        <v-layout>
                        <v-flex xs11 md6 style="text-align: left;" >
                          <a href="#" class="teal--text text--darken-4"> <b>CANDIDATE</b></a>
                        
                        </v-flex>

                        <v-divider vertical></v-divider>

                        <v-flex xs1 md6 >
                          <a href="#" class="teal--text text--darken-4"><b>
                            VOTES
                          </b></a>
                          
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                        <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand1}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand1}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                        <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand2}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand2}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand3}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand3}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand4}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand4}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand5}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand5}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand6}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand6}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand7}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand7}}
                        </v-flex>
                        </v-layout>
                        <br>
                        <v-layout>
                          <v-flex xs11 md6 class="teal--text text--darken-4">
                          {{things.cand8}}
                        </v-flex>
                        <v-flex xs1 md2 class="black--text" style="text-align: right;">
                          {{result.cand8}}
                        </v-flex>
                        </v-layout>
                        <br>
                      </v-container>
                      </v-flex>
                      <v-flex xs12 md8>
                        <div v-if="pieOptions.series[0].data">
                          <highcharts :options=" pieOptions" class="charts"  ></highcharts>
                          <div id="container"></div>
                          </div>
                      </v-flex>
                    </v-layout>
                    <div v-if="poll">
                      <div  > <a href="#" style="font-size:25px;" class="teal--text text--darken-4">POLLING STATIONS In</a>  <a href="#" style="font-size:25px;" class="red--text text--darken-4"> {{result.PARISH_NAME}}</a>  </div>
                      <br>
                    <v-layout row wrap justify-space-around>
                      <v-flex xs4 md4 >
                        <div style="color:#0702d4;">
                          Polling station
                        </div>
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand1}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand2}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand3}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand4}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand5}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand6}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand7}}
                      </v-flex>
                      <v-flex xs12 md1 style="color:#0702d4;">
                        {{things.cand8}}
                      </v-flex>
                      <v-divider inset>

                      </v-divider>
                    </v-layout>
                    <v-card flat v-for="(item,index) in resultd" :key="item.PS_NAME">
                    <v-layout row wrap justify-space-around>
                        <v-flex xs4 md4 >
                            <v-dialog
                              v-model="dialog"
                              width="700"
                            >
                              <template v-slot:activator="{ on }">
                                  <a href="#" v-on="on" @click="pushimage(),get_file(index)" style="color:black;">  {{item.PS_NAME}}</a>
                              </template>
                                  <div v-if="my_image">
                                    <v-card>
                                <!-- <v-card-title
                                  class="headline grey lighten-2"
                                  primary-title
                                >
                                  {{item.PS_NAME}}
                                </v-card-title> -->

                                <v-card-text>
                                  <div class="image-preview" v-if="my_image">
                                    <img class="preview" v-bind:src="'data:image/jpg;base64,'+my_image">
                                    
                                </div>
                                </v-card-text>

                                <v-divider></v-divider>

                                <v-card-actions>
                                  <v-spacer></v-spacer>
                                  <v-btn
                                    color="pink"
                                    text
                                    small
                                    @click="dialog = false"
                                    class="text--white"
                                  >
                                    close
                                  </v-btn>
                                </v-card-actions>
                              </v-card>

                                  </div>
                                  <div v-if="my_image===''">
                                    <h3 class="red--text">No DR form yet</h3>
                                      <!-- <v-spacer></v-spacer> -->
                                    <v-btn
                                    color="pink"
                                    text
                                    small
                                    @click="dialog = false"
                                    class="text--white"
                                  >
                                    close
                                  </v-btn>
                                  </div>
                            </v-dialog>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand1}}
                        <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand1/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand2}}
                        <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand2/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand3}}
                      <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand3/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand4}}
                      <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand4/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand5}}
                        <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand5/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand6}}
                        <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand6/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand7}}
                        <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand7/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-flex xs12 md1>
                        {{item.cand8}}
                      <div style="font-size:10px;color:#0702d4;">
                          ({{((item.cand8/(item.cand1+item.cand2+item.cand3+item.cand4+item.cand5+item.cand6+item.cand7+item.cand8))*100).toFixed(1)}}%)
                        </div>
                      </v-flex>
                      <v-divider inset>
                      </v-divider>
                    </v-layout>
                    </v-card>
                    </div>
                  </v-container>
                  </v-card>
                </v-expand-x-transition>
                </div>
                <div v-else-if="cat==='parliamentary'">
                  <v-expand-x-transition>
                    <v-card flat
                    height="610"
                    class="mx-auto"
                    style="overflow-y: auto;background-color:white;overflow-x: auto;">
                    <v-container>
                        <v-layout>
                    <v-flex xs12 md12 style="font-size:2.5vw">
                        No Parliamentary Data Available
                    </v-flex>
                  </v-layout>

                    </v-container>
                    

                    </v-card>
                    

                  </v-expand-x-transition>
                  
                </div>
                <div v-else>
                  <v-expand-x-transition >
                  <v-card
                    flat
                    height="600"
                    class="mx-auto"
                    style="overflow-y: auto;background-color:white;"
                   
                  >
                  <v-avatar size="400"  style="margin-top:9%;margin-left:30%;">
                    <img  src="@/assets/img/vote.png" style="width:100%;height:auto;" alt="vote">
                  </v-avatar>
                    </v-card>
                  </v-expand-x-transition>
                </div>
            </v-flex>
        </v-layout>
        <v-card flat style="background-color:teal;" height="74">
           
        </v-card>
        </v-container>
      </v-card>
    
    </div>
</template>
<script>
import Highcharts from 'highcharts'
import VueHighcharts from './VueHighcharts.vue'
import axios from 'axios'
import navbar from './NavBar'

export default {
  components: {
    VueHighcharts,
    navbar

  },
    data(){
        return{
            cat:"",
            dist:"",
            county:"",
            poll:"",
            ps_name:"",
            title:"PRESIDENTIAL OVERALL PERFORMANCE",
            now:null,
            expand: false,
      expand2: false,
       offset: true,
        dialog: false,
         my_image:'',
         district_:'DISTRICT',
            dropdown_icon: [
        { text: 'Presidential'},
        { text: 'parliamentary' },
        // { text: 'delete', callback: () => console.log('delete') },
      ],
      dropdown_icon1:null,
       dropdown_icon2: null,
      dropdown_icon3: null,
       dropdown_icon4: [
        { text: 'mubs', callback: () => console.log('lists') },
        { text: 'katwe c/u', callback: () => console.log('favorites') },
        // { text: 'delete', callback: () => console.log('delete') },
      ],
      result:[],
      dresult:[],
      resultd:[],
      things:[],

      pieOptions:{
                                chart: {
                            renderTo: 'container',
                            type: 'pie',
                            width: 500,
                            height: 450,
                             backgroundColor: null,
                        },
                        title: {
                            text: null
                        },
                        credits: {
                                enabled: false
                            },
                        series: [{
                          data:this.now,
                            name: 'Votes',
                            
                            dataLabels: {
                                format: '<b>{point.name}</b> {point.percentage:.1f}%'
                            }
                        }]

      }

        }
    },
    created(){
       axios.get('http://127.0.0.1:5000/get_districts',
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      let result= response.data
      this.dropdown_icon1=result
     

    })
    
    },
   
    
    methods:{
      general(){
         

        axios.post('http://127.0.0.1:5000/Candidates',{"Category":this.cat,"District":this.dist,"Subconty":this.county,"PARISH_NAME":this.poll},
         {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
   
    ).then(response =>{
     let d=response.data
      this.result= response.data
      this.pieOptions.series[0].data=[{
                                name: 'FDC',
                                color: '#0200D0',
                                y: parseInt(d.cand5, 10)
                            }, {
                                name: 'NRM',
                                color: '#ffe51f',
                                y: parseInt(d.cand8, 10)
                            },
                            {
                                name: 'AMAMA',
                                color: '#00ab1f',
                                y: parseInt(d.cand2, 10)
                            },
                            {
                                name: 'ABED',
                                color: '#eb3434',
                                y: parseInt(d.cand1, 10)
                            },
                            {
                                name: 'BARYA',
                                color: '#52024a',
                                y: parseInt(d.cand3, 10)
                            },
                            {
                                name: 'BENON',
                                color: '#3e4a35',
                                y: parseInt(d.cand4, 10)
                            },
                            {
                                name: 'JOSEPH',
                                color: '#adaca8',
                                y: parseInt(d.cand6, 10)
                            },
                             {
                                name: 'KYALYA',
                                color: '#080a09',
                                y: parseInt(d.cand7, 10)
                            }

      ]
      
      // console.log(this.result)

    })

      },
      district(){
            axios.post('http://127.0.0.1:5000/candidateDistrict',{"District":this.dist},
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      let result= response.data
      this.dropdown_icon2=result
      console.log(this.dropdown_icon2)

    })

      },
      pasrish(){
         axios.post('http://127.0.0.1:5000/candidateParish',{"District":this.dist,"Subconty":this.county},
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      let result= response.data
      this. dropdown_icon3=result
      console.log(this.dropdown_icon3)

    })
      },
      polling(){
        axios.post('http://127.0.0.1:5000/candidateSubcounty',{"District":this.dist,"Subconty":this.county,"PARISH_NAME":this.poll},
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      this.resultd= response.data
      console.log( this.resultd)

    })
      },
       pushToArray(){
         this.dist=''
         this.county=''
       },
        pushToArray2(){
         this.county=''
       },
        pushToArray3(){
         this.poll=''
       },
       candidates(){
          axios.post('http://127.0.0.1:5000/get_allcandidates',{"Category":this.cat},
    {
      headers: {
        'x-access-token': localStorage.getItem('token')
    }
    }
    ).then(response =>{
     
      this.things= response.data
      // console.log(this.things)
      
     

    })
       },
        pushimage(){
         this.my_image=''
        
       },

               get_file(index){
//           axios({
//         url: 'http://127.0.0.1:5000 /single_file',
//         method: 'POST',
//         responseType: 'blob',
        
//           "files":this.file
        
//          // important
// })
// .then((res) => {
//    this.my_image=res.data

//    console.log(this.my_image)
// })
             axios.post('http://127.0.0.1:5000/single_file',{responseType: 'blob',"ps_name":this.resultd[index].PS_NAME},
    {
      headers: {
        'x-access-token': localStorage.getItem('token'),
        
    }
    }
    ).then(response =>{
                this.my_image=response.data.media
     
      // var b = new Buffer(response.data);
      // this.my_image = b.toString('base64');

      // console.log(this.my_image)
     

    })

        },
    }
}
</script>

<style >
img.preview {
    width: 600px;
    background-color: white;
    border: 1px solid #DDD;
    padding: 5px;
    height: 600px;
}
.image-preview {
    font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
    padding: 20px;
}
.charts{
  position:absolute;
}
</style>