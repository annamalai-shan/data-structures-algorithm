# HashMap

## Definition

A hash map (hash table) is an associative array that maps keys to values. It uses a hash function to compute a bucket index for each key, enabling efficient key-value storage and retrieval on average.

## Internal Representation

```txt
Keys    :  "name"   "age"    "city"
            |        |        |
Hash    :   h1       h2       h3
            v        v        v
Buckets :  [0]      [1]      [2]
            |        |        |
           null   (k,v)    (k,v) -> (k,v)
```

## Key Characteristics

- Key-value pair storage
- Hash function distributes keys across buckets
- Average O(1) get, put, and remove
- Keys are unique; values may repeat
- Collision resolution via chaining or open addressing
- Dynamic resizing when load factor exceeds a threshold

## What Problem Does It Solve?

- Fast key-based lookup and updates
- Counting and grouping by key
- Caching computed results
- Building indexes over data

## Use Cases

- Caching
- Indexing
- Frequency counting
- Symbol tables
- Database indexing

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Insert | O(1) | O(n) | O(1) |
| Delete | O(1) | O(n) | O(1) |
| Search | O(1) | O(n) | O(1) |
| Access | O(1) | O(n) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Put: Add or update key-value pair
- Get: Retrieve value by key
- Remove: Delete key-value pair
- Contains: Check if key exists
- Keys/Values: Get all keys or values

## Related Algorithms

- Two Sum
- Group Anagrams
- Subarray Sum Equals K
- LRU Cache

## Related Patterns

- Hash Table
- Frequency Counting
- Prefix Sum with Hash Map
