"""
INSERTION SORT ALGORITHM 
........................
It is a simple and intuitive sorting algorithm that builds a sorted array one element at a time.

Algorithm:
1. Start with the second element (index 1) of the array.
2. Compare it with the elements before it (the sorted sublist).
3. Shift all larger elements in the sorted sublist to the right.
4. Insert the current element into its correct position.
5. Repeat until the entire array is sorted.

Pros:
- Simple to implement.
- Efficient for small datasets.
- Stable sort.

Cons:
- Inefficient for large datasets.

When to use:
- When the dataset is small or nearly sorted.
- When memory usage is a concern, as it sorts in place.
- When a stable sort is required

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(n)
Average: O(n^2) 
Worst: O(n^2) 

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

class InsertionSort:
    """
    Class to perform insertion sort on a list.

    Parameters
    ----------
    arr : list
        The list of elements to be sorted.

    Attributes
    ----------
    arr : list
        The list to be sorted.

    Methods
    -------
    sort()
        Sorts the list in place using insertion sort and returns it.

    Returns
    -------
    list
        The sorted list.
        
    """

    def __init__(self, arr):
        """
        Initialize the sorter with a list.

        Parameters
        ----------
        arr : list
            The list to be sorted.
        """
        self.arr = arr

    @time_it
    def sort(self):
        """
        Sort the list in place using insertion sort.

        Returns
        -------
        list
            The sorted list.
        """
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr

# --- Example Usage ---
if __name__ == "__main__":
    my_list = [12, 11, 13, 5, 6, 10, 14, 8]
    print(f"Original list: {my_list}")
    sorter = InsertionSort(my_list)
    sorted_list = sorter.sort()
    print(f"Sorted list: {sorted_list}\n")