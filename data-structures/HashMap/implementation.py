"""
HashMap Implementation in Python
This module provides a simple hash map implementation with separate chaining.
"""


class HashMap:
    """A simple hash map implementation using separate chaining for collision resolution."""

    def __init__(self, capacity=16):
        """
        Initialize a hash map with given capacity.
        
        Args:
            capacity: Initial capacity of the hash map
        """
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.load_factor = 0.75

    def __len__(self):
        """Return the number of key-value pairs in the map."""
        return self.size

    def _hash(self, key):
        """
        Compute hash value for a key.
        
        Args:
            key: Key to hash
            
        Returns:
            Hash value
        """
        return hash(key) % self.capacity

    def put(self, key, value):
        """
        Insert or update a key-value pair.
        
        Args:
            key: Key to insert/update
            value: Value to associate with the key
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor exceeded
        if self.size / self.capacity > self.load_factor:
            self._resize()

    def get(self, key):
        """
        Get the value associated with a key.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with the key
            
        Raises:
            KeyError: If key is not found
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        """
        Remove a key-value pair from the map.
        
        Args:
            key: Key to remove
            
        Returns:
            The removed value
            
        Raises:
            KeyError: If key is not found
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return v
        
        raise KeyError(f"Key '{key}' not found")

    def contains_key(self, key):
        """
        Check if a key exists in the map.
        
        Args:
            key: Key to check
            
        Returns:
            True if key exists, False otherwise
        """
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def keys(self):
        """
        Get all keys in the map.
        
        Returns:
            List of all keys
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)
        return result

    def values(self):
        """
        Get all values in the map.
        
        Returns:
            List of all values
        """
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(v)
        return result

    def items(self):
        """
        Get all key-value pairs in the map.
        
        Returns:
            List of (key, value) tuples
        """
        result = []
        for bucket in self.buckets:
            result.extend(bucket)
        return result

    def _resize(self):
        """Resize the hash map to double its capacity."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def __str__(self):
        """Return string representation of the hash map."""
        pairs = [f"{k}: {v}" for k, v in self.items()]
        return "{" + ", ".join(pairs) + "}"


# Example usage
if __name__ == "__main__":
    hm = HashMap()
    
    # Put key-value pairs
    hm.put("name", "John")
    hm.put("age", 30)
    hm.put("city", "New York")
    print(f"HashMap after puts: {hm}")
    
    # Get value
    print(f"Get 'name': {hm.get('name')}")
    
    # Update value
    hm.put("age", 31)
    print(f"HashMap after update: {hm}")
    
    # Contains key
    print(f"Contains 'city': {hm.contains_key('city')}")
    print(f"Contains 'country': {hm.contains_key('country')}")
    
    # Get all keys and values
    print(f"Keys: {hm.keys()}")
    print(f"Values: {hm.values()}")
    
    # Remove key
    removed = hm.remove("city")
    print(f"Removed value: {removed}")
    print(f"HashMap after remove: {hm}")
    
    # Size
    print(f"Size: {len(hm)}")
