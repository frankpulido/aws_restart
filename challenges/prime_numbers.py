# Python 3.9.6
# Author: Frank Pulido
# Date: June 10, 2025
# Purpose: Generate prime numbers up to a given limit (default 250)
# File: prime_numbers.py
# Encoding: ASCII (a subset of UTF-8)

def is_prime(number):
    # Determines whether the number is prime
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(limit=250):
    # Generates a list of the prime numbers found up to a given limit.
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d@%H:%M:%S")
    limit = input("Enter the limit for prime number generation (default is 250): ")
    if limit.isdigit():
        limit = int(limit)
    else:
        print("Invalid input. Using default limit of 250.") 
        limit = 250  # Default limit

    import subprocess
    # Create file primes_numbers_results.txt if it does not exist
    subprocess.run(["touch", "prime_numbers_results.txt"])
    # Make a list of prime numbers up to the limit and write the results to the file
    with open("prime_numbers_results.txt", "a") as file:
        file.write(f"{current_date} - Prime numbers up to {limit}:\n")
        primes = generate_primes(limit)
        file.write(", ".join(map(str, primes)) + "\n")
    # Print the results to the console
    print(f"Prime numbers up to {limit} (total found = {len(primes)}):")
    print(primes)


if __name__ == "__main__":
    main()