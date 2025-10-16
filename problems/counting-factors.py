"""
Problem: Count the Factors
Execution command: python3 problems/counting-factors.py
-------------------------------------
Count how many numbers divide n completely.
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
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

# Example usage:
n = 36
print(f"The number of factors of {n} is: {count_factors(n)}")
