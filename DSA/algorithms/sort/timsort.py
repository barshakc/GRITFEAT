"""
TIMSORT ALGORITHM
..................
It is a hybrid sorting algorithm derived from merge sort and insertion sort.
It is designed to perform well on many kinds of real-world data.

Algorithm:
1. Divide the array into small segments called "runs".
2. Sort each run using insertion sort.
3. Merge the sorted runs using a modified merge sort.

Pros:
- Efficient for large datasets.
- Adaptive.
- Stable sort.

Cons:
- More complex to implement than simpler algorithms.
- Requires additional memory for merging.

When to use:
- When the dataset is large.
- When the dataset is partially sorted.
- When a stable sort is required.

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)

Space Complexity
----------------
Best: O(n)
Average: O(n)
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

class Timsort:
    """
    Class to perform Timsort on a list.

    Parameters:
    ----------
    arr : list
        The list of elements to be sorted.

    Attributes:
    ----------
    arr : list
        The list of elements to be sorted.
    min_run : int
        The minimum size of a run.

    Methods:
    -------
    sort() : list
        Sorts the list using Timsort algorithm and returns the sorted list.

    Returns
    -------
    list
        The sorted list.
    
    """

    def __init__(self, arr):
        self.arr = arr
        self.min_run = 32 

    @time_it
    def sort(self):
        """
        Sorts the array using Timsort algorithm.
        """
        n = len(self.arr)
        if n < 2:
            return self.arr
        
        # Sort individual runs using insertion sort
        for start in range(0, n, self.min_run):
            end = min(start + self.min_run, n)
            self.insertion_sort(start, end)

        # Merge runs
        size = self.min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = min(n, start + size)
                end = min((start + size * 2), n)
                self.merge(start, mid, end)
            size *= 2

        return self.arr

    def insertion_sort(self, left, right):
        """
        Sorts a portion of the array using insertion sort.
        """
        for i in range(left + 1, right):
            key = self.arr[i]
            j = i - 1
            while j >= left and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def merge(self, left, mid, right):
        """
        Merges two sorted subarrays.
        """
        if mid >= right:
            return
        
        left_copy = self.arr[left:mid]
        right_copy = self.arr[mid:right]

        left_index, right_index = 0, 0
        sorted_index = left

        while left_index < len(left_copy) and right_index < len(right_copy):
            if left_copy[left_index] <= right_copy[right_index]:
                self.arr[sorted_index] = left_copy[left_index]
                left_index += 1
            else:
                self.arr[sorted_index] = right_copy[right_index]
                right_index

#Example usage:
if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19, 33, 2, 77, 1, 4]
    timsort = Timsort(arr)
    sorted_arr = timsort.sort()
    print("Sorted array:", sorted_arr)