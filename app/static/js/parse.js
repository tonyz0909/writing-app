document.getElementById("submit").onclick = function() {
    loadFileAsText();
};

function parseText() {
  text = document.getElementById('exampleFormControlTextarea1').value;
  console.log(text);
  document.getElementById("results").innerHTML = text;
}

function loadFileAsText(){
  var fileToLoad = document.getElementById("fileToLoad").files[0];

  if (fileToLoad == undefined) {
        return parseText();
  }
  var fileReader = new FileReader();
  fileReader.onload = function(fileLoadedEvent){
      var textFromFileLoaded = fileLoadedEvent.target.result;
      document.getElementById("inputTextToSave").value = textFromFileLoaded;
  };

  fileReader.readAsText(fileToLoad, "UTF-8");
  console.log(text)
}
