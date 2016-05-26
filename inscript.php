<?php
include_once 'connbdd.php';
mysql_select_db($nom_base_donnees, $conn);
if ($_POST['login']!=null && !empty( $_POST['pass'] && ($_POST['pass'] == $_POST['passv']))) {

$req = "insert into tbl_user (login, pwd) VALUES ('".$_POST['login']."','".$_POST['pass']."')";
mysql_query($req);
include 'redirect.php';
}
elseif ($_POST['pass'] != $_POST['passv']) {
    echo "<h1>Mot de passe différent</h1>";
}
?>
