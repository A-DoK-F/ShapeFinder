<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Projetjuin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <link rel="stylesheet" href="style/stylesheet.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  </head>
  <body>
    <div class="header">
      <h1>Shape Finder</h1>
      <hr></hr>
    </div>
      <div class="containerdv">
    <div id="divg">
      <h1>Essayer Shape Finder Gratuitement!</h1>
      <img src="img/geometryshapes.gif"/><br>
      <a href="essayer.php"><button type="button" name="button">Essayer Maintenant</button></a>
    </div>
    <div id="divd">
      <h1>Inscription / Connexion</h1>
      <img src="img/geometryshapes.gif"/><br>
      <a href="#" data-toggle="modal" data-target="#login-modal"><button>Connexion/Inscription</button></a>

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
