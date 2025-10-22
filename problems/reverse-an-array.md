# Problem Statement
Given an array of size N, reverse the array in place.

## Example
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

## Solution (Python):

1. Brute Force Approach (O(N) Time Complexity, O(N) Space Complexity)

Approach :

a. Directly use the built-in reverse function to reverse the array.

```python
def reverse_array_brute_force(arr):
    return arr[::-1]
```

2. Optimal Approach (O(N) Time Complexity, O(1) Space Complexity)

Approach:
a. Use two pointers. One pointer starts at the beginning of the array, and the other starts at the end. 
b. Swap the elements at these pointers and move the pointers towards each other until they meet in the middle.

```python
def reverse_array(arr):
    start = 0
    end = len(arr)-1
    for i in range(len(arr)//2):
        if arr[start] < arr[end]:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
        start += 1
        end -= 1
    return arr

# Example usage:
input_array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(input_array)
print(reversed_array)  # Output: [5, 4, 3, 2, 1]
```
