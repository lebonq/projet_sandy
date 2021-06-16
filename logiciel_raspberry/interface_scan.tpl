<!doctype html>
<head>
<title>Interface de scan</title>
<link rel="icon"  href="static/favicon.ico"/>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript"> 
    var $SCRIPT_ROOT = "{{ request.script_name }}";
</script>
<script type="text/javascript">
  $(function() {
    var submit_next = function(e) {
      $.getJSON($SCRIPT_ROOT + '_run_again', {
      }, function(data) {
      });
      return false;
    };

    $('#next').bind('click', submit_next);

    });
  });
</script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/p5@1.3.1/lib/p5.js"></script>
<script type="text/javascript" src="static/scan_interface.js"></script>

</head>

<body>
<h1>Moteur A - Interface de controle</h1>
<main>
</main>
<p>
    <input type="button" size="5" name="next" value="Suivant" id="next">
<p>
</body>
</html>