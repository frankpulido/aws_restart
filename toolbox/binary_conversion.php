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
        $my_number = (int)trim(fgets(STDIN));
    } while (!is_numeric($my_number) || $my_number < 0 || $my_number > 255);

    echo PHP_EOL;
    echo "Binary representation using Maribel's method: " . binary8bit($my_number) . PHP_EOL;
    echo "Binary representation using iterative method: " . binaryIterative($my_number) . PHP_EOL;
    echo "Binary representation using built-in function: " . binaryBuiltin($my_number) . PHP_EOL;

    echo PHP_EOL;
    echo 'Enter 0 to exit or any other key to continue: ';
    $exit = trim(fgets(STDIN));

} while ($exit !== '0');

echo "Exiting the program. Thank you for using the binary conversion tool!" . PHP_EOL;
echo PHP_EOL;


// METHOD 1: Convert to binary 8-bit (1 byte) representation manually (Maribel)

function binary8bit(int $number): string {
    $binary = '';
    foreach ([128, 64, 32, 16, 8, 4, 2, 1] as $value) {
        if ($number >= $value) {
            $binary .= '1';
            $number -= $value;
        } else {
            $binary .= '0';
        }
    }
    return $binary;
}

// METHOD 2: Iterative method to convert to binary, regardless of the number of bits

function binaryIterative(int $number): string {
    $binary = '';
    $temp = $number;
    do {
        $modulus = $temp % 2;
        $temp = intdiv($temp, 2);
        $binary = $modulus . $binary;
    } while ($temp > 0);
    if (strlen($binary) < 8) {
        $binary = str_pad($binary, 8, '0', STR_PAD_LEFT); // Ensure the binary representation is 1 byte = 8 bits long (ZEROFILL)
    }
    return $binary;
}

// METHOD 3: There is also a built-in function to convert to binary

function binaryBuiltin(int $number): string {
    $binary = decbin($number);
    if (strlen($binary) < 8) {
        $binary = str_pad($binary, 8, '0', STR_PAD_LEFT); // Ensure the binary representation is 1 byte = 8 bits long (ZEROFILL)
    }
    return $binary;
}

?>