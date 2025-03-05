const carouselItems = document.querySelectorAll(".carousel_item"); 
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
},2000)

//increase and decrease button//
function totalClick(click) {
    const totalClicks = document.getElementById('totalClicks');
    let sumvalue = parseInt(totalClicks.innerText) + click;
    sumvalue = sumvalue < 0 ? 0 : sumvalue; // Preventing value from going below zero
    totalClicks.innerText = sumvalue;
}
//Google Places api//
let autocomplete;

function initAutocomplete() {
  autocomplete = new google.maps.places.Autocomplete(
    document.getElementById('autocomplete'), {types: ['geocode']}
  );
  
  autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
  var place = autocomplete.getPlace();
  if (!place.geometry) {
    // User entered the name of a Place that was not suggested and
    // pressed the Enter key, or the Place Details request failed.
    window.alert("No details available for input: '" + place.name + "'");
    return;
  }

  // You can use place details here as needed
}
window.addEventListener("load", function (event) {
  let drp = new DateRangePicker('datetimerange-input1',
      {
          //startDate: '2000-01-01',
          //endDate: '2000-01-03',
          //minDate: '2021-07-15 15:00',
         // maxDate: '2021-08-16 15:00',
          //maxSpan: { "days": 9 },
          showDropdowns: true,
          //minYear: 2020,
          maxYear: 2025,
          //showWeekNumbers: true,
          //showISOWeekNumbers: true,
          timePicker: true,
          //timePickerIncrement: 10,
          timePicker24Hour: true,
          //timePickerSeconds: true,
          //showCustomRangeLabel: false,
          alwaysShowCalendars: true,
          //opens: 'center',
          //drops: 'up',
          //singleDatePicker: true,
          //autoApply: true,
          //linkedCalendars: false,
          //isInvalidDate: function(m){
          //    return m.weekday() == 3;
          //},
          //isCustomDate: function(m){
          //    return "weekday-" + m.weekday();
          //},
          //autoUpdateInput: false,
          //ranges: {
             // 'Today': [moment().startOf('day'), moment().endOf('day')],
              //'Yesterday': [moment().subtract(1, 'days').startOf('day'), moment().subtract(1, 'days').endOf('day')],
             // 'Last 7 Days': [moment().subtract(6, 'days').startOf('day'), moment().endOf('day')],
             // 'This Month': [moment().startOf('month').startOf('day'), moment().endOf('month').endOf('day')],//
         // },
          locale: {
              format: "YYYY-MM-DD HH:mm:ss",
          }
      },
      function (start, end) {
          alert(start.format() + " - " + end.format());
      })
  //drp.setStartDate('2014/03/01');
  //drp.setEndDate('2014/03/03');
  window.addEventListener('apply.daterangepicker', function (ev) {
      console.log(ev.detail.startDate.format('YYYY-MM-DD'));
      console.log(ev.detail.endDate.format('YYYY-MM-DD'));
  });
});

