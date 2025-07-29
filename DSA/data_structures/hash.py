"""
HASH TABLE DATA STRUCTURE
..........................
A hash table is a data structure that implements a structure that can map keys to values.
It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

This implementation provides a simple hash table using separate chaining for collision resolution.

Operations:
1. Insert: Add a key-value pair to the hash table.
2. Search: Retrieve the value associated with a given key.
3. Delete: Remove a key-value pair from the hash table.
4. Check if empty: Determine if the hash table has no entries.

Properties:
- Each entry contains a key and a value.
- Collisions are handled using separate chaining (linked lists).

Pros:
- Provides average-case constant time complexity for insert, search, and delete.
- Efficient for large datasets with unique keys.

Cons:
- Performance degrades if many collisions occur.
- Requires a good hash function for uniform distribution.

When to use a hash table:
- When you need fast lookups, insertions, and deletions by key.
- When keys are unique and hashable.

When not to use a hash table:
- When order of elements matters.
- When keys are not hashable or are mutable.

Keyword arguments:
argument -- description
Return: return_description
"""

class HashNode:
    """
    Node for separate chaining in hash table.

    Parameters
    ----------
    key : object
        The key for the entry.
    value : object
        The value associated with the key.
    next : HashNode, optional
        Reference to the next node in the chain (default is None).

    Attributes
    ----------
    key : object
        The key stored in the node.
    value : object
        The value stored in the node.
    next : HashNode or None
        Reference to the next node in the chain.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    Hash table implementation using separate chaining.

    Methods
    -------
    insert(key, value)
        Insert a key-value pair into the hash table.
    search(key)
        Retrieve the value associated with a key.
    delete(key)
        Remove a key-value pair from the hash table.
    is_empty()
        Check if the hash table is empty.

    Parameters
    ----------
    capacity : int, optional
        Number of buckets in the hash table (default is 10).

    Attributes
    ----------
    _buckets : list
        List of bucket heads (linked lists).
    _capacity : int
        Number of buckets in the hash table.
    _size : int
        Number of key-value pairs in the hash table.
    """

    def __init__(self, capacity=10):
        """Initialize an empty hash table.

        Time complexity: O(1)
        Space complexity: O(n)
        """
        self._capacity = capacity
        self._buckets = [None] * capacity
        self._size = 0

    def _hash(self, key):
        """
        Compute the hash index for a given key.

        Parameters
        ----------
        key : object
            The key to hash.

        Returns
        -------
        int
            Index in the buckets array.
        """
        return hash(key) % self._capacity

    def is_empty(self):
        """
        Check if the hash table is empty.

        Returns
        -------
        bool
            True if the hash table is empty, False otherwise.

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
        return self._size == 0

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.

        Parameters
        ----------
        key : object
            The key to insert.
        value : object
            The value to associate with the key.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(n) 

        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        """
        index = self._hash(key)
        head = self._buckets[index]
        current = head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = HashNode(key, value)
        new_node.next = head
        self._buckets[index] = new_node
        self._size += 1

    def search(self, key):
        """
        Retrieve the value associated with a key.

        Parameters
        ----------
        key : object
            The key to search for.

        Returns
        -------
        object or None
            The value associated with the key, or None if not found.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(n) 

        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        """
        index = self._hash(key)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        """
        Remove a key-value pair from the hash table.

        Parameters
        ----------
        key : object
            The key to delete.

        Returns
        -------
        bool
            True if the key was found and deleted, False otherwise.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(1)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(1)
        Worst : O(1)
        """
        index = self._hash(key)
        current = self._buckets[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self._buckets[index] = current.next
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False
   

# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    print("Initial hash table:", ht)
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    print("Hash table after insertion:", ht)

    print("Search 'banana':", ht.search("banana"))
    print("Search 'grape':", ht.search("grape"))

    print("Delete 'banana':", ht.delete("banana"))
    print("Hash table after deletion:", ht)

    print("Is hash table empty?", ht.is_empty())