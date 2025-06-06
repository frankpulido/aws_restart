<?php
declare(strict_types=1);

/*
Author: Frank Pulido
Date: June 06, 2025
Purpose: Convert a decimal number to binary representation
File: binary_conversion.php
Encoding: ASCII (a subset of UTF-8)
PHP Version: 8.2.4

This code provides three methods to convert a decimal number (0-255) to its binary representation.
The code is structured to ensure that the user inputs a valid number within the specified range.
The binary representations are padded to 8 bits for consistency.

The first method uses a custom approach (Maribel's method) for 8-bit (1 byte) only, the second uses an iterative approach that works regardless of the number of bits, and the third uses PHP's built-in formatting (also for any number of bits).
The user can input a number, and the program will display the binary representation using all three methods.
The program continues to prompt for input until the user decides to exit.
*/

$modulus = 256;
$binary = '';
$exit = 0;

do {
    
    $binary = '';
    do {
        echo PHP_EOL;
        echo 'Enter a number between 0 and 255: ';
        $my_number = trim(fgets(STDIN));
        echo PHP_EOL;
    } while (!is_numeric($my_number) || $my_number < 0 || $my_number > 255);

    $backup_number = $my_number;

    // METHOD 1: Convert to binary 8-bit (1 byte) representation manually (Maribel)

    $binary = '';
    foreach ([128, 64, 32, 16, 8, 4, 2, 1] as $value) {
        if ($my_number >= $value) {
            $binary .= '1';
            $my_number -= $value;
        } else {
            $binary .= '0';
        }
    }
    echo "Binary representation using Maribel's method : $binary" . PHP_EOL;


    // METHOD 2: Iterative method to convert to binary, regardless of the number of bits

    $my_number = (int)$backup_number; // Reset to original number
    $binary_iterative = '';
    $temp = $my_number;
    do {
        $modulus = $temp % 2;
        $temp = intdiv($temp, 2);
        $binary_iterative = $modulus . $binary_iterative;
    } while ($temp > 0);
    $binary_iterative = str_pad($binary_iterative, 8, '0', STR_PAD_LEFT); // Ensure the binary representation is 1 byte = 8 bits long (ZEROFILL)
    echo "Binary representation using iterative method: $binary_iterative" . PHP_EOL;


    // METHOD 3: There is also a built-in function to convert to binary

    $binary_builtin = decbin((int)$backup_number);
    // Ensure the binary representation is 8 bits long (ZEROFILL)
    $binary_builtin = str_pad($binary_builtin, 8, '0', STR_PAD_LEFT);
    echo "Binary representation using built-in function: $binary_builtin" . PHP_EOL;
    
    echo PHP_EOL;
    echo 'Enter 0 to exit or any other key to continue: ';
    $exit = trim(fgets(STDIN));

} while ($exit !== '0');

echo "Exiting the program." . PHP_EOL;
echo PHP_EOL;
?>