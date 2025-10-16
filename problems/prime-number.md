## Prime Numbers
**Problem Statement:** Given a number `n`, determine if it is a prime number.

### A. Brute Force Approach (O(N) Time Complexity)

To check if a number `n` is prime, iterate through all integers from 2 to `n-1` and check if any of them divides `n` evenly. If you find any such divisor, `n` is not prime.
**Code (Python):**

```python
def is_prime_brute_force(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

**Note:**  
This approach is inefficient for large values of `n` because standard machines can perform about $10^8$ operations per second. For larger values of `n`, consider using more efficient algorithms.

### B. Optimized Approach (O(√N) Time Complexity)

We already have a code to count the factors of a number. A number is prime if and only if it has exactly 2 factors: 1 and itself. We can use the optimized factor counting method to determine if `n` is prime.

**Code (Python):**

```python
def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # call the optimized factor counting method which we already solved in the previous problem. file -> counting-factors.py
    count = count_factors(n)
    if count == 2:
        return True
    return False
```

**Note:**  
This approach is more efficient than the brute force method, especially for larger values of `n`. However, for extremely large numbers, consider using advanced techniques like the Miller-Rabin primality test.