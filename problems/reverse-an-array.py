"""
Problem: Reverse an Array
Execution command: python3 problems/reverse-an-array.py
-------------------------------------
Reverse the elements of an array in place.
Time Complexity: O(n)
Space Complexity: O(1)  
"""

import re


def reverse_array(arr):
    """Reverse the elements of an array in place.

    Args:
        arr (list): The array to be reversed.
    
    Returns:
        list: The reversed array.
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
array = [1, 2, 3, 4, 5]
print(f"Original array: {array}")
reversed_array = reverse_array(array)
print(f"Reversed array: {reversed_array}")


def reverse_array_for_specific_indices(arr, start, end):
    """Reverse the elements of an array between specific indices in place.

    Args:
        arr (list): The array to be reversed.
        start (int): The starting index for reversal.
        end (int): The ending index for reversal.
    
    Returns:
        list: The array with the specified section reversed.
    """
    left = start
    right = end
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage for specific indices:
array2 = [10, 20, 30, 40, 50, 60]
start_index = 1
end_index = 4
print(f"\nOriginal array: {array2}")
reversed_array_section = reverse_array_for_specific_indices(array2, start_index, end_index)
print(f"Array after reversing from index {start_index} to {end_index}: {reversed_array_section}")

    
