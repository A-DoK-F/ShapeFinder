<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Projetjuin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style/bootstrap.min.css">
    <link rel="stylesheet" href="style/stylesheet_jeu.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  	</head>

  	<body>
    	<div class="header">
      	<h1>Shape Finder</h1>
      </div>

      	<div class="containerdv">
    		<div id="divg">
    		<h1>Sélectionne les cercles</h1><br>



    		<form method="post" action="result.php">
          <?php $date1 = time(); ?>
        <input type="hidden" name="date1" value="<?php echo $date1; ?>"/>
    		<table>
   				<tr>
    			<td><input type="checkbox" id="cercler" name="cercle"/><label for="cercler"> <span><img src="img/sens_interdit.png"/></span></label></td>
      			<td><input type="checkbox" id="triangle" name="triangle"/><label for="triangle"> <span><img src="img/triangle_oeil.png"/></span></label></td>
      			<td><input type="checkbox" id="triangle1" name="triangle"/><label for="triangle1"> <span><img src="img/triangle1.png"/></span></label></td>
      			</tr>
      		<table>
      			<button type="submit" name="valider">Valider</button>
      		</form>

      		<div>

		</div>




    </body>
</html>
