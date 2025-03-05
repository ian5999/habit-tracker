new DateRangePicker('datetimerange-input1', {
    // options here
}, function (start, end) {
  // callback
  alert(start.format() + " - " + end.format());
})

window.addEventListener('apply.daterangepicker', function (ev) {
    console.log(ev.detail.startDate.format('YYYY-MM-DD'));
    console.log(ev.detail.endDate.format('YYYY-MM-DD'));
  });
  window.addEventListener('show.daterangepicker', function (ev) {
    // do something
  });
  window.addEventListener('hide.daterangepicker', function (ev) {
    // do something
  });
  window.addEventListener('showCalendar.daterangepicker', function (ev) {
    // do something
  });
  window.addEventListener('hideCalendar.daterangepicker', function (ev) {
    // do something
  });
  window.addEventListener('cancel.daterangepicker', function (ev) {
    // do something
  });