$(document).ready(function () {

});

document.getElementById("submit").onclick = function() { parseText() };

function myFunction() {
  text = document.getElementById('exampleFormControlTextarea1').value;
  console.log(text)
  document.getElementById(results).innerHTML = text;
}