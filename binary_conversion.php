<?php
declare(strict_types=1);

$modulus = 256;
$binary = '';
$exit = 0;

do {
    
    $binary = '';
    do {
    echo 'Enter a number between 0 and 255: ' . PHP_EOL;
    $my_number = trim(fgets(STDIN));
    } while (!is_numeric($my_number) || $my_number < 0 || $my_number > 255);

    $backup_number = $my_number;

    // Convert to binary representation manually

    if ($my_number >= 128) {
        $binary .= '1';
        $my_number -= 128;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 64) {
        $binary .= '1';
        $my_number -= 64;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 32) {
        $binary .= '1';
        $my_number -= 32;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 16) {
        $binary .= '1';
        $my_number -= 16;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 8) {
        $binary .= '1';
        $my_number -= 8;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 4) {
        $binary .= '1';
        $my_number -= 4;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 2) {
        $binary .= '1';
        $my_number -= 2;
    } else {
        $binary .= '0';
    }
    if ($my_number >= 1) {
        $binary .= '1';
        $my_number -= 1;
    } else {
        $binary .= '0';
    }
    echo "Binary representation using Maribel method : $binary" . PHP_EOL;


    // Shorter iterative method to convert to binary
    $my_number = (int)$backup_number; // Reset to original number
    $binary_iterative = '';
    $temp = $my_number;
    do {
        $modulus = $my_number % 2;
        $temp = intdiv($temp, 2);
        $binary_iterative = $modulus . $binary_iterative;
    } while ($temp > 0);
    $binary_iterative = str_pad($binary_iterative, 8, '0', STR_PAD_LEFT); // Ensure the binary representation is 1 byte = 8 bits long (ZEROFILL)
    echo "Binary representation using iterative method: $binary_iterative" . PHP_EOL;


    // There is also a built-in function to convert to binary
    $binary_builtin = decbin((int)$backup_number);
    // Ensure the binary representation is 8 bits long (ZEROFILL)
    $binary_builtin = str_pad($binary_builtin, 8, '0', STR_PAD_LEFT);
    echo "Binary representation using built-in function: $binary_builtin" . PHP_EOL;
    echo 'Enter 0 to exit or any other key to continue: ' . PHP_EOL;
    $exit = trim(fgets(STDIN));

} while ($exit !== '0');

echo "Exiting the program." . PHP_EOL;
?>