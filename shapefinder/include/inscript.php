
<?php
include_once 'connbdd.php';
mysql_select_db($nom_base_donnees, $conn);
if ($_POST['login']!=null && !empty( $_POST['mail'] && !empty( $_POST['pass'] && ($_POST['pass'] == $_POST['passv'])))) {
	$pass_hache = hash('sha256',$_POST['pass']);
$req = "insert into tbl_user (login, pwd) VALUES ('".$_POST['login']."','$pass_hache')";
mysql_query($req);
include 'redirect.php';
}
elseif ($_POST['pass'] != $_POST['passv']) {
    echo "<h1>Mot de passe différent</h1>";
}
?>
