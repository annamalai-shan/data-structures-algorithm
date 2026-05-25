# Singly Linked List

## Definition

A singly linked list is a linear data structure where each node stores a value and a reference to the next node. Traversal proceeds in one direction from head to tail.

## Internal Representation

```txt
head -> [10|*] -> [20|*] -> [30|*] -> [40|null]
         data next   data next   data next   data next
```

## Key Characteristics

- Dynamic size; no fixed capacity
- Non-contiguous memory allocation per node
- O(1) insertion and deletion at the head
- O(n) access, search, and tail operations
- Extra memory per node for the next pointer
- No backward traversal without reversing

## What Problem Does It Solve?

- Efficient insertions and deletions without shifting elements
- Dynamic memory when size is unknown upfront
- Building other structures (stack, queue, adjacency lists)

## Use Cases

- Dynamic memory allocation
- Implementation of stacks and queues
- Polynomial representation
- Music playlist management

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Access | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) |
| Insertion (head) | O(1) | O(1) | O(1) |
| Insertion (tail) | O(n) | O(n) | O(n) |
| Deletion (head) | O(1) | O(1) | O(1) |
| Deletion (tail) | O(n) | O(n) | O(n) |

## Space Complexity

- O(n)

## Common Operations

- Insert at head/tail
- Delete from head/tail
- Search for element
- Reverse the list
- Detect cycles
- Find middle element

## Related Algorithms

- Reverse Linked List
- Merge Two Sorted Lists
- Linked List Cycle
- Remove Nth Node From End

## Related Patterns

- Two Pointers (slow/fast)
- Dummy Head Node
- In-place Reversal
