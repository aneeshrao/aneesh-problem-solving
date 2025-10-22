"""
Problem: Rotate an Array
Execution command: python3 problems/rotate-array.py
-------------------------------------
Rotate the elements of an array to the right by k steps.
Time Complexity: O(n)
Space Complexity: O(1)
"""

def rotate_array(arr, k):
    """Rotate the elements of an array to the right by k steps.

    Args:
        arr (list): The array to be rotated.
        k (int): The number of steps to rotate the array.
    
    Returns:
        list: The rotated array.
    """
    n = len(arr)
    k = k % n  # In case k is greater than n

    # Helper function to reverse a portion of the array
    def reverse_section(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse_section(0, n - 1)
    # Reverse the first k elements
    reverse_section(0, k - 1)
    # Reverse the remaining n-k elements
    reverse_section(k, n - 1)

    return arr