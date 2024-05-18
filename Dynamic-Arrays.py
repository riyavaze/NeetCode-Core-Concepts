class DynamicArray:
    def __init__(self, capacity: int):
        # Initialize a dynamic array with a specific capacity.
        # 'capacity' is the maximum number of elements the array can hold before needing to resize.
        # 'length' keeps track of the number of elements currently in the array.
        # 'arr' is the list that stores the elements of the dynamic array.
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        # Retrieve the element at index 'i' from the array.
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Set the element at index 'i' to 'n'.
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # Add a new element 'n' to the end of the dynamic array.
        # If the array is full (length equals capacity), resize the array before adding the new element.
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        # Remove the last element from the dynamic array and return its value.
        # If the array is not empty, decrease the length by one.
        if self.length > 0:
            self.length -= 1
        
        return self.arr[self.length]
 
    def resize(self) -> None:
        # Double the capacity of the array when it's full.
        # Create a new array 'new_arr' with double the capacity, and copy the elements from the old array to the new one.
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def getSize(self) -> int:
        # Return the current number of elements in the dynamic array.
        return self.length
    
    def getCapacity(self) -> int:
        # Return the current capacity of the dynamic array.
        return self.capacity
