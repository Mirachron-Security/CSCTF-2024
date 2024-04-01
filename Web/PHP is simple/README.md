# PHP basics
Author: [Cujbă Mihai](https://www.linkedin.com/in/mihai-cujb%C4%83-109b8a72/)

<br>

## Description
```
Send a serialized payload for the chosen number
```

<br>

## Requirements
- PHP serialization
- PHP packing of data
- requests

<br>

## Solve
Firstly, make sure you understand the code:

```php
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
```

<br>

- include the flag (`$flag` variable)
- expect a POST request
- store the data in a variable named `_`
    - PHP variables are called with a prepended `$`
- deserialize the data sent 
- `unpack` interprets the hexadecimal value `0x41` as an array of unsigned short integers
    - use [1] to extract only the value from the array
    ```php
    <?php
    $___ = unpack("S*",0x41);
    print_r($___); // Display the entire array

    ?>
    ```
    ```
    Array
    (
        [1] => 13622
    )
    ```
- check if the deserialized value contains a `num` variable equal to the unpacked data.

<br>

To solve the challenge, reverse the process and send the data: [`serialize.php`](./create/serialize.php)
```php
<?php
$___ = unpack("S*",0x41)[1];
echo $___,"\n"; 

$payload = serialize(['num' => $___]); 
echo $payload; 

?>
```
```bash
php serialize.php

13622
a:1:{s:3:"num";i:13622;}    
```

<br>

Now, put everything together in a [`solve.py`](./solve/solve.py) script.
```bash
python3 solve.py chal.chronossec.site 30230
```

<br>

> Flag: `CSCTF{PHP_serialize_and_pack_your_numbers}`