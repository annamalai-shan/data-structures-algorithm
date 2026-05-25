# Array

## Definition

An array is a linear data structure that stores elements in contiguous memory locations.

Since elements are stored sequentially, elements can be accessed directly using their index, providing constant-time access.

## Internal Representation

```txt
Index :  0    1    2    3
Value : [10] [20] [30] [40]
```

## Key Characteristics

- Contiguous memory allocation
- Fast indexed access
- Ordered collection
- Expensive middle insertion/deletion

## What Problem Does It Solve?

- Fast random access
- Sequential data processing
- Efficient traversal

## Use Cases

- Storing collections of similar data
- Implementing other data structures
- Matrix operations
- Buffer storage

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Access | O(1) | O(1) | O(1) |
| Lookup | O(n) | O(n) | O(n) |
| Insert | O(n) | O(n) | O(1) |
| Delete | O(n) | O(n) | O(n) |
| Update | O(1) | O(1) | O(1) |
| Traverse | O(n) | O(n) | O(n) |

## Space Complexity

- O(n)

## Common Operations

- Access element by index
- Search for an element
- Insert element at position
- Delete element at position
- Traverse all elements

## Related Algorithms

- Binary Search
- Kadane's Algorithm
- Merge Intervals

## Related Patterns

- Two Pointers
- Sliding Window
- Prefix Sum
