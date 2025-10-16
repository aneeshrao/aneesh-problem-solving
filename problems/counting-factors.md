## Count the Factors

### A. Brute Force Approach (O(N) Time Complexity)

To count the factors of a number `N`, iterate through all integers from 1 to `N` and check if each divides `N` evenly.

**Code (Python):**

```python
def count_factors_brute_force(N):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    return count
```

**Note:**  
This approach is inefficient for large values of `N` because standard machines can perform about $10^8$ operations per second.

- For $N = 10^8$: ~1 second  
- For $N = 10^9$: ~10 seconds  
- For $N = 10^{10}$: ~100 seconds  
- For $N = 10^{12}$: ~10,000 seconds  
- For $N = 10^{18}$: ~$10^{10}$ seconds (over 300 years)

#### Problem Trace

Let's trace the function for `N = 24`:

- Factors: 1, 2, 3, 4, 6, 8, 12, 24
- Pairs of factors (`i` and `N/i`):
  - 1 and 24
  - 2 and 12
  - 3 and 8
  - 4 and 6

Notice that after $\sqrt{N}$, the pairs start repeating. So, we can stop at $\sqrt{N}$.

---

### B. Optimized Approach (O(√N) Time Complexity)

To optimize the factor counting, iterate only up to the square root of `N`. For each integer `i` that divides `N`, both `i` and `N/i` are factors.

**Code (Python):**

```python
def count_factors_optimized(N):
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            count += 1  # Count the factor i
            if i != N // i:
                count += 1  # Count the factor N/i if it's different
        i += 1
    return count
```

**Note:**  
This approach is much more efficient for large values of `N`. ($N > 10^9$ can be computed in under a second).

#### Problem Trace

**For $N = 36$:**

- Factors up to $\sqrt{36}$: 1, 2, 3, 4, 6
- Pairs:
  - 1 and 36
  - 2 and 18
  - 3 and 12
  - 4 and 9
  - 6 and 6 (counted once)

**For $N = 100$:**

- Factors up to $\sqrt{100}$: 1, 2, 4, 5, 10
- Pairs:
  - 1 and 100
  - 2 and 50
  - 4 and 25
  - 5 and 20
  - 10 and 10 (counted once)


**Important Note:**

How to write square root in code?

```python
import math
math.sqrt(N)
```

or 

```python
i * i <= N
```