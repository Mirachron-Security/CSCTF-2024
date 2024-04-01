<?php
// Set the cookie before any output
if (!isset($_COOKIE['user']) || $_COOKIE['user'] !== 'admin') {
    setcookie('user', 'guest', time() + 3600, '/');
    $_COOKIE['user'] = 'guest'; 
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Listing</title>
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
<h1>Basics #4</h1>
<?php
// Now that headers are already sent, you can safely output content.
if (isset($_COOKIE['user'])) {
    if ($_COOKIE['user'] === 'guest') {
        echo 'Hello, guest!';
    } elseif ($_COOKIE['user'] === 'admin') {
        include 'flag.php';
        echo $flag; 
    }
} else {
    echo 'Unknown user';
}
?>
</body>
</html>
