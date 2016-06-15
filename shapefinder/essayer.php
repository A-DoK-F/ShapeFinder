<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Shape Finder</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style/bootstrap.min.css">
    <link rel="stylesheet" href="style/stylesheet_jeu.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <link rel="icon" type="image/x-icon" href="img/favicon.ico" />
  	</head>

  	<body>
    	<div class="header">
      	<h1>Shape Finder</h1>
      </div>

      	<div class="containerdv">
    		<div id="divg">
    		<h1>Sélectionne les cercles</h1><br></br>
        <div id="form">
          <form method="post" action="result.php">
            <?php $date1 = time(); ?>
          <input type="hidden" name="date1" value="<?php echo $date1; ?>"/>
          <table>
              <td><input type="checkbox" id="cercler" name="choix[]" value="sens_interdit.png"/><label for="cercler"> <span><img src="img/sens_interdit.png"/></span></label></td>
              <td><input type="checkbox" id="triangle" name="choix[]" value="triangle_oeil.png"/><label for="triangle"> <span><img src="img/triangle_oeil.png"/></span></label></td>
              <td><input type="checkbox" id="triangle1" name="choix[]" value="triangle1.png"/><label for="triangle1"> <span><img src="img/triangle1.png"/></span></label></td>
          <table>
              <button type="submit" name="valider" value="valider">Valider</button>
          </form>
        </div>

        </div>
      </div>



    </body>
</html>
