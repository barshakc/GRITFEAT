"""
BINARY SEARCH ALGORITHM
.......................
It is a searching algorithm that finds the position of a target value within a sorted array.
It compares the target value to the middle element of the array.

Algorithm:
1. Start with the middle element of the array.
2. If the middle element is equal to the target value, return its index.
3. If the target value is less than the middle element, repeat the search on the left half of the array.
4. If the target value is greater than the middle element, repeat the search on the right half of the array.
5. If the target value is not found, return -1.

Pros:
- Efficient for large datasets.
- Requires fewer comparisons than linear search.
- Works only on sorted arrays.

Cons
- Requires the array to be sorted.
- Not suitable for small datasets.

When to use:
- When the dataset is large and sorted.
- When you need to perform multiple searches on the same dataset.

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(1)
Average: O(log n)
Worst: O(log n)

Space Complexity
----------------
Best: O(1)
Average: O(1)
Worst: O(1)

"""

import time
import logging

logging.basicConfig(level=logging.INFO)

def time_it(func):
    """
    A decorator that measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        logging.info(f"'{func.__name__}' executed in {execution_time:.4f} ms")
        return result
    return wrapper

class BinarySearch:
    """
    Class to perform binary search on a sorted list.
    """
    def __init__(self):
        pass

    @time_it
    def search(self, arr, target):
        """
        Perform binary search on a sorted array.

        Parameters:
        arr (list): The sorted array to search in.
        target (int): The value to search for.

        Methods:
        search(arr, target) -> int:
            Returns the index of the target value if found, otherwise -1.

        Returns:
        int: The index of the target value if found, otherwise -1.
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

# Example usage:
if __name__ == "__main__":
    bs = BinarySearch()
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_value = 5
    index = bs.search(sorted_array, target_value)
    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found in the array.")