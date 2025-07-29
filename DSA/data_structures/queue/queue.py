"""
QUEUE DATA STRUCTURE
..........................
A queue follows the principle of "First in, First out" (FIFO).
FIFO means that the first element added to the queue is the first one to be removed.

Operations:
1. Enqueue: Add an element to the end of the queue.
2. Dequeue: Remove and return the front element of the queue.
3. Peek: Return the front element without removing it.
4. is_empty: Check if the queue is empty.
5. size: Return the number of elements in the queue.

Properties:
- The queue grows and shrinks as elements are added or removed.
- The queue can be implemented using various data structures, such as arrays or linked lists.
- Only the front element is accessible.
- Elements are processed in the order they were added.

Pros:
- Simple and efficient for managing data that follows FIFO order.
- Useful for scheduling tasks, managing resources, and handling requests in order.
- Easy to implement.

Cons:
- Limited access to elements (only the front element can be accessed).
- Fixed size if implemented using arrays, which can lead to overflow.
- Not suitable for scenarios where random access is required.

When to use a queue:
- When we need to process items in the order they arrive.
- When implementing breadth-first search algorithms.
- When managing tasks in a multi-threaded environment.

When not to use a queue:
- When we need to access elements in a non-FIFO order.
- When we need to frequently access elements in the middle of the collection.
- When we need to store large amounts of data that may exceed the queue's capacity.

Keyword arguments:
argument -- description
Return: return_description

"""


class Queue:
    """
    A simple queue implementation using a Python list.

    Methods
    -------
    enqueue(value)
        Add an element to the end of the queue.
    dequeue()
        Remove and return the front element of the queue.
    peek()
        Return the front element without removing it.
    is_empty()
        Check if the queue is empty.
    size()
        Return the number of elements in the queue.

    Parameters
    ----------
    None

    Attributes
    ----------
    _values : list
        Internal storage for queue elements.
    """

    def __init__(self):
        """Initialize an empty queue.
        
        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        
        Space complexity
        ----------------
        Best : O(n)
        Average : O(n)  
        Worst : O(n)
        
        """
        self._values = []

    def enqueue(self, value):
        """
        Add an element to the end of the queue.

        Parameters
        ----------
        value : object
            The element to be added to the queue.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(n)
        
        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(n)

        """
        self._values.append(value)

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns
        -------
        object
            The front element of the queue.

        Raises
        ------
        IndexError
            If the queue is empty.

        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)
        
        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(1)

        """
        if not self.is_empty():
            return self._values.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """
        Return the front element without removing it.

        Returns
        -------
        object
            The front element of the queue.

        Raises
        ------
        IndexError
            If the queue is empty.
        
        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        
        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(1)

        """
        if not self.is_empty():
            return self._values[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        
        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        
        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(1)

        """
        return len(self._values) == 0

    def size(self):
        """
        Return the number of elements in the queue.

        Returns
        -------
        int
            The number of elements in the queue.
        
        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        
        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(1)

        """
        return len(self._values)

    def __str__(self):
        """
        Return a string representation of the queue.

        Returns
        -------
        str
            String representation of the queue.

        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)
        
        Space complexity
        ----------------
        Best : O(n)
        Average : O(n)  
        Worst : O(n)

        """
        if self.is_empty():
          return "Queue is empty"
        return "Front -> " + " -> ".join(str(value) for value in self._values) + " -> Rear"
    
    def __repr__(self):
        """
        Return a detailed string representation of the queue.

        Returns
        -------
        str
            Detailed string representation of the queue.
        
        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)
        
        Space complexity
        ----------------
        Best : O(n)
        Average : O(n)  
        Worst : O(n)

        """
        return f"Queue({self._values})"
    

# Example usage:
if __name__ == "__main__":
    q = Queue()
    print("Initial queue:", q)  
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print("After enqueue:", q)  
    print("Dequeue:", q.dequeue())  
    print("After dequeue:", q)
    print("Peek:", q.peek())  
    print("After peek:", q)
    print("Size of queue:", q.size())
    print("Is queue empty?", q.is_empty())