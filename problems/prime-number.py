"""
Problem: Prime Number
Execution command: python3 problems/prime-number.py
-------------------------------------
Check if a number is prime.
Time Complexity: O(√n)
Space Complexity: O(1)
"""

def count_factors(n):
    """Count the factors of a number.

    Args:
        n (int): The number to count factors for.

    Returns:
        int: The count of factors of n.
    """
    i = 1
    count = 0
    while i * i <= n:
        if n%2 == 0:
            if i*i  == n:
                count += 1
            else:
                count += 2
        i += 1
    return count


def is_prime_number(n):
    """Checks if the given number is prime or not

    Args:
        n (int): The number to check if it is prime
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    count = count_factors(n)
    if count == 2:
        return True
    else:
        return False


# Example usage:
n = 29
if is_prime_number(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")