<?php
$___ = unpack("S*",0x41)[1];
// echo $___,"\n"; 

$payload = serialize(['num' => $___]); 
echo $payload; 

?>
