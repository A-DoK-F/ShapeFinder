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
      	<h1>Résultats</h1><br>

		<?php
			if($_SERVER['REQUEST_METHOD'] == 'POST') { // vérifie si le formulaire est validé
          $date1 = $_POST['date1']; // récupère le timestamp de debut de question dans une variable
          # echo $date1;
          $now = time(); //recupère le timestamp de maintenant dans une variable
          # echo $now;
          $diff = abs($now - $date1); // fait la différence entre les deux timestamp
          echo 'Temps de réponse : ' .$diff. ' secondes'; // affiche le temps passé à repondre à la question

          if(isset($_POST['valider']) && !empty($_POST['choix'])) {   // on vérifie que le form a été submit et que des cases ont été cochées
             # echo '<pre>';
             # print_r($_POST['choix']);
             # echo '</pre>';
             //on déclare une variable qui contient les values des cases cochées (noms des images sélectionnées)
           	$choix ='';
            INCLUDE 'include/connbdd.php'; // on se connecte à la bdd
           	//on boucle pour récup les values pour chaque case cochée
           	for ($i=0;$i<count($_POST['choix']);$i++) {
           	//on concatène
           	$choix .= $_POST['choix'][$i].'|';
  	        }
  	        # echo $choix; // affiche les (nom des images sélectionnées)
            $explore = explode('|',$choix); // on les sépare pour pouvoir les traiter indépendamment
            # print_r($explore);
            foreach($explore as $valeur) {    // on les stocke dans une variable $valeur
               if(!empty($valeur)){
                   # echo $valeur.'<br/>';
                   //on va chercher la forme de l'image dans la bdd en fonction de son chemin (nom de l'image)
                   $sql = "SELECT * FROM img WHERE NomImage = '$valeur'";
                   $req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());
                   $data = mysql_fetch_assoc($req);
                   $cochee = $data[FormeImage];
                   #print $cochee;
                   // on va chercher la bonne reponse au questionnaire dans la bdd en fonction de son id
                   $sql2 = "SELECT * FROM questionnaire WHERE IdQuestionnaire = 1";
                   $req2 = mysql_query($sql2) or die('Erreur SQL !<br>'.$sql2.'<br>'.mysql_error());
                   $data2 = mysql_fetch_assoc($req2);
                   $reponse = $data2[answer]; // on stocke la réponse dans une variable
                   # print $reponse;
                   echo "<br>Ce qu'il fallait sélectionner : " . $reponse;
                   echo "<br>Ce que tu as sélectionné : " . $cochee;
                   // on compare la forme des images sélectionnées avec la réponse enregistrée dans la base de données
                   if($cochee == $reponse) {
                     echo "<br>Bien joué !";
                     $score = 1;
                     echo "<br>Score = " .$score;
                   }else {
                     echo "<br>Essaye encore";
                     $score = 0;
                   }
               }
           }
         }else{
           echo '<br> Il faut sélectionner au moins une image !';
         }

         // on insère les données de la partie dans la table séance de la bdd
         $sql = "INSERT INTO seances (DateDebut, DateFin, TempsReponse, IdUtilisateur, ScoreSeance)
                 VALUES ($date1, $now, $diff, '2', $score)";
         mysql_query($sql);
        }
        mysql_close($db); // on ferme la connextion à la bdd

        //
        //    *** Trucs à faire :
        //    *** gérer les cas où le joueur coche des bonnes et des mauvaises reponses avec des ifs supplémentaires
        //    *** là j'ai mis 2 comme Id Utilisateur mais il faudra le récupérer en se servant des données de l'utilisateur connecté
        //    *** il faudra le récupérer en se servant des données de l'utilisateur connecté avec un session_start()
        //    *** les dates début et fin ne s'affichent pas dans la bdd, il met des zero, j'ai testé différents type, si vous avz une idée...
        //
        //
		?>


      	<br><br><a href="essayer.php"><button type="button" name="button">Rejouer</button></a>
    	</div>
    	<div id="divd">
        </div>
    </div>
  </body>
</html>
