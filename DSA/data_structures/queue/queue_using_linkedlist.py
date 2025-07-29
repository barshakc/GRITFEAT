class Node:
    """
    Node for singly linked list.

    Parameters
    ----------
    value : object
        The value to store in the node.
    next : Node, optional
        Reference to the next node (default is None).

    Attributes
    ----------
    value : object
        The value stored in the node.
    next : Node or None
        Reference to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
    Queue implementation using a singly linked list.

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
    _front : Node or None
        Reference to the front node of the queue.
    _rear : Node or None
        Reference to the rear node of the queue.
    count : int
        Number of elements in the queue.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self._front = None
        self._rear = None
        self.count = 0

    def enqueue(self,_value):
        """
        Add an element to the end of the queue.

        Parameters
        ----------
        value : object
            The element to be added to the queue.
        """
        new_node = Node(_value)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self.count += 1

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
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._front._value
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self.count -= 1
        return value

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
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._front._value

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return self._front is None

    def size(self):
        """
        Return the number of elements in the queue.

        Returns
        -------
        int
            The number of elements in the queue.
        """
        return self.count

    def __str__(self):
        """
        Return a string representation of the queue from front to rear.

        Returns
        -------
        str
            String representation of the queue.
        """
        values = []
        current = self._front
        while current:
            values.append(str(current.value))
            current = current.next
        return "Front -> " + " -> ".join(values) + " -> Rear"

    def __repr__(self):
        """
        Return a detailed string representation of the queue.

        Returns
        -------
        str
            Detailed string representation of the queue.
        """
        return f"Queue(size={self._count})"

# Example usage:
if __name__ == "__main__":
    q = Queue()
    print("Initial queue:", q)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("After enqueue:", q)
    print("Dequeue:", q.dequeue())
    print("After dequeue:", q)
    print("Peek:", q.peek())
    print("Size of queue:", q.size())
    print("Is queue empty?", q.is_empty())
