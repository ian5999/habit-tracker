const carouselItems = document.querySeletorALL(".carousel_item");
let i = 1;

setInterval(() => {
// Accessing All the carousel Items
 Array.from(carouselItems).forEach((item,index) => {

   if(i < carouselItems.length){
    item.style.transform = `translateX(-${i*100}%)`
   }
  })

  if(i < carouselItems.length){
    i++;
  }
  else{
    i=0;
  }
},1000)