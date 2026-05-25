# HashSet

## Definition

A hash set is a collection that stores unique elements with no duplicates. It implements the mathematical set abstract data type using a hash function to map each element to a bucket index, enabling near-constant-time membership testing on average.

## Internal Representation

```txt
Buckets :  [0]      [1]      [2]      [3]
            |        |        |        |
            v        v        v        v
           null    [42]     null    [17] -> [91]
                              (chaining)
```

## Key Characteristics

- Stores only unique elements
- Hash function maps elements to bucket indices
- Average O(1) insert, delete, and lookup
- No inherent ordering of elements
- Worst-case O(n) when many collisions occur
- Load factor triggers rehashing as the set grows

## What Problem Does It Solve?

- Fast uniqueness checking
- Removing duplicates from data
- Set membership and set algebra operations
- Tracking seen elements during traversal

## Use Cases

- Removing duplicates
- Membership testing
- Set operations
- Caching unique values
- Frequency counting

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Insert | O(1) | O(n) | O(1) |
| Delete | O(1) | O(n) | O(1) |
| Search | O(1) | O(n) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Add: Insert element if not present
- Remove: Delete element
- Contains: Check if element exists
- Size: Get number of elements
- Union: Combine two sets
- Intersection: Find common elements
- Difference: Find elements in one set but not the other

## Related Algorithms

- Two Sum
- Contains Duplicate
- Longest Consecutive Sequence
- Valid Sudoku

## Related Patterns

- Hash Table
- Frequency Counting
- Set Membership
