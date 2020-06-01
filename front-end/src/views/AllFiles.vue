<template>
   

        <div  class="wrap" style="width:50px; height:100px; margin:80px auto 0 auto;perspective-origin:50% -100%;
  perspective: 1500px;">
<div id="box">
<div class=" cube__face one" ><h1>100%</h1><p>Votes Recieved</p></div>
<!-- <div class=" cube__face two"></div> -->
<!-- <div class=" cube__face three"></div> -->
<div class=" cube__face four"><h1>NRM</h1> <p>60.2% of 100%</p></div>
<div class=" cube__face five"><h1>FDC</h1><p>35.8% of 100%</p></div>
<div class=" cube__face six"><h1>Others </h1><p>9% of 100%</p></div>
</div>
</div>


        
   
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
           
        }

    },
  
   
}
</script>

<style scoped >
.wrap {
  margin-top: 150px;
  perspective: 1000px;
  perspective-origin: 50% 50%;
}

#box
{
 margin: auto;
  position: relative;
  height: 100px;
  width: 100px;
  transform-style: preserve-3d; 
-webkit-animation-name: animation;
-webkit-animation-timing-function: ease-in-out;
-webkit-animation-iteration-count: infinite;
-webkit-animation-duration: 10s;

-webkit-transform-style: preserve-3d;
-webkit-transform-origin: 50px 50px 0;


}


#box div
{
position: absolute;
  box-sizing: border-box;
  padding: 10px;
  height: 100%;
  width: 100%;
  opacity: 0.9;
  background-color: #000;
  border: solid 1px #eeeeee;
  color: #ffffff;


}


 
#box .one
{ 
-webkit-transform: translateZ(50px);

}
#box .two
{ 
-webkit-transform: rotateX(-90deg) translateZ(100px);
}
#box .three 
{
-webkit-transform: rotateY(90deg) rotateX(90deg) translateZ(100px);
}
#box .four 
{
-webkit-transform: rotateY(180deg)  translateZ(50px);
}
#box .five
{ 
-webkit-transform: rotateY(-90deg)  translateZ(50px);
}
#box .six 
{
-webkit-transform: rotateY(90deg) translateZ(50px);
}
 
@-webkit-keyframes animation
{
from,to{}
 0% { transform: rotateY(0); }
 50%{transform: rotateY(180deg);}
    100% { transform: rotateY(360deg); }

}
</style>