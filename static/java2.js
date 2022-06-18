
let site="x";


function submit() {

  const url = 'http://localhost:5000/uploader'

  fetch(url)
  .then(response => response.json())
  .then(json => {
     console.log(json);
  })

  document.getElementById("sub").style.display = "none";
  document.getElementById("file").style.display="none";
  document.getElementById("executar_web").style.display="none";
  document.getElementById("executar").style.display ="block";
  document.getElementById("img_down").style.display="none";
  //add_img();
}

//process with svm model
function execute() {

  const res = document.getElementById("resultado");
  const url = 'http://localhost:5000/execute'

  fetch(url)
  .then(response => response.json())
  .then(json => {

    console.log("tudo2",json)
     console.log("boas",json[0], json[1][1]);
     path = "./static/uploads/"
      //srcz ="201604621.jpg"
      //console.log(json.length)
     for (let i = 0; i < json[0].length; i++) {
        //console.log(i)
        var img = document.createElement('img');
        var h3 = document.createElement("h3");
        h3.setAttribute("id","h3_u");

        //console.log(path.concat(json[i]))
        elem1 = json[0];
        elem2 = json[1][1];

        img.src = path.concat(elem1[i]);
        h3.innerHTML = elem2[i];
        //l = json[1]
        document.getElementById("grid").appendChild(h3);
        document.getElementById('grid').appendChild(img);
     }
     res.style.display ='block';
     document.getElementById("resultado").innerHTML = JSON.stringify(json[1]);
  })
}

///////////////////////////////////////////////////////////////

//Functions site menu

//DOWNLOAD IMAGENS DE 1 SITE
function loading_img() {

  document.getElementById("about_text").style.display="none";
  document.getElementById("upload").style.display="none";
  const url = 'http://localhost:5000/web_image';

  var value = {site}

  fetch(url,
    {
      method: 'POST',
      body : JSON.stringify(value),
      headers: new Headers({
        "content-type": "application/json"
      })
    }
    )
  //document.getElementById("executar_web").style.display = "none";
  document.getElementById("img_down").style.display = "none";
  document.getElementById("sub").style.display = "none";
  document.getElementById("file").style.display = "none";

  t = 2000;

  setTimeout(function () {
    imagens_pausa();
  });

  setTimeout(function () {
    //loading_img();
    console.log("oi")
  document.getElementById("executar_web").style.display="block";
  }, t+5);
}

function imagens_pausa(){

  document.getElementById("alarm").style.display = "block";
  setTimeout(hideElement, t);
  
}

function hideElement() {
  document.getElementById("alarm").style.display = 'none';
}

//process with svm model
function executa_web() {

  const url = 'http://localhost:5000/execute_web';
  
  fetch(url)
  .then(response => response.json())
  .then(json => {
    console.log("tudo2",json)
     //console.log("boas",json[1][1]);
      path = "./staticz/"
      //srcz ="201604621.jpg"
      //console.log(json.length)
      for (let i = 0; i < json[0].length; i++) {

        var img = document.createElement('img');
        var h3 = document.createElement("h3");
        h3.setAttribute("id","h3_u");
        //console.log(path.concat(json[i]))
        elem_1 = json[0];
        elem_2 = json[1][1];
        img.src = path.concat(elem_1[i]);
        
        h3.innerHTML = elem_2[i];
        //l = json[1]
        document.getElementById("grid1").appendChild(h3)
        //console.log("im", img.src)
        document.getElementById('grid1').appendChild(img);
      }
    document.getElementById("resultado_web").style.display ='block';
    document.getElementById("resultado").innerHTML = JSON.stringify(json[1])
  })
}


function local(){
  
  document.getElementById("about_text").style.display="none";
  document.getElementById("executar_web").style.display="none";
  document.getElementById("upload").style.display="none";
  document.getElementById("img_down").style.display = "none";
  document.getElementById("executar").style.display = "block";
  document.getElementById("teste").style.display = "block";

  
}

function download(){
  
  document.getElementById("about_text").style.display="none";
  document.getElementById("executar_web").style.display="none";
  document.getElementById("upload").style.display="none";
  document.getElementById("download").style.display="block";
  document.getElementById("img_down").style.display = "block";
  document.getElementById("teste").style.display = "none";
  document.getElementById("executar").style.display = "none";
}
function pageabout(){

  document.getElementById("executar_web").style.display="none";
  document.getElementById("upload").style.display="none";
  document.getElementById("executar").style.display = "none";
  document.getElementById("teste").style.display = "none";
  document.getElementById("img_down").style.display = "none";
  const about = document.getElementById("about_text");

  if(about.style.display=="none"){
    about.style.display="block";
  }
  else{
    about.style.display="none";
  }
}

function teste_p(){
  chrome.tabs.create({ url: "upload_file.html" });
}

  //browser.tabs.create({url: "/index.html"})

/*window.addEventListener('scroll',(event) => {
  console.log('Scrolling...');
});
window.onscroll = function(event) {
  console.log("jbk")
};*/

window.onload = function(){


//upload 
const sub = document.getElementById("sub");
sub.addEventListener("click", submit, false);



/*const imagem = document.getElementById("img_down");
imagem.addEventListener("click", imagens_pausa, false);*/

//menu local
const executar = document.getElementById("executar");
executar.addEventListener("click", execute, false);
}