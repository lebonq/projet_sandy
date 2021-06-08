<!doctype html>
<head>
<title>Moteur A</title>
<link rel="icon"  href="favicon.ico"/>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript"> 
    var $SCRIPT_ROOT = "{{ request.script_name }}";
</script>

<script type="text/javascript">
  $(function() {
    var submit_speed = function(e) {
      $.getJSON($SCRIPT_ROOT + '_change_speed', {
        vitesse: $('input[name="vitesse"]').val(),
      }, function(data) {
        $('#speed_aff').text(data.speed);
      });
      return false;
    };
    
    var submit_run = function(e) {
      $.getJSON($SCRIPT_ROOT + '_run', {
      }, function(data) {
        $('#run_aff').text(data.run_aff);
      });
      return false;
    };

    var submit_sens = function(e) {
      $.getJSON($SCRIPT_ROOT + '_sens', {
      }, function(data) {
        $('#sens_aff').text(data.sens);
      });
      return false;
    };

    $('#run').bind('click', submit_run);
    $('#sens').bind('click', submit_sens);


    $('input[type=text]').bind('keydown', function(e) {
      if (e.keyCode == 13) {
        submit_speed(e);
      }
    });
  });
</script>
</head>

<body>
<h1>Moteur A - Interface de controle</h1>
<p>
    Vitesse = <span id="speed_aff">50</span> <span id="run_aff">Arrêt</span> <span id="sens_aff">Avant</span></br></br>
    <input type="text" size="5" name="vitesse"></br>
    <input type="button" size="5" name="run" value="On/Off" id="run">
    <input type="button" size="5" name="sens" value="Changer de sens" id="sens">
<p>
</body>
</html>