class ListNode:
    def __init__(self, val, next_node=None):
        # Node initialization
        # 'val' stores the value of the node.
        # 'next_node' is a reference to the next node in the list, defaults to None.
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        # Initialize the linked list with a dummy head node.
        # 'head' is a dummy node, which simplifies edge cases in list manipulation.
        # 'tail' points to the last node in the list starting with the dummy head.
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        # Returns the value at the specified index in the linked list.
        # Start with the first real node (self.head.next).
        # 'i' tracks the current index as we traverse.
        current_node = self.head.next
        i = 0
        while current_node:  # Continue until the end of the list
            if i == index:
                return current_node.val  # Return the value at the index
            i += 1
            current_node = current_node.next
        return -1  # If index is out of bounds, return -1

    def insertHead(self, val: int) -> None:
        # Insert a new node with value 'val' at the head of the list.
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        # If the list was empty, set the tail to the new node.
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # Insert a new node with value 'val' at the tail of the list.
        self.tail.next = ListNode(val)
        self.tail = self.tail.next  # Update the tail reference

    def remove(self, index: int) -> bool:
        # Remove the node at the specified index.
        i = 0
        current_node = self.head  # Start from dummy head

        # Traverse the list to find the node right before the one to remove.
        while i < index and current_node:
            i += 1
            current_node = current_node.next

        # Check if the node to remove exists.
        if current_node and current_node.next:
            # If removing the tail, update the tail pointer.
            if current_node.next == self.tail:
                self.tail = current_node
            # Bypass the node to be removed.
            current_node.next = current_node.next.next
            return True
        return False
        
    def getValues(self) -> list:
        # Return a list of all values in the linked list.
        current_node = self.head.next
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return result
