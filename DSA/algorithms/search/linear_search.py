"""
LINEAR SEARCH ALGORITHM
.......................
It is a simple searching algorithm that checks each element in the array sequentially until the target value is found or the end of the array is reached.

Algorithm:
1. Start from the first element of the array.
2. Compare the current element with the target value.
3. If the current element is equal to the target value, return its index.
4. If the current element is not equal, move to the next element.
5. Repeat steps 2-4 until the target value is found or the end of the array is reached.
6. If the target value is not found, return -1.

Pros:
- Simple and easy to implement.
- Does not require the array to be sorted.
- Works on any data type.

Cons:
- Inefficient for large datasets.

When to use:
- When the dataset is small.
- When the dataset is unsorted.

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(1)
Average: O(n)
Worst: O(n)

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

class LinearSearch:
    """
    Class to perform linear search on a list.
    """
    def __init__(self):
        pass

    @time_it
    def search(self, arr, target):
        """
        Perform linear search on the array.

        Parameters:
        arr : list 
            The list of elements to be searched.
        target : any
            The element to search for in the list.
        
        Methods:
        search(arr, target) -> int:
            Returns the index of the target element if found, otherwise -1.

        Returns:
        int : The index of the target element if found, otherwise -1.

        """
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1
    
# Example usage:
if __name__ == "__main__":
    ls = LinearSearch()
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = ls.search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")