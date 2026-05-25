"""
Double Ended Queue (Deque) Implementation in Python
This module provides a deque implementation with common operations.
"""


class Deque:
    """A deque implementation using a list."""

    def __init__(self):
        """Initialize an empty deque."""
        self.items = []

    def __len__(self):
        """Return the number of elements in the deque."""
        return len(self.items)

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0

    def add_front(self, item):
        """
        Add an item to the front of the deque.
        
        Args:
            item: Item to add
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Add an item to the rear of the deque.
        
        Args:
            item: Item to add
        """
        self.items.append(item)

    def remove_front(self):
        """
        Remove an item from the front of the deque.
        
        Returns:
            The removed item
            
        Raises:
            IndexError: If deque is empty
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop(0)

    def remove_rear(self):
        """
        Remove an item from the rear of the deque.
        
        Returns:
            The removed item
            
        Raises:
            IndexError: If deque is empty
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items.pop()

    def peek_front(self):
        """
        Peek at the front item without removing it.
        
        Returns:
            The front item
            
        Raises:
            IndexError: If deque is empty
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[0]

    def peek_rear(self):
        """
        Peek at the rear item without removing it.
        
        Returns:
            The rear item
            
        Raises:
            IndexError: If deque is empty
        """
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.items[-1]

    def size(self):
        """
        Return the size of the deque.
        
        Returns:
            Number of elements in the deque
        """
        return len(self.items)

    def __str__(self):
        """Return string representation of the deque."""
        return str(self.items)


def is_palindrome(s):
    """
    Check if a string is a palindrome using a deque.
    
    Args:
        s: String to check
        
    Returns:
        True if palindrome, False otherwise
    """
    deque = Deque()
    
    for char in s.lower():
        if char.isalnum():
            deque.add_rear(char)
    
    while len(deque) > 1:
        if deque.remove_front() != deque.remove_rear():
            return False
    
    return True


def sliding_window_maximum(nums, k):
    """
    Find the maximum in each sliding window of size k using a deque.
    
    Args:
        nums: List of numbers
        k: Window size
        
    Returns:
        List of maximum values in each window
    """
    from collections import deque as collections_deque
    
    result = []
    dq = collections_deque()
    
    for i in range(len(nums)):
        # Remove elements outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from the rear
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# Example usage
if __name__ == "__main__":
    deque = Deque()
    
    # Add elements
    deque.add_rear(10)
    deque.add_rear(20)
    deque.add_front(5)
    print(f"Deque after adds: {deque}")
    
    # Peek
    print(f"Front: {deque.peek_front()}")
    print(f"Rear: {deque.peek_rear()}")
    
    # Remove elements
    print(f"Remove front: {deque.remove_front()}")
    print(f"Remove rear: {deque.remove_rear()}")
    print(f"Deque after removes: {deque}")
    
    # Palindrome check
    print(f"\nIs 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")
    
    # Sliding window maximum
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"\nSliding window maximum: {sliding_window_maximum(nums, k)}")
