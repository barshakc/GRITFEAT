
class Node:
    """
    Node for singly linked list.

    Parameters
    ----------
    value : object
        The value to store in the node.
    next : Node, None
        Reference to the next node. Default is None.

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

class Stack:
    """
    Stack implementation using a singly linked list.

    Methods
    -------
    push(value)
        Add an element to the top of the stack.
    pop()
        Remove and return the top element of the stack.
    peek()
        Return the top element without removing it.
    is_empty()
        Check if the stack is empty.
    size()
        Return the number of elements in the stack.

    Parameters
    ----------
    None

    Attributes
    ----------
    _top : Node or None
        Reference to the top node of the stack.
    count : int
        Number of elements in the stack.
    """

    def __init__(self):
        """Initialize an empty stack.
        
        Time complexity: O(1)
        Space complexity: O(1)
        
        """

        self._top = None
        self._count = 0

    def push(self, value):
        """
        Add an element to the top of the stack.

        Parameters
        ----------
        value : object
            The element to be added to the stack.
        """
        new_node = Node(value)
        new_node.next = self._top
        self._top = new_node
        self._count += 1

    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns
        -------
        object
            The top element of the stack.

        Raises
        ------
        IndexError
            If the stack is empty.

        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._top.value
        self._top = self._top.next
        self._count -= 1
        return value

    def peek(self):
        """
        Return the top element without removing it.

        Returns
        -------
        object
            The top element of the stack.

        Raises
        ------
        IndexError
            If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise.
        """
        return self._top is None

    def size(self):
        """
        Return the number of elements in the stack.

        Returns
        -------
        int
            The number of elements in the stack.
        """
        return self._count

    def __str__(self):
        """
        Return a string representation of the stack from top to bottom.

        Returns
        -------
        str
            String representation of the stack.
        """
        values = []
        current = self._top
        while current:
            values.append(str(current.value))
            current = current.next
        return "Top -> " + " -> ".join(values)

    def __repr__(self):
        """
        Return a detailed string representation of the stack.

        Returns
        -------
        str
            Detailed string representation of the stack.
        """
        return f"Stack(size={self._count})"

# Example usage:
if __name__ == "__main__":
    s = Stack()
    print("Initial stack:", s)
    s.push(10)
    s.push(20)
    s.push(30)
    print("After push:", s)
    print("Pop:", s.pop())
    print("After pop:", s)
    print("Peek:", s.peek())
    print("Size of stack:", s.size())
    print("Is stack empyty?", s.is_empty())