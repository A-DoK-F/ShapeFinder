<?php
include_once 'conbdd.php';
mysql_select_db($nom_base_donnees, $conn);
$sql = "select festival from Festivals where lieux= 'ardeche'";
$req = mysql_query($sql) or die('Erreur SQL !<br>'.$sql.'<br>'.mysql_error());
$data = mysql_fetch_assoc($req);

print $data['festival'];
?>
