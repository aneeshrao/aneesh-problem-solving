## Rotate Array

**Problem Statement:** Given an array of size N, rotate the array to the right by K steps.

### A. Brute Force Approach (O(N*K) Time Complexity)
To rotate the array to the right by K steps, we can perform K rotations, where in each rotation we move the last element to the front of the array.
**Code (Python):**

```python
def rotate_array_brute_force(arr, K):
    N = len(arr)
    K = K % N  # In case K is greater than N
    for _ in range(K):
        last_element = arr[-1]
        for i in range(N-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last_element
    return arr
```

### B. Optimal Approach (O(N) Time Complexity, O(1) Space Complexity)
To rotate the array to the right by K steps, we can use the following approach:
1. Reverse the entire array.
2. Reverse the first K elements.
3. Reverse the remaining N-K elements.

```python
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotate_array(arr, K):
    N = len(arr)
    K = K % N  # In case K is greater than N
    # Step 1: Reverse the entire array
    reverse(arr, 0, N-1)
    # Step 2: Reverse the first K elements
    reverse(arr, 0, K-1)
    # Step 3: Reverse the remaining N-K elements
    reverse(arr, K, N-1)
    return arr
```