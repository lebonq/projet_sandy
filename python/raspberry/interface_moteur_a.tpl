<title>Moteur A</title>
<p>Vitesse = {{vitesse}} Marche = {{marche}} Sens = {{sens}} </p>
<form action="/moteura" method="POST">
    <input type="range" min="1" max="100" value="{{vitesse}}" class="slider" name="speed"></br>
    <td><input type ="submit" value="Marche" name="run"></td>
    <td><input type ="submit" value="Arrêt" name="stop"></td>
    <td><input type ="submit" value="Rotation avant" name="forward"></td>
    <td><input type ="submit" value="Rotation arrière" name="backward"></td>
</form>