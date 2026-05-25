"""
Queue Implementation in Python
This module provides a queue implementation with common operations.
"""


class Queue:
    """A queue implementation using a list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self.items)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: Item to enqueue
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove an item from the front of the queue.
        
        Returns:
            The dequeued item
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        """
        Peek at the front item without removing it.
        
        Returns:
            The front item
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def size(self):
        """
        Return the size of the queue.
        
        Returns:
            Number of elements in the queue
        """
        return len(self.items)

    def __str__(self):
        """Return string representation of the queue."""
        return str(self.items)


class CircularQueue:
    """A circular queue implementation using a fixed-size array."""

    def __init__(self, capacity):
        """
        Initialize a circular queue with given capacity.
        
        Args:
            capacity: Maximum number of elements
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: Item to enqueue
            
        Raises:
            IndexError: If queue is full
        """
        if self.is_full():
            raise IndexError("Queue is full")
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1

    def dequeue(self):
        """
        Remove an item from the front of the queue.
        
        Returns:
            The dequeued item
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """
        Peek at the front item without removing it.
        
        Returns:
            The front item
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]

    def __str__(self):
        """Return string representation of the queue."""
        if self.is_empty():
            return "[]"
        
        result = []
        index = self.front
        for _ in range(self.size):
            result.append(str(self.items[index]))
            index = (index + 1) % self.capacity
        
        return "[" + ", ".join(result) + "]"


# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"Queue after enqueues: {queue}")
    
    # Peek
    print(f"Front element: {queue.peek()}")
    
    # Dequeue elements
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue after dequeue: {queue}")
    
    # Size
    print(f"Queue size: {queue.size()}")
    
    # Circular queue
    print("\nCircular Queue:")
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(f"Circular queue: {cq}")
    print(f"Is full: {cq.is_full()}")
    print(f"Dequeued: {cq.dequeue()}")
    cq.enqueue(4)
    print(f"After enqueue 4: {cq}")
