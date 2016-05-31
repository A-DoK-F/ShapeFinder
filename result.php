<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Projetjuin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style/bootstrap.min.css">
    <link rel="stylesheet" href="style/stylesheet.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <link rel="icon" type="image/x-icon" href="img/favicon.ico" />
  </head>

  <body>
    <div class="header">
      <h1>Shape Finder</h1>
      <hr></hr>
    </div>

    <div class="containerdv">
    	<div id="divg">
      	<h1>Résultats</h1><br>


		<?php
			if($_SERVER['REQUEST_METHOD'] == 'POST') {// Si formulaire non-validé, ça sert à rien.
          $date1 = $_POST['date1'];
          //echo $date1;
          $now = time();
          //echo $now;
          //$date2 = strtotime('2012-08-14 16:01:05');
          //echo $date2;
          $diff  = abs($now - $date1);
          echo 'Temps de réponse : ' .$diff. ' secondes';

   				print"reponse reçue";
      			if(isset($_POST['cercle'])) {
         			echo "Bravo.\n";
         			print"ouais";
      			}
      			else {
         			echo "Tu n'as pas sélectionné tous les cercles.\n";
         			print"non";
      			}
			}else {
   				echo "Vous n'avez pas validé de commande !\n";
			}
		?>






      	<a href="essayer.php"><button type="button" name="button">Rejouer</button></a>
    	</div>
    	<div id="divd">
        </div>
    </div>
  </body>
</html>
