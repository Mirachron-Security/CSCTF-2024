<!DOCTYPE html>
<html>
<head>
    <title>Secret Password Form</title>
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
    <h1>Basics #1</h1>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
        <input type="text" id="secretpassword" name="secretpassword" placeholder="secret password"><br><br>
        <input type="submit" value="Submit">
    </form> 

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $submittedPassword = $_POST["secretpassword"];

        $correctPassword = 'cHHyyRgJFQzF';

        if ($submittedPassword === $correctPassword) {
            echo '<p>Congratulations! You got the flag!</p>';
            echo file_get_contents('flag.php'); 
            
        } else {
            echo '<p>Try again.</p>';
        }
    }
    ?>
</body>
</html>















<!-- secretpassword:cHHyyRgJFQzF -->