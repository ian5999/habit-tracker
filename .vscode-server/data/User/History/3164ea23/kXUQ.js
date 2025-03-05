new DateRangePicker('datetimerange-input1', {
    // options here
}, function (start, end) {
  // callback
  alert(start.format() + " - " + end.format());
})