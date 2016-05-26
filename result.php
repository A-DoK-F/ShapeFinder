<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Projetjuin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <link rel="stylesheet" href="stylesheet_jeu.css">
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
      <h1>Résultats</h1><br>
      BRAVO!
      <button type="button" name="button"><a href="essayer.php">Rejouer</a></button>
    </div>
    <div id="divd">
      <h1>Inscription / Connexion</h1>
      <img src="geometryshapes.gif"/><br>
      <a href="#" data-toggle="modal" data-target="#login-modal"><button>Connexion</button></a>

      <div class="modal fade" id="login-modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
          	  <div class="modal-dialog">
      				<div class="loginmodal-container">
      					<h1>Se connecter</h1><br>
      				  <form method="post">
      					<input type="text" name="user" placeholder="Nom d'utilisateur">
      					<input type="password" name="pass" placeholder="Mot de passe">
      					<input type="submit" name="login" class="login loginmodal-submit" value="Connexion">
      				  </form>

      				  <div class="login loginmodal-submit">
      					<a href="#">Inscription</a>
      				  </div>
      				</div>
      			</div>
      		  </div>
    </div>
      </div>
</body>
</html>
