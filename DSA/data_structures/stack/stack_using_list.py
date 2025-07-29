"""
STACK DATA STRUCTURE
..........................
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. 
LIFO means that the last element added to the stack is the first one to be removed.

Operations:
1. Push: Add an element to the top of the stack.
2. Pop: Remove and return the top element of the stack.
3. Peek: Return the top element without removing it.
4. is_empty: Check if the stack is empty.
5. size: Return the number of elements in the stack.

Properties:
- The stack grows and shrinks as elements are added or removed.
- The stack can be implemented using various data structures, such as arrays or linked lists.
- Only the top element is accessible.

Pros:
- Simple and efficient for managing data that follows LIFO order.
- Useful for function call management, expression evaluation, and backtracking algorithms.
- Easy to implement.

Cons:
- Limited access to elements (only the top element can be accessed).
- Fixed size if implemented using arrays, which can lead to overflow.
- Not suitable for scenarios where random access is required.

When to use a stack:
- When we need to reverse items (e.g., reversing a string).
- When implementing undo functionality in applications.
- When managing function calls in programming languages (call stack)

When not to use a stack:
- When we need to access elements in a non-LIFO order.
- When we need to frequently access elements in the middle of the collection.
- When we need to store large amounts of data that may exceed the stack's capacity.

Keyword arguments:
argument -- description
Return: return_description
"""

class Stack:
    """
    Stack implementation using a Python list.

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
    _values : list
        Internal storage for stack elements.
    """
    
    def __init__(self):
        """
        Initialize an empty stack.

        Time complexity: O(1)
        Space complexity: O(n) 
        """
        self._values = []

    def push(self, value):
        """
        Add an element to the top of the stack.

        Parameters
        ----------
        value : object
            The element to be added to the stack.

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
            return self._values.pop()
        raise IndexError("pop from empty stack")

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
            return self._values[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise.
        
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
        Return the number of elements in the stack.

        Returns
        -------
        int
            The number of elements in the stack.
        
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
       Return a user-friendly visual representation of the stack 
       from top to bottom.

       Returns
       -------
       str
        A string showing the stack elements from top to bottom.

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
        return "Stack is empty"
       return "Top -> " + " -> ".join(str(value) for value in reversed(self._values))


    def __repr__(self):
        """
        Return a detailed string representation of the stack.

        Returns
        -------
        str
            Detailed string representation of the stack.
        
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
        return f"Stack({self._values})"

    
# Example usage:
if __name__ == "__main__":
    s = Stack()
    print("Initial stack:", s)  
    s.push(12)
    s.push(23)
    s.push(34)
    s.push(42)
    print("After push:",s)  
    print("Pop:",s.pop())  
    print("After pop:", s)
    print("Peek:",s.peek())  
    print("After peek:", s)
    print("Size of stack:",s.size())
    print("Is stack empty?", s.is_empty())
    
    
