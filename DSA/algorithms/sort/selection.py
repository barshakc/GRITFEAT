"""
SELECTION SORTING ALGORITHM
............................
It is a simple and intuitive sorting algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion of the array and moves it to the sorted portion.

Algorithm:
1. Start with the first element as the minimum.
2. Compare it with the rest of the elements to find the smallest.
3. Swap the smallest element with the first element.
4. Move to the next element and repeat until the entire array is sorted.

Pros:
- Simple to implement.
- Works well for small datasets.
- In-place sort.

Cons:
- Inefficient for large datasets.

When to use:
- When the dataset is small.
- When memory usage is a concern, as it sorts in place.

Keyword arguments:
argument -- description
Return: return_description

Time Complexity
----------------
Best: O(n^2)
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

class SelectionSort:
    """
    Class to perform selection sort on a list.

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
        Sorts the array using selection sort algorithm and returns the sorted array.

    Returns
    -------
    list
        The sorted array.

    """

    def __init__(self, arr):
        """
        Initialize the sorter with a list.

        Parameters:
        ----------
        arr : list
            The list of elements to be sorted.
        """

        self.arr = arr

    @time_it
    def sort(self):
        """
        Sorts the array using selection sort algorithm.

        Returns:
        -------
        list
            The sorted array.

        """
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr
    

#Example usage
if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11, 10, 14, 8]
    print(f"Original list: {my_list}")
    sorter = SelectionSort(my_list)
    sorted_list = sorter.sort()
    print(f"Sorted list: {sorted_list}")

