<?php
      $DBASE = "ShapeFinder";         // Nom base de données
      $USER = "alex_";      // Login utilisateur localhost
      $PASS = "alex_";         // pass_mbword localhost
      $SERVER = "94.76.204.85";  //  localhost Server
      //
      //$nomsite = "Connection base de données site mabase";
      //$db = mysql_connect($SERVER, $USER, $pass_mb) or die("Impossible de se connecter à la base de donn&eacute;es du site web.");
      //$db = mysql_connect('mysql5-24.bdb', 'saelt','marius971');

      //********** Cette connnexion est fonctionnelle******************
      $db = mysql_connect($SERVER, $USER, $PASS);
        if (!$db) {
          die('Connexion impossible : ' . mysql_error());
      	  //On peut imaginer ici orienter le visiter ou l'administrateur (back-end) sur une page d'erreur personnalisée
        } else {
          //echo "<center><h1 style='color:purple'>Bienvenue !</h1></center>";
          //echo "<h2>Vous êtes bien connecté à $DBASE.</h2>";
          mysql_select_db($DBASE,$db);
        }
        //mysql_close($db); //Ici je ferme la connexion, ce qui peut-être embétant pour les traitements suivants !
        //**************************************************************************
      ?>
