class Node:
    def __init__(self, key: int, value: int):
        # Initialize a node with a key, value, and a pointer to the next node (for chaining)
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        # Initialize the hash table with a given capacity
        self.capacity = capacity
        self.size = 0  # Track the number of elements in the hash table
        self.table = [None] * self.capacity  # Create an array of None with the given capacity

    def hash_function(self, key: int) -> int:
        # Compute the hash value using modulo operation
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        # Insert a key-value pair into the hash table
        index = self.hash_function(key)  # Compute the index using the hash function
        node = self.table[index]

        # If the bucket is empty, insert the new node
        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # If the bucket is not empty, traverse the linked list to find the key or append a new node
            prev = None
            while node:
                if node.key == key:
                    # If the key already exists, update its value
                    node.value = value
                    return
                prev, node = node, node.next
            # Append the new node to the end of the list
            prev.next = Node(key, value)
            self.size += 1

        # Check if resizing is needed (load factor >= 0.5)
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        # Retrieve the value associated with the given key
        index = self.hash_function(key)  # Compute the index using the hash function
        node = self.table[index]

        # Traverse the linked list to find the key
        while node:
            if node.key == key:
                return node.value  # Return the value if the key is found
            node = node.next

        return -1  # Return -1 if the key is not found

    def remove(self, key: int) -> bool:
        # Remove the node with the given key from the hash table
        index = self.hash_function(key)  # Compute the index using the hash function
        node = self.table[index]
        prev = None

        # Traverse the linked list to find the key
        while node:
            if node.key == key:
                # If the key is found, remove the node
                if prev:
                    prev.next = node.next  # Remove the node by linking the previous node to the next node
                else:
                    self.table[index] = node.next  # Remove the node by updating the head of the list
                self.size -= 1
                return True
            prev, node = node, node.next

        return False  # Return False if the key is not found

    def getSize(self) -> int:
        # Return the number of elements in the hash table
        return self.size

    def getCapacity(self) -> int:
        # Return the current capacity of the hash table
        return self.capacity

    def resize(self) -> None:
        # Resize the hash table when the load factor exceeds the threshold
        new_capacity = self.capacity * 2  # Double the capacity
        new_table = [None] * new_capacity  # Create a new table with the new capacity

        # Rehash all the nodes and insert them into the new table
        for node in self.table:
            while node:
                index = node.key % new_capacity  # Compute the new index using the new capacity
                if new_table[index] is None:
                    new_table[index] = Node(node.key, node.value)  # Insert the node into the new table
                else:
                    new_node = new_table[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)  # Append the node to the end of the list in the new table
                node = node.next

        self.capacity = new_capacity  # Update the capacity
        self.table = new_table  # Update the table reference to the new table