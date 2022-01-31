//start date picker - checks if date is in the future.
$(document).ready(function () {

  $("#id-start-date").on('change', function () {
    var selectedDate = new Date($(this).val());
    Math.floor(selectedDate.getTime()/ 1000)

    var todaysDay = new Date();
    Math.floor(todaysDay.getTime()/ 1000)

    if (selectedDate > todaysDay) {
        alert("Start date must not be greater than today's date");
        $(this).val('');
    }  
  })
});

//end date picker - checks if date is in the future.
$(document).ready(function () {

  $("#id-end-date").on('change', function () {
    var selectedDate = new Date($(this).val());
    Math.floor(selectedDate.getTime()/ 1000)

    var todaysDay = new Date();
    Math.floor(todaysDay.getTime()/ 1000)

    if (selectedDate > todaysDay) {
        alert("End date must not be greater than today's date");
        $(this).val('');
    }  
  })
});


$(document).ready(function () {


  // Toggle password visibility
  $("#toggle-password").click(function () {
      id = $(this).attr("data-bs-target");
      if ($(`#${id}`).attr("type") === "password") {
        $(`#${id}`).attr("type", "text");
        $(this).removeClass("fa-lock").addClass("fa-lock-open");
      } else if ($(`#${id}`).attr("type") === "text") {
        $(`#${id}`).attr("type", "password");
        $(this).removeClass("fa-lock-open").addClass("fa-lock");
      }
    });
  });



