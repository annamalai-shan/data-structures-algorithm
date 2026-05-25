# Stack

## Definition

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. Elements are added and removed only from the top end of the stack.

## Internal Representation

```txt
Array-based:
Index :  0    1    2    3
Value : [10] [20] [30] [40]  <- top

Linked-list-based:
head -> [40] -> [30] -> [20] -> [10] -> null
         top
```

## Key Characteristics

- LIFO ordering
- Push and pop occur at the same end (top)
- O(1) push, pop, and peek with array or linked list
- No random access to middle elements
- Natural fit for nested and recursive processing

## What Problem Does It Solve?

- Reversing order of processing
- Tracking nested state (calls, brackets, scopes)
- Backtracking and depth-first exploration
- Evaluating expressions with operator precedence

## Use Cases

- Function call stack
- Undo/redo operations
- Expression evaluation
- Backtracking algorithms
- Browser history
- Parentheses matching

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Push | O(1) | O(1) | O(1) |
| Pop | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) |
| isEmpty | O(1) | O(1) | O(1) |
| Size | O(1) | O(1) | O(1) |

## Space Complexity

- O(n)

## Common Operations

- Push: Add element to top
- Pop: Remove element from top
- Peek: View top element
- isEmpty: Check if stack is empty
- Size: Get number of elements

## Related Algorithms

- Valid Parentheses
- Daily Temperatures
- Largest Rectangle in Histogram
- Evaluate Reverse Polish Notation

## Related Patterns

- Monotonic Stack
- DFS (iterative)
- Backtracking
