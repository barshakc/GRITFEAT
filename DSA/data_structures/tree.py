"""
TREE DATA STRUCTURE
..........................
A tree is a hierarchical data structure consisting of nodes.
Each tree has a root node and each node can have zero or more child nodes.

This implementation provides a Binary Tree, where each node has at most two children (left and right).

Operations:
1. Insert: Add a new node to the tree.
2. Search: Find a node in the tree.
3. Pre-order Traversal: Visit the root, then left subtree, then right subtree.
4. In-order Traversal: Visit the left subtree, then root, then right subtree.
5. Post-order Traversal: Visit the left subtree, then right subtree, then root.
6. Check if empty: Determine if the tree has no nodes.

Properties:
- Each node contains a value and references to its children.
- The root node is the topmost node in the tree.

Pros:
- Hierarchical structure allows for efficient searching and sorting.
- Easy to search, traverse, and modify relationships.

Cons:
- More complex than linear data structures like arrays or linked lists.
- Requires more memory due to pointers/references.

When to use a tree:
- When representing hierarchical data.
- When performing fast searches, insertions, and deletions.
- When implementing algorithms like binary search trees, heaps, or tries.

When not to use a tree:
- When data is flat or linear.
- When we need to frequently access elements in a non-hierarchical manner.

Keyword arguments:
argument -- description
Return: return_description
"""

class TreeNode:
    """
    A node in a binary tree.

    Parameters
    ----------
    value : object
        The value to store in the node.
    left : TreeNode, optional
        Reference to the left child node (default is None).
    right : TreeNode, optional
        Reference to the right child node (default is None).

    Attributes
    ----------
    value : object
        The value stored in the node.
    left : TreeNode or None
        Reference to the left child node.
    right : TreeNode or None
        Reference to the right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Binary tree implementation.

    Methods
    -------
    insert(value)
        Insert a value into the binary tree (level order).
    search(value)
        Check if a value exists in the tree.
    inorder()
        Return a list of values from an inorder traversal.
    preorder()
        Return a list of values from a preorder traversal.
    postorder()
        Return a list of values from a postorder traversal.
    is_empty()
        Check if the tree is empty.

    Parameters
    ----------
    None

    Attributes
    ----------
    root : TreeNode or None
        Reference to the root node of the tree.
    """

    def __init__(self):
        """Initialize an empty binary tree.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.root = None

    def is_empty(self):
        """
        Check if the tree is empty.

        Returns
        -------
        bool
            True if the tree is empty, False otherwise.
        
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
        return self.root is None

    def insert(self, value):
        """
        Insert a value into the binary tree.

        Parameters
        ----------
        value : object
            The value to insert.

        Time complexity
        ---------------
        Best : O(1)
        Average : O(log n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(1)
        Average : O(log n)
        Worst : O(n)

        """
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def search(self, value):
        """
        Check if a value exists in the tree.

        Parameters
        ----------
        value : object
            The value to search for.

        Returns
        -------
        bool
            True if value is found, False otherwise.

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
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def inorder(self):
        """
        Return a list of values from an inorder traversal.

        Returns
        -------
        list
            List of values in inorder: Left, Root, Right.

        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(h)
        Average : O(h)
        Worst : O(h)

        """
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)

    def preorder(self):
        """
        Return a list of values from a preorder traversal.

        Returns
        -------
        list
            List of values in preorder: Root, Left, Right.

        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(h)
        Average : O(h)
        Worst : O(h)

        """
        def _preorder(node):
            return [node.value] + _preorder(node.left) + _preorder(node.right) if node else []
        return _preorder(self.root)

    def postorder(self):
        """
        Return a list of values from a postorder traversal.

        Returns
        -------
        list
            List of values in postorde: Left, Right, Root.

        Time complexity
        ---------------
        Best : O(n)
        Average : O(n)
        Worst : O(n)

        Space complexity
        ----------------
        Best : O(h)
        Average : O(h)
        Worst : O(h)

        """
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.value] if node else []
        return _postorder(self.root)

    def __str__(self):
        """
        Return a string representation of the tree (inorder).

        Returns
        -------
        str
            String representation of the tree.

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
        return "Inorder: " + str(self.inorder())

    def __repr__(self):
        """
        Return a detailed string representation of the tree.

        Returns
        -------
        str
            Detailed string representation of the tree.

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
        return f"BinaryTree(root={self.root})"

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    print("Initial tree:", tree)
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(60)
    print("Tree after insertion:", tree)

    print("Inorder:", tree.inorder())
    print("Preorder:", tree.preorder())
    print("Postorder:", tree.postorder())

    print("Search 30:", tree.search(30))  
    print("Search 99:", tree.search(99))  
    
    print("Is tree empty?", tree.is_empty())