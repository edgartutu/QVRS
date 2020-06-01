<template>
<div >
 
 <!-- <navbar/> -->
   <mapChart/>


 
</div>
 
</template>

<script>
import axios from 'axios'
import mapChart from '../components/DashViews/Map.vue'
import navbar from '../components/DashViews/NavBar'
export default{
    components:{
      mapChart,
      navbar
    },
  data(){
    return{
     
      
    }
  },

}

</script>