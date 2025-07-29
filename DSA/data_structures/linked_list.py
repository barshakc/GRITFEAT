"""
LINKED LIST DATA STRUCTURE
..........................
A linked list is a linear data structure where elements, called nodes, are stored in a sequence.
Each node contains a value and a reference(pointer) to the next node in the sequence.

Operations: 
1. Insert: Add a new node to the linked list.
2. Delete: Remove a node from the linked list.
3. Search: Find a node with a specific value.
4. Traverse: Visit each node in the linked list.
6. Peek: Return the value of the first node without removing it.
7. is_empty: Check if the linked list is empty.
8. size: Return the number of nodes in the linked list.

Properties:
- The linked list grows and shrinks as nodes are added or removed.
- Each node contains a value and a reference to the next node.
- The first node is called the head, and the last node points to null.
- The linked list can be singly linked or doubly linked.

Pros:
- Dynamic size.
- Adding or removing nodes is quick.
- They do not have a predefined size.
- Can easily implement stacks and queues using linked lists.

Cons:
- More memory overhead due to storing pointers.
- Accessing elements is slower than arrays.
- No direct access to elements.

When to use a linked list:
- When we need a dynamic data structure that can grow and shrink.
- When we need to frequently insert or delete elements.
- When we need to implement data structures like stacks or queues.

When not to use a linked list:
- When we need fast access to elements by index.
- When memory overhead is a concern.

Keyword arguments:
argument -- description
Return: return_description

"""


class Node:
    """
    A node in a singly linked list.

    Parameters
    ----------
    value : object
        The value to store in the node.
    next : Node or None
        Reference to the next node. Default is None.
            
    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the list.
    
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list implementation.

    Methods
    -------
    insert(value)
        Insert a new node with the given value at the end of the linked list.
    delete(value)
        Remove the first node with the specified value from the linked list.
    search(value)
        Search for a node with the specified value and return it.
    traverse()
        Traverse the linked list and return a list of values.
    peek()
        Return the value of the first node without removing it.
    is_empty()
        Check if the linked list is empty.
    size()
        Return the number of nodes in the linked list.

    Parameters
    ----------
    None

    Attributes
    ----------
    _head: The first node in the linked list.
    count: The number of nodes in the linked list.
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
    
        self._head = None
        self.count = 0

    def insert(self,_value):
        """
        Insert a new node with the given value at the end of the linked list.

        Parameters
        ----------
        _value : object
            The value to be inserted into the list.

        Returns
        -------
        None

        Time complexity
        ---------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)  
        Worst : O(1)
        """
        
        new_node = Node(_value)
        
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
        self.count += 1

    def delete(self,_value):
        """ 
        Remove the first node with the specified value from the linked list.
        
        Parameters
        ----------
        _value : object
            The value of the node to be deleted.

        Returns
        -------
        None
   
        Time complexity:
        ---------------
        Best: O(1)
        Average: O(n)
        Worst: O(n)
        
        Space complexity:
        -----------------
        Best: O(1)
        Average: O(1)
        Worst: O(1)
        """

        if self._head is None:
            return
        
        if self._head.data == _value:
            self._head = self._head.next
            self.count -= 1
            return
        
        current = self._head
        while current.next is not None:
            if current.next.data == _value:
                current.next = current.next.next
                self.count -= 1
                return
            current = current.next
        raise ValueError(f"Value {_value} not found in the linked list.")
    

    def search(self,_value):
        """
          Search for a node with the specified value and return it.

        Parameters
        ----------
        _value : object
            The value to search for in the linked list.

        Returns
        -------
        Node or None
            The first node with the specified value, or None if not found.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)

        """
        current = self._head
        while current is not None:
            if current.data == _value:
                return current
            current = current.next
        return None
    
    def traverse(self):
        """
        Traverse the linked list and return a list of values.

        Returns
        -------
        list
            A list containing the values of all nodes in the linked list.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)
        """
        
        values = []
        current = self._head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values
            
    def peek(self):
        """
        Return the value of the first node without removing it.
        Returns
        -------
        object
            The value of the first node in the linked list.
        Raises
        ------
        IndexError
            If the linked list is empty.

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
        if self._head is not None:
            return self._head.data
        raise IndexError("peek from empty linked list")
        
    def is_empty(self):
        """
        Check if the linked list is empty.
        Returns
        -------
        bool
            True if the linked list is empty, False otherwise.

        Time complexity:
        ---------------
        Best: O(1)
        Average: O(1)
        Worst: O(1)

        Space complexity:
        ----------------
        Best: O(1)
        Average: O(1)
        Worst: O(1)
        
        """
        return self._head is None
    
    def size(self):
        """
        Return the number of nodes in the linked list.

        Returns
        -------
        int
            The number of nodes in the linked list.

        Time complexity:
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)

        Space complexity:
        ----------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)

        """
        return self.count
    
    def __str__(self):
        """
        Return a string representation of the linked list.

        Returns
        -------
        str
            A string representation of the linked list.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)
        
        """
        values = []
        current = self._head
        while current:
         values.append(str(current.data))
         current = current.next
        return " -> ".join(values) + " -> None"
    
    def __repr__(self):
        """
        Return a string representation of the linked list for debugging.

        Returns
        -------
        str
            A string representation of the linked list.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(n)
        Worst : O(n)
        
        """
        values = self.traverse()
        return f"LinkedList({values})"
    
#Example usage:
if __name__ == "__main__":
    l = LinkedList()
    print("Initial linked list:", l)  
    
    l.insert(11)
    l.insert(22)
    l.insert(33)
    l.insert(44)
    print("After insert:", l)  
    print("Delete 22:", l.delete(22))
    print("After delete:", l)  
    print("Search 33:", l.search(33) is not None)  
    print("Search 99:", l.search(99) is not None)  
    print("Peek first:", l.peek()) 
    print("Size of list:", l.size()) 
    print("Is list empty?", l.is_empty())
    print("All values:", l.traverse())



