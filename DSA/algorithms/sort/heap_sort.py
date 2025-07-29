"""
HEAP SORT ALGORITHM
..................
It is a comparison-based sorting algorithm that uses a binary heap data structure.
It first builds a max heap from the input data, and then repeatedly extracts the maximum element from the heap to build the sorted array.

Algorithm:
1. Build a max heap from the input array.
2. Swap the root of the heap (maximum element) with the last element of the heap.
3. Reduce the size of the heap by one.
4. Heapify the root of the heap to maintain the max heap property.
5. Repeat steps 2-4 until the heap is empty.

Pros:
- Efficient for large datasets.
- In-place sort.
- Does not require additional memory for merging.

Cons:
- Not a stable sort.

When to use:
- When the dataset is large.
- When memory usage is a concern, as it sorts in place.

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

class HeapSort:
    """
    A class that implements the Heap Sort algorithm.

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
        Sorts the list using Heap Sort algorithm and returns the sorted list.

    Returns:
    -------
    list
        The sorted list.

    """

    def __init__(self, arr):
        self.arr = arr

    @time_it
    def sort(self):
        n = len(self.arr)

        # Building a max heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(n, i)

        # Extracting elements from the heap one by one
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]  
            self._heapify(i, 0)

        return self.arr

    def _heapify(self, n, i):
        largest = i  
        left = 2 * i + 1  
        right = 2 * i + 2  

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i] 
            self._heapify(n, largest)

# Example usage:
if __name__ == "__main__":
    arr = [12, 19, 30, 5, 6, 27, 10, 45]
    heap_sort = HeapSort(arr)
    sorted_arr = heap_sort.sort()
    print("Sorted array:", sorted_arr)