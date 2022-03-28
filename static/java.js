
let site="x";

//let sitex = "x"
//let a = 33;

/*function call_func() {
  const res = document.getElementById("x");

  const url = 'http://localhost:5000/test'
  fetch(url)
  .then(response => response.json())
  .then(json => {
      //console.log(json[0], "1:", json[1]);
      path = "./static/uploads/"
      //srcz ="201604621.jpg"
      //console.log(json.length)
     for (let i = 0; i < json[0].length; i++) {
        console.log(i)
        var img = document.createElement('img');
        //console.log(path.concat(json[i]))
        a = json[0]
        console.log(a)
        img.src = path.concat(a[i]);
        l = json[1]
       document.getElementById('grid').appendChild(img);
    }
     res.style.display ='block';
     document.getElementById("x").innerHTML = JSON.stringify(json)
  });
   
}*/
//functions local menu

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
  document.getElementById("upload").style.display="none";
  //add_img();
}

//process with svm model
function execute() {

  const res = document.getElementById("resultado");
  const url = 'http://localhost:5000/execute'

  fetch(url)
  .then(response => response.json())
  .then(json => {
     console.log("boas",json[0], json[1][1]);
     console.log(",", json)
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
        elem2 = json[1][0];

        img.src = path.concat(elem1[i]);
        h3.innerHTML = elem2[i];
        //l = json[1]
        document.getElementById("grid").appendChild(h3);
        document.getElementById('grid').appendChild(img);
     }
     //res.style.display ='block';
     //document.getElementById("resultado").innerHTML = JSON.stringify(json[1]);
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
      console.log(json)
      console.log("1",json[1][0]);
      console.log("2",json[1][1]);
      path = "./staticz/"
      //srcz ="201604621.jpg"
      //console.log(json.length)
      for (let i = 0; i < json[0].length; i++) {

        var img = document.createElement('img');
        var h3 = document.createElement("h3");
        //console.log(path.concat(json[i]))
        elem_1 = json[0];
        //elem_2 = json[1][1];
        elem_2 = json[1][0]
        img.src = path.concat(elem_1[i]);
        
        h3.innerHTML = elem_2[i];
        //l = json[1]
        document.getElementById("grid1").appendChild(h3)
        //console.log("im", img.src)
        document.getElementById('grid1').appendChild(img);
      }
    //document.getElementById("resultado_web").style.display ='block';
    //document.getElementById("resultado").innerHTML = JSON.stringify(json[1])
  })
}


function local(){
  
  document.getElementById("about_text").style.display="none";
  document.getElementById("executar_web").style.display="none";
  document.getElementById("upload").style.display="none";
  document.getElementById("img_down").style.display = "none";
  //document.getElementById("executar").style.display = "none";
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

  document.getElementById("executar").style.display ="none";
}

  //browser.tabs.create({url: "/index.html"})

/*window.addEventListener('scroll',(event) => {
  console.log('Scrolling...');
});
window.onscroll = function(event) {
  console.log("jbk")
};*/

window.onload = function(){

  chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
  site = tabs[0].url;
  
});
/*chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
  
const pop = window.open("index.html", tabs[0].url, 'menubar=0, innerWidth=800, innerHeight=400');
//browser.window.create({url:'index.html', height:100, widhth:800,type:'popup'})
});*/


/*var popupWindow = window.open(
  chrome.extension.getURL("index.html"),
  "exampleName",
  "width=400,height=400"
);
window.close();*/
/*const botao = document.getElementById("botao");
botao.addEventListener("click", call_func, false);*/

//upload 
const sub = document.getElementById("sub");
if(sub!=null){
sub.addEventListener("click", submit, false);
}
//local menu
const l = document.getElementById("local");
if(l!=null){
l.addEventListener("click", local, false);
}

/////////////////////////////////////////////////////

//botao site (faz download)
const s = document.getElementById("site");
if(s!=null){
s.addEventListener("click", download, false);
}

/*const imagem = document.getElementById("img_down");
imagem.addEventListener("click", imagens_pausa, false);*/

//menu local
const executar = document.getElementById("executar");
if(executar!=null){
executar.addEventListener("click", execute, false);
}

//menu site
const executar_web = document.getElementById("executar_web");
if(executar_web!=null){
executar_web.addEventListener("click", executa_web, false);
}

const down = document.getElementById("img_down");
if(down!=null){
down.addEventListener("click", loading_img, false);
}

//menu about
const about = document.getElementById("about");
if(about!=null){
about.addEventListener("click", pageabout, false);
}

const teste = document.getElementById("teste");
if(teste!=null){
teste.addEventListener("click", teste_p, false);
}
}