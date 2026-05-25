# Doubly Linked List

## Definition

A doubly linked list is a linear data structure where each node stores a value, a reference to the next node, and a reference to the previous node. Traversal can proceed in both directions.

## Internal Representation

```txt
null <- [10] <-> [20] <-> [30] <-> [40] -> null
         prev next  prev next  prev next  prev next
head --------------------------------^
tail ----------------------------------------^
```

## Key Characteristics

- Bidirectional traversal from head or tail
- O(1) insertion and deletion at both ends (with tail pointer)
- Two pointers per node increase memory overhead
- O(n) random access by index
- Easier deletion of a known node than in a singly linked list
- Common building block for LRU cache and deque implementations

## What Problem Does It Solve?

- Efficient removal of nodes when a pointer to the node is known
- Forward and backward navigation without re-scanning
- Implementing structures that need O(1) operations at both ends

## Use Cases

- Browser history navigation
- Text editor undo/redo
- Music playlist with previous/next
- Cache implementations

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Access | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) |
| Insertion (head) | O(1) | O(1) | O(1) |
| Insertion (tail) | O(1) | O(1) | O(1) |
| Deletion (head) | O(1) | O(1) | O(1) |
| Deletion (tail) | O(1) | O(1) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Insert at head/tail
- Delete from head/tail
- Search for element
- Reverse the list
- Traverse forward/backward
- Detect cycles

## Related Algorithms

- LRU Cache
- Design Browser History
- Flatten a Multilevel Doubly Linked List

## Related Patterns

- Two Pointers
- Dummy Head Node
- Cache Eviction (LRU)
