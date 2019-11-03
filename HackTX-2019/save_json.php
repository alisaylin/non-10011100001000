<?php
    $stringData = $_POST["data"];
    $myfile = file_put_contents('user.json', $stringData.PHP_EOL , FILE_APPEND | LOCK_EX);
?>