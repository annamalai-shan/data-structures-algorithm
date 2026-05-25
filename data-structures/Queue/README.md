# Queue

## Definition

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear (enqueue) and removed from the front (dequeue).

## Internal Representation

```txt
Circular buffer:
front -> [10] [20] [30] [40] <- rear
          ^                  ^
          dequeue            enqueue

Linked-list-based:
front -> [10] -> [20] -> [30] -> [40] <- rear
```

## Key Characteristics

- FIFO ordering
- Enqueue at rear, dequeue at front
- O(1) enqueue and dequeue with proper implementation
- Fair ordering for sequential processing
- Often used as a buffer between producers and consumers

## What Problem Does It Solve?

- Fair ordering of tasks or events
- Level-order traversal in trees and graphs
- Buffering data streams
- Scheduling work in arrival order

## Use Cases

- Task scheduling
- Print job management
- Call center systems
- BFS algorithms
- Buffer management
- Message queues

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Enqueue | O(1) | O(1) | O(1) |
| Dequeue | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) |
| isEmpty | O(1) | O(1) | O(1) |
| Size | O(1) | O(1) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Enqueue: Add element to rear
- Dequeue: Remove element from front
- Peek: View front element
- isEmpty: Check if queue is empty
- Size: Get number of elements

## Related Algorithms

- Binary Tree Level Order Traversal
- Shortest Path (unweighted BFS)
- Rotting Oranges
- Word Ladder

## Related Patterns

- BFS
- Sliding Window (with deque)
- Producer-Consumer
