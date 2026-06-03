class Array:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.elements[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.elements[index] = value

    def append(self, value):
        if self.size >= self.capacity:
            self._resize()
        self.elements[self.size] = value
        self.size += 1

    def insert(self, index, value):
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
        for i in range(self.size):
            if self.elements[i] == value:
                return i
        return -1

    def _resize(self):
        new_capacity = self.capacity * 2
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def __str__(self):
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
