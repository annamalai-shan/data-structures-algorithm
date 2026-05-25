"""
Array Implementation in Python
This module provides a basic array implementation with common operations.
"""


class Array:
    """A simple array implementation with common operations."""

    def __init__(self, capacity=10):
        """
        Initialize an array with a given capacity.
        
        Args:
            capacity: Maximum number of elements the array can hold
        """
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity

    def __len__(self):
        """Return the current number of elements in the array."""
        return self.size

    def __getitem__(self, index):
        """
        Get element at the specified index.
        
        Args:
            index: Index of the element to retrieve
            
        Returns:
            Element at the specified index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.elements[index]

    def __setitem__(self, index, value):
        """
        Set element at the specified index.
        
        Args:
            index: Index where to set the element
            value: Value to set
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.elements[index] = value

    def append(self, value):
        """
        Add an element to the end of the array.
        
        Args:
            value: Value to append
        """
        if self.size >= self.capacity:
            self._resize()
        self.elements[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """
        Insert an element at the specified index.
        
        Args:
            index: Index where to insert the element
            value: Value to insert
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size >= self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        
        self.elements[index] = value
        self.size += 1

    def delete(self, index):
        """
        Delete element at the specified index.
        
        Args:
            index: Index of the element to delete
            
        Returns:
            The deleted element
            
        Raises:
            IndexError: If index is out of bounds
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        deleted_value = self.elements[index]
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        
        self.elements[self.size - 1] = None
        self.size -= 1
        
        return deleted_value

    def search(self, value):
        """
        Search for an element in the array.
        
        Args:
            value: Value to search for
            
        Returns:
            Index of the element if found, -1 otherwise
        """
        for i in range(self.size):
            if self.elements[i] == value:
                return i
        return -1

    def _resize(self):
        """Double the capacity of the array."""
        new_capacity = self.capacity * 2
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def __str__(self):
        """Return string representation of the array."""
        return str([self.elements[i] for i in range(self.size)])


# Example usage
if __name__ == "__main__":
    arr = Array(5)
    
    # Append elements
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(f"Array after appends: {arr}")
    
    # Access element
    print(f"Element at index 1: {arr[1]}")
    
    # Insert element
    arr.insert(1, 15)
    print(f"Array after insert: {arr}")
    
    # Search for element
    print(f"Index of 20: {arr.search(20)}")
    
    # Delete element
    deleted = arr.delete(2)
    print(f"Deleted element: {deleted}")
    print(f"Array after delete: {arr}")
