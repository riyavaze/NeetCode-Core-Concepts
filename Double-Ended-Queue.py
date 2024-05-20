class ListNode:
    def __init__(self, value):
        # Initializes a node with three attributes:
        # 'value' stores the data value of the node.
        # 'next' is a pointer to the next node in the deque; initially set to None.
        # 'prev' is a pointer to the previous node in the deque; also initially None.
        # This node structure supports bidirectional traversal which is essential for a deque.
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        # Initializes the deque by creating two sentinel nodes: 'head' and 'tail'.
        # These sentinel nodes do not hold data relevant to the user but act as boundary markers.
        # 'head' always points to the first element and 'tail' to the last element.
        # Initially, 'head.next' is connected to 'tail' and 'tail.prev' to 'head', forming an empty deque.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        # Checks if the deque is empty. The deque is considered empty if there are no nodes between 'head' and 'tail'.
        # This condition is met if 'head.next' points directly to 'tail'.
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        # Adds a new node with the specified value to the end of the deque.
        # First, the method creates a new node and locates the last node ('tail.prev').
        # Then, inserts the new node between the last node and the 'tail' sentinel, adjusting the links accordingly.
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        # Adds a new node with the specified value to the front of the deque.
        # This method inserts the new node right after the 'head' sentinel.
        # The new node is placed between 'head' and 'head.next', and the links are adjusted to maintain deque integrity.
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        # Removes the last element from the deque and returns its value.
        # This method checks if the deque is empty using 'isEmpty()'.
        # If not empty, it identifies the last node ('tail.prev'), captures its value, and adjusts links to exclude it from the deque.
        if self.isEmpty():
            return -1
        target_node = self.tail.prev
        value = target_node.value
        prev_node = target_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        # Removes the first element from the deque and returns its value.
        # Similar to 'pop()', but operates at the front.
        # The method captures the value of the first node ('head.next'), adjusts the links to exclude it, and returns its value.
        if self.isEmpty():
            return -1
        target_node = self.head.next
        value = target_node.value
        next_node = target_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
