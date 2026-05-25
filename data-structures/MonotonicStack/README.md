# Monotonic Stack

## Definition

A monotonic stack is a stack that maintains elements in strictly increasing or decreasing order. When pushing a new element violates the order, elements are popped until the invariant is restored.

## Internal Representation

```txt
Increasing monotonic stack (bottom to top):

Push 3:  [3]
Push 1:  [3, 1]  -> pop 3 (3 > 1) -> [1]
Push 4:  [1, 4]

Each pop resolves a "next smaller/greater" relationship.
```

## Key Characteristics

- Maintains monotonic increasing or decreasing order
- Each element is pushed and popped at most once — O(n) total for a scan
- Used to find next/previous greater or smaller element efficiently
- Often stores indices instead of values for range problems
- Specialized variant of a standard stack

## What Problem Does It Solve?

- Finding next or previous greater/smaller element in O(n)
- Computing spans and bounded ranges in arrays
- Histogram and area problems with linear scans

## Use Cases

- Finding next greater/smaller elements
- Stock span problem
- Histogram area calculation
- Trapping rain water
- Expression evaluation

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Push | O(1) | O(1) | O(1) |
| Pop | O(1) | O(1) | O(1) |
| Next Greater Element | O(n) | O(n) | O(n) |
| Next Smaller Element | O(n) | O(n) | O(n) |

## Space Complexity

- O(n)

## Common Operations

- Next Greater Element
- Next Smaller Element
- Previous Greater Element
- Previous Smaller Element
- Sliding Window Maximum

## Related Algorithms

- Daily Temperatures
- Largest Rectangle in Histogram
- Trapping Rain Water
- Sum of Subarray Minimums

## Related Patterns

- Monotonic Stack
- Next Greater Element
- Contribution Technique
