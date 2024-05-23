# Binary Search Tree Node
class TreeNode:
    def __init__(self, key: int, val: int):
        # Initialize a node with a key, value, and pointers to left and right children
        self.key = key
        self.val = val
        self.left = None
        self.right = None

# Implementation for Binary Search Tree Map
class TreeMap:
    def __init__(self):
        # Initialize the root of the TreeMap as None
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # Create a new TreeNode to insert
        newNode = TreeNode(key, val)
        if self.root == None:
            # If the tree is empty, set the new node as the root
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                # Traverse to the left child if the key is less than the current node's key
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                # Traverse to the right child if the key is greater than the current node's key
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                # If the key already exists, update the value
                current.val = val
                return

    def get(self, key: int) -> int:
        # Retrieve the value associated with the given key
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1  # Return -1 if the key is not found

    def getMin(self) -> int:
        # Get the minimum value in the tree
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            # Traverse to the leftmost node, which has the minimum key
            node = node.left
        return node

    def getMax(self) -> int:
        # Get the maximum value in the tree
        current = self.root
        while current and current.right:
            # Traverse to the rightmost node, which has the maximum key
            current = current.right
        return current.val if current else -1
    
    def remove(self, key: int) -> None:
        # Remove the node with the given key from the tree
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            # If the key to be deleted is greater than the current key, traverse to the right child
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            # If the key to be deleted is less than the current key, traverse to the left child
            curr.left = self.removeHelper(curr.left, key)
        else:
            # If the current node is the one to be deleted
            if curr.left == None:
                # Replace the current node with its right child
                return curr.right
            elif curr.right == None:
                # Replace the current node with its left child
                return curr.left
            else:
                # Replace the current node with its inorder successor (smallest node in the right subtree)
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self):
        # Get all keys in the tree in sorted order (inorder traversal)
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result) -> None:
        # Helper function for inorder traversal
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)