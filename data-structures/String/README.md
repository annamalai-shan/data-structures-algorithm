# String

## Definition

A string is a linear data structure that stores a sequence of characters.

Strings are commonly used for:

- text processing
- pattern matching
- parsing
- searching

## Internal Representation

```txt
Index :  0    1    2    3    4
Value : [H]  [E]  [L]  [L]  [O]
```

## Key Characteristics

- Sequence of characters
- Indexed access
- Usually immutable in many languages
- Supports traversal and substring operations
- Frequently used in text manipulation

## What Problem Does It Solve?

- Text storage
- String searching
- Pattern matching
- Parsing and tokenization
- Data serialization

## Use Cases

- Text processing
- Pattern matching
- Data validation
- Text formatting

## Time Complexity Table

| Operation | Average Case | Worst Case | Amortized Case |
| :-------- | :----------: | :--------: | -------------: |
| Access | O(1) | O(1) | O(1) |
| Lookup | O(n) | O(n) | O(n) |
| Insert | O(n) | O(n) | O(n) |
| Delete | O(n) | O(n) | O(n) |
| Update | O(n) | O(n) | O(n) |
| Traverse | O(n) | O(n) | O(n) |

## Space Complexity

- O(n)

## Common Operations

- String reversal
- Palindrome check
- Substring search
- Character frequency
- String manipulation

## Related Algorithms

- Knuth-Morris-Pratt Algorithm
- Rabin-Karp Algorithm
- Z Algorithm
- Manacher's Algorithm

## Related Patterns

- Sliding Window
- Two Pointers
- Prefix Sum
- Fast and Slow Pointer
