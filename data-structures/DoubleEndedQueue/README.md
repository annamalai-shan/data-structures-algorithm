# Double Ended Queue (Deque)

## Definition

A double-ended queue (deque) is a linear data structure that allows insertion and deletion at both the front and the rear. It generalizes both stacks and queues.

## Internal Representation

```txt
Doubly linked list deque:
null <- [10] <-> [20] <-> [30] -> null
front ----------------^      rear --^

Circular array deque:
       front
         v
       [30][40][10][20]
         ^           ^
        rear       (wraps around)
```

## Key Characteristics

- Insert and remove at both front and rear in O(1)
- Combines LIFO and FIFO capabilities
- Often implemented with doubly linked list or circular buffer
- Useful for sliding-window and palindrome problems
- More flexible than a standard queue or stack alone

## What Problem Does It Solve?

- O(1) access to both ends of a sequence
- Maintaining a window of elements with efficient updates
- Implementing stack and queue behavior in one structure

## Use Cases

- Implementing stacks and queues
- Palindrome checking
- Sliding window problems
- Undo/redo operations
- Task scheduling with priorities

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Add front | O(1) | O(1) | O(1) |
| Add rear | O(1) | O(1) | O(1) |
| Remove front | O(1) | O(1) | O(1) |
| Remove rear | O(1) | O(1) | O(1) |
| Peek front | O(1) | O(1) | O(1) |
| Peek rear | O(1) | O(1) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Add front: Add element to front
- Add rear: Add element to rear
- Remove front: Remove element from front
- Remove rear: Remove element from rear
- Peek front: View front element
- Peek rear: View rear element

## Related Algorithms

- Sliding Window Maximum
- Palindrome Linked List
- Shortest Subarray with Sum at Least K

## Related Patterns

- Sliding Window
- Monotonic Deque
- BFS (0-1 BFS with deque)
