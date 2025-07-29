"""
QUICK SORT ALGORITHM
..................
It is a divide-and-conquer algorithm that sorts an array by selecting a 'pivot' element and 
partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
The sub-arrays are then sorted recursively.

Algorithm:
1. Choose a pivot element from the array.
2. Partition the array into two sub-arrays:
   - Elements less than the pivot.
   - Elements greater than the pivot.
3. Recursively apply the same logic to the sub-arrays.
4. Combine the sorted sub-arrays and the pivot to get the final sorted array.

Pros:
- Efficient for large datasets.
- Requires only a small, constant amount of additional storage space.

Cons:
- Not stable.

When to use:
- When the dataset is large.
- When average-case performance is more important than worst-case performance.

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(n log n)
Average: O(n log n)
Worst: O(n^2)

Space Complexity
----------------
Best: O(log n)
Average: O(log n)
Worst: O(n)

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

class QuickSort:
    """
    Class to perform quick sort on a list.

    Parameters:
    ----------
    arr : list
        The list of elements to be sorted.

    Attributes:
    ----------
    arr : list
        The list of elements to be sorted.

    Methods:
    -------
    sort() : list
        Sorts the list using quick sort algorithm and returns the sorted list.

    Returns
    -------
    list
        The sorted list.
        
    """

    def __init__(self, arr):
        self.arr = arr

    def _quicksort(self, arr):
        """
        Helper method to perform quick sort recursively.

        Parameters
        ----------
        arr : list
            The list to sort.

        Returns
        -------
        list
            The sorted list.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quicksort(left) + middle + self._quicksort(right)

    @time_it
    def sort(self):
        """
        Sorts the array using quick sort algorithm.

        Returns
        -------
        list
            The sorted array.
        """
        return self._quicksort(self.arr)
    
# Example usage:
if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 33, 2, 77, 1, 4]
    quicksort = QuickSort(arr)
    sorted_arr = quicksort.sort()
    print("Sorted array:", sorted_arr)