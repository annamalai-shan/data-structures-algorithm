"""
Singly Linked List Implementation in Python
This module provides a singly linked list implementation with common operations.
"""


class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        """
        Initialize a node with data.
        
        Args:
            data: Data to store in the node
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """A singly linked list implementation."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
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
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1

    def prepend(self, data):
        """
        Add a node with data to the beginning of the list.
        
        Args:
            data: Data to add
        """
        new_node = Node(data)
        new_node.next = self.head
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
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False

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
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def find_middle(self):
        """
        Find the middle node of the list.
        
        Returns:
            Data of the middle node, None if list is empty
        """
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data

    def has_cycle(self):
        """
        Detect if the list has a cycle using Floyd's algorithm.
        
        Returns:
            True if cycle exists, False otherwise
        """
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

    def to_list(self):
        """
        Convert the linked list to a Python list.
        
        Returns:
            List of data values
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        """Return string representation of the list."""
        return " -> ".join(str(data) for data in self.to_list())


# Example usage
if __name__ == "__main__":
    ll = SinglyLinkedList()
    
    # Append elements
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print(f"List after appends: {ll}")
    
    # Prepend element
    ll.prepend(5)
    print(f"List after prepend: {ll}")
    
    # Search for element
    print(f"Search for 20: {ll.search(20)}")
    print(f"Search for 100: {ll.search(100)}")
    
    # Find middle
    print(f"Middle element: {ll.find_middle()}")
    
    # Reverse list
    ll.reverse()
    print(f"List after reverse: {ll}")
    
    # Delete element
    ll.delete(20)
    print(f"List after delete 20: {ll}")
    
    # Check for cycle
    print(f"Has cycle: {ll.has_cycle()}")
