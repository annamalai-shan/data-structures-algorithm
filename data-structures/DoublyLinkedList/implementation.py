"""
Doubly Linked List Implementation in Python
This module provides a doubly linked list implementation with common operations.
"""


class Node:
    """A node in a doubly linked list."""

    def __init__(self, data):
        """
        Initialize a node with data.
        
        Args:
            data: Data to store in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """A doubly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.size

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def append(self, data):
        """
        Add a node with data to the end of the list.
        
        Args:
            data: Data to add
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def prepend(self, data):
        """
        Add a node with data to the beginning of the list.
        
        Args:
            data: Data to add
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1

    def delete(self, data):
        """
        Delete the first occurrence of a node with the given data.
        
        Args:
            data: Data to delete
            
        Returns:
            True if deleted, False if not found
        """
        if self.head is None:
            return False
        
        current = self.head
        
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            
            current = current.next
        
        return False

    def delete_head(self):
        """
        Delete the head node.
        
        Returns:
            Data of the deleted node, None if list is empty
        """
        if self.head is None:
            return None
        
        data = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return data

    def delete_tail(self):
        """
        Delete the tail node.
        
        Returns:
            Data of the deleted node, None if list is empty
        """
        if self.tail is None:
            return None
        
        data = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return data

    def search(self, data):
        """
        Search for a node with the given data.
        
        Args:
            data: Data to search for
            
        Returns:
            True if found, False otherwise
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        """Reverse the linked list in place."""
        current = self.head
        
        while current:
            # Swap prev and next
            current.prev, current.next = current.next, current.prev
            current = current.prev
        
        # Swap head and tail
        self.head, self.tail = self.tail, self.head

    def to_list_forward(self):
        """
        Convert the linked list to a Python list (forward traversal).
        
        Returns:
            List of data values
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_backward(self):
        """
        Convert the linked list to a Python list (backward traversal).
        
        Returns:
            List of data values
        """
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def __str__(self):
        """Return string representation of the list."""
        return " <-> ".join(str(data) for data in self.to_list_forward())


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Append elements
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print(f"List after appends: {dll}")
    
    # Prepend element
    dll.prepend(5)
    print(f"List after prepend: {dll}")
    
    # Search for element
    print(f"Search for 20: {dll.search(20)}")
    print(f"Search for 100: {dll.search(100)}")
    
    # Delete head
    print(f"Delete head: {dll.delete_head()}")
    print(f"List after delete head: {dll}")
    
    # Delete tail
    print(f"Delete tail: {dll.delete_tail()}")
    print(f"List after delete tail: {dll}")
    
    # Reverse list
    dll.reverse()
    print(f"List after reverse: {dll}")
    
    # Backward traversal
    print(f"Backward traversal: {dll.to_list_backward()}")
