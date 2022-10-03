<?php
require_once('Archive/Zip.php');

$zip_file = './datas/postcode_temp/temp.zip';
$dir = './datas/postcode_temp/';

$objZip = new Archive_Zip($zip_file);
$p_params = array ('add_path' => $dir);
$result = $objZip->extract($p_params);
sleep(2);
unlink($zip_file);
header("Location: index.cgi?m=postcode&a=zip");
?>