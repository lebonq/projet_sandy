var x = 0;
var y = 0;
var input_user = true;
var pins_warning = false;

function get_pos() {
      $.getJSON($SCRIPT_ROOT + '_get_position', {
      }, function(data) {
        x = data.x;
        y = data.y;
      });
      return false;
}

function get_user_input() {
  $.getJSON($SCRIPT_ROOT + '_get_input_needed', {
  }, function(data) {
    if(String(data.user_input) == "true"){
      input_user = true;
    }
    else{
      input_user = false;
    }

  });
  return false;
}

function get_pin() {
  $.getJSON($SCRIPT_ROOT + '_get_pins', {
  }, function(data) {
    if(String(data.pins_warning) == "true"){
      pins_warning = true;
    }
    else{
      pins_warning = false;
    }

  });
  return false;
}

function setup() {
    createCanvas(400, 400);
    frameRate(3);
}
function draw() {    
    get_pos();
    get_user_input();
    get_pin();

    background(220);
    //On draw les tiges filtées
    fill(color(255,255,255));
    rect(10,0,10,400,20);
    rect(380,0,10,400,20);

    //on draw les piquets de bois
    fill(color(127,84,67));//marron
    rect(10,5,10,10);
    rect(380,5,10,10);
    rect(10,385,10,10);
    rect(380,385,10,10);
    
    fill(color(100,100,100));//bleu nuit
    rect(10,x,380,10);//la barre

    fill(color(0,0,0));
    rect(y,x-5,20,20,10);//le support

    fill(color(255,0,0)) //texte en rouge
    //On affiche les alertes
    if(input_user){
      textSize(32);
      text('Veuillez placer le support au bon endroit et appuyer sur le bouton pour continuer', 30, 75, 340,300);
      fill(0, 102, 153);
    }
    else if(pins_warning){
      textSize(32);
      text('Veuillez mettre les leviers dans leur position initiale', 30, 75, 340,300);
      fill(0, 102, 153);
    }
}