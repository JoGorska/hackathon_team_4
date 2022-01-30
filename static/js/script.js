

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

// Handwriting animation
var i = 0;
var txt = 'Welcome to [project name]'; /* The text */
var speed = 80; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("writing").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

typeWriter();

