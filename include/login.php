<?php session_start() ?>
<?php
 include_once 'connbdd.php';
	mysql_select_db($nom_base_donnees, $conn);
if(isset($_POST) && !empty($_POST['login']) && !empty($_POST['pass'])) {
 extract($_POST);
 $pass_hache = hash('sha256',$_POST['pass']);

 $sql = "select pwd from tbl_user where login='".$login."'";
 $req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());
 $data = mysql_fetch_assoc($req);


 if($data['pwd'] != $pass_hache) {
   echo '<p>Mauvais login / password. Merci de recommencer</p>';
   include('connection.php');
   exit;
 }
 else {
   session_start();
   $_SESSION['login'] = $login;
   echo "Connexion réussie";
   include 'redirection.php';
 }
}
else {
 echo '<p>Vous avez oublié de remplir un champ.</p>';
  include('connection.php');
  exit;
}
?>
