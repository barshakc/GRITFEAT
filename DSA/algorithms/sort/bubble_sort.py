"""
BUBBLE SORT ALGORITHM
......................
It is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
The pass through the list is repeated until the list is sorted.

Algorithm:
1. Start at the beginning of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat until the end of the array.
5. Repeat the entire process until no swaps are needed.

Pros:
- Simple to implement.
- Works well for small datasets.

Cons:
- Inefficient for large datasets.
- Performs poorly on average and worst-case scenarios.

When to use:
- When the dataset is small.
- When simplicity is preferred over performance.

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

class BubbleSort:
    """
    Class to perform bubble sort on a list.

    Parameters:
    list : list
        The list to be sorted.

    Attributes:
    list : list
        The list of elements to be sorted.

    Methods:
    sort() : list
        Sorts the list using bubble sort algorithm and returns the sorted list.

    Returns:
    list
        The sorted list.

    """
    
    def __init__(self, list):
        self.list = list

    @time_it
    def sort(self):
        """
        Sorts the list using bubble sort algorithm.

        Returns:
        --------
        list
            The sorted list.
        """
        n = len(self.list)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
                    swapped = True
            if not swapped:
                break
        return self.list
    

# Example usage:
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSort(my_list)
    sorted_list = sorter.sort()
    print("Sorted list:", sorted_list)