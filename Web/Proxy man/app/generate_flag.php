<?php

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

function generate_flag($salt) {
    date_default_timezone_set('Europe/Bucharest');
    $current_time = time();
    $seconds_passed = date('H', $current_time) * 3600 + date('i', $current_time) * 60 + date('s', $current_time);
    $num_blocks_passed = floor($seconds_passed / 300);  // renew every 300 seconds

    $flag = "CSCTF{}" . $num_blocks_passed . $salt;
    $hashed_flag = hash("sha256", $flag);
    $flag = "CSCTF{" . $hashed_flag . "}";

    return $flag;
}

if(isset($_GET['generate_flag'])) {
    $salt = "Proxy man";
    $flag = generate_flag($salt);
    echo json_encode(['flag' => $flag]);
}
?>
