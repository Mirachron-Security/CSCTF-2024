<?php

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

function generateFlag($salt) {
    date_default_timezone_set('Europe/Bucharest');
    $current_time = time();
    $seconds_passed = date('H', $current_time) * 3600 + date('i', $current_time) * 60 + date('s', $current_time);
    $num_blocks_passed = floor($seconds_passed / 300);  // renew every 300 seconds

    $flag = "CSCTF{}" . $num_blocks_passed . $salt;
    $hashed_flag = hash("sha256", $flag);
    $flag = "CSCTF{" . $hashed_flag . "}";

    return $flag;
}

$salt = "Simple upload";
$flag = generateFlag($salt);

$flagFilePath = "/var/www/html/hidden_secret_flag.php";

file_put_contents($flagFilePath, "<?php\n\$flag = '" . $flag . "';\n?>\n");
?>
