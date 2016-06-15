<?php
session_start();
 ?>
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
  </head>
  <body>
    <div class="header">
      <h1>Shape Finder</h1>
    <hr></hr>
    </div>
      <div class="containerdv">
    <div id="divg">
      <h1>Essayer Shape Finder Gratuitement!</h1>
      <br>
      <a href="essayer.php"><img src="img/geometryshapes.gif"/></a>
    </div>
    <div class="pixel">

    </div>
    <div id="space">
      <hr></hr>
    </div>
    <div id="divd">
      <h1>Inscription / Connexion</h1>
      <?php
      if (isset($_SESSION ['login'])) {
        echo "<a href='include/deconn.php'><img src='img/deco.png'/></a>";
      }
      else {
        echo "<a href='#' data-toggle='modal' data-target='#login-modal'><img src='img/conn.png'/></a>";
      }
      ?>

      <div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
          	  <div class="modal-dialog">
      				<div class="loginmodal-container">
      					<h1>Se connecter</h1><br>
      				  <form method="post" action="include/login.php">
      					<input type="text" name="login" placeholder="Nom d'utilisateur">
      					<input type="password" name="pass" placeholder="Mot de passe">
      					<input type="submit" name="submit" class="login loginmodal-submit" value="Connexion">
      				  </form>
      				</div>
              <div class="loginmodal-container">
                <h1>S'enregistrer</h1><br>
                <form action="include/inscript.php" method="post">
                  <input type="text" name="login" placeholder="Nom d'utilisateur">
                  <input type="text" name="mail" placeholder="Adresse-email">
                  <input type="password" name="pass" placeholder="Mot de passe">
                  <input type="password" name="passv" placeholder="Verif. Mot de passe">
                  <input type="submit" name="submit" class="login loginmodal-submit" value="Inscription">
                </form>
              </div>
            </div>
      			</div>
      		  </div>
</body>
</html>
