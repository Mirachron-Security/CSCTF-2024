<!DOCTYPE html>
<html>
<head>
    <title>Access Restricted</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap');

        body {
            font-family: 'Ubuntu', sans-serif;
            text-align: center; 
            margin: 0;
            padding: 0;
        }

        form {
            display: inline-block;
            text-align: center;
        }

        h1 {
            margin-top: 50px; 
        }
    </style>
</head>
<body>
    <h1>Basics #2</h1>

    <?php
    include 'flag.php';
    $userAgent = $_SERVER['HTTP_USER_AGENT'];

    if (stripos($userAgent, 'mini') !== false && 
    stripos($userAgent, 'neo') !== false && 
    stripos($userAgent, 'x5') !== false) {
    echo $flag;
    } else {
    echo 'This website is accessible only by Minix NEO X5';
    }
    ?>

</body>
</html>
