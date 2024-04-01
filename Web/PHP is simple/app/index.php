<?php
include 'flag.php';
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $_ = file_get_contents("php://input");
    $__ = unserialize($_);
    $___ = unpack("S*",0x41)[1];
    if($__['num'] == $___){echo $flag;}
}else{
    highlight_file(__FILE__);
}
?>
