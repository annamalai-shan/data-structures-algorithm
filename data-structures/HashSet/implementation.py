"""
HashSet Implementation in Python
This module provides a simple hash set implementation with separate chaining.
"""


class HashSet:
    """A simple hash set implementation using separate chaining for collision resolution."""

    def __init__(self, capacity=16):
        """
        Initialize a hash set with given capacity.
        
        Args:
            capacity: Initial capacity of the hash set
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor = 0.75

    def __len__(self):
        """Return the number of elements in the set."""
        return self.size

    def _hash(self, item):
        """
        Compute hash value for an item.
        
        Args:
            item: Item to hash
            
        Returns:
            Hash value
        """
        return hash(item) % self.capacity

    def add(self, item):
        """
        Add an item to the set if it doesn't already exist.
        
        Args:
            item: Item to add
            
        Returns:
            True if item was added, False if it already existed
        """
        index = self._hash(item)
        bucket = self.buckets[index]
        
        # Check if item already exists
        for existing in bucket:
            if existing == item:
                return False
        
        # Add new item
        bucket.append(item)
        self.size += 1
        
        # Resize if load factor exceeded
        if self.size / self.capacity > self.load_factor:
            self._resize()
        
        return True

    def remove(self, item):
        """
        Remove an item from the set.
        
        Args:
            item: Item to remove
            
        Returns:
            True if item was removed, False if it didn't exist
        """
        index = self._hash(item)
        bucket = self.buckets[index]
        
        for i, existing in enumerate(bucket):
            if existing == item:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False

    def contains(self, item):
        """
        Check if an item exists in the set.
        
        Args:
            item: Item to check
            
        Returns:
            True if item exists, False otherwise
        """
        index = self._hash(item)
        bucket = self.buckets[index]
        
        for existing in bucket:
            if existing == item:
                return True
        
        return False

    def to_list(self):
        """
        Convert the set to a list.
        
        Returns:
            List of all elements in the set
        """
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result

    def _resize(self):
        """Resize the hash set to double its capacity."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for item in bucket:
                self.add(item)

    def __str__(self):
        """Return string representation of the hash set."""
        return "{" + ", ".join(str(item) for item in self.to_list()) + "}"

    def __iter__(self):
        """Return an iterator over the set."""
        return iter(self.to_list())


def union(set1, set2):
    """
    Return the union of two sets.
    
    Args:
        set1: First HashSet
        set2: Second HashSet
        
    Returns:
        New HashSet containing union of both sets
    """
    result = HashSet()
    for item in set1:
        result.add(item)
    for item in set2:
        result.add(item)
    return result


def intersection(set1, set2):
    """
    Return the intersection of two sets.
    
    Args:
        set1: First HashSet
        set2: Second HashSet
        
    Returns:
        New HashSet containing intersection of both sets
    """
    result = HashSet()
    for item in set1:
        if set2.contains(item):
            result.add(item)
    return result


def difference(set1, set2):
    """
    Return the difference of two sets (elements in set1 but not in set2).
    
    Args:
        set1: First HashSet
        set2: Second HashSet
        
    Returns:
        New HashSet containing difference of set1 - set2
    """
    result = HashSet()
    for item in set1:
        if not set2.contains(item):
            result.add(item)
    return result


# Example usage
if __name__ == "__main__":
    hs = HashSet()
    
    # Add elements
    hs.add(10)
    hs.add(20)
    hs.add(30)
    print(f"HashSet after adds: {hs}")
    
    # Contains check
    print(f"Contains 20: {hs.contains(20)}")
    print(f"Contains 40: {hs.contains(40)}")
    
    # Add duplicate
    added = hs.add(20)
    print(f"Add duplicate 20: {added}")
    
    # Remove element
    removed = hs.remove(20)
    print(f"Remove 20: {removed}")
    print(f"HashSet after remove: {hs}")
    
    # Size
    print(f"Size: {len(hs)}")
    
    # Convert to list
    print(f"To list: {hs.to_list()}")
    
    # Set operations
    hs1 = HashSet()
    hs1.add(1)
    hs1.add(2)
    hs1.add(3)
    
    hs2 = HashSet()
    hs2.add(2)
    hs2.add(3)
    hs2.add(4)
    
    print(f"\nSet1: {hs1}")
    print(f"Set2: {hs2}")
    print(f"Union: {union(hs1, hs2)}")
    print(f"Intersection: {intersection(hs1, hs2)}")
    print(f"Difference (Set1 - Set2): {difference(hs1, hs2)}")
