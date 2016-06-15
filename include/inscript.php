<?php session_start() ?>
<?php
include_once 'connbdd.php';
mysql_select_db($nom_base_donnees, $conn);
$sql_username = 'SELECT * FROM tbl_user WHERE login="'.mysql_real_escape_string($_POST['login']).'"';
$req_username = mysql_query($sql_username) or die('Erreur SQL !<br />'.$sql_username.'<br />'.mysql_error());
$data_username = mysql_fetch_array($req_username);

if ($_POST['login']!=null && !empty( $_POST['mail'] && !empty( $_POST['pass'] && ($_POST['pass'] == $_POST['passv'] && ($data_username[0] == 0))))) {
	$pass_hache = hash('sha256',$_POST['pass']);
$req = "insert into tbl_user (login, pwd) VALUES ('".$_POST['login']."','$pass_hache')";
mysql_query($req);
include 'redirect.php';
}
elseif ($_POST['pass'] != $_POST['passv']) {
    echo "<h1>Mot de passe différent</h1>";
}
elseif($data_username[0] != 0) {
	$error = print "Cet identifiant est déjà pris";
	INCLUDE 'inc/inscription_form.html';
}
?>
