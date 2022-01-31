// Handwriting animation
var i = 0;
var txt = "Welcome to MyMind'sEye"; /* The text */
var speed = 80; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("writing").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

typeWriter();