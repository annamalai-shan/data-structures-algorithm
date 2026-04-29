# Data Structures Cheat Sheet (Worst Case)

A quick reference for common data structures with **worst-case time complexities** and **internal implementation details**.

---

## 📊 Time Complexity Table

| Data Structure            | Type       | Internal Implementation                           | Access | Search   | Insert   | Delete   | Update     |
| ------------------------- | ---------- | ------------------------------------------------- | ------ | -------- | -------- | -------- | -------- |
| **Array**                 | Linear     | Contiguous memory                                 | O(1)   | O(n)     | O(n)     | O(n)     | O(1)     |
| **String (immutable)**    | Linear     | Array of characters                               | O(1)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Linked List**           | Linear     | Nodes + pointers                                  | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Stack**                 | Linear     | Array / Linked List                               | —      | O(n)     | O(1)     | O(1)     | —        |
| **Queue**                 | Linear     | Linked List / Circular Array                      | —      | O(n)     | O(1)     | O(1)     | —        |
| **Deque**                 | Linear     | Doubly Linked List / Circular Array               | —      | O(n)     | O(1)     | O(1)     | —        |
| **HashMap**               | Non-linear | Hash Table (Array + hashing + collision handling) | —      | O(n)     | O(n)     | O(n)     | O(n)     |
| **Set**                   | Non-linear | Hash Table (keys only)                            | —      | O(n)     | O(n)     | O(n)     | —        | O(n)     |
| **Heap (Priority Queue)** | Non-linear | Binary Heap (array-based tree)                    | —      | O(n)     | O(log n) | O(log n) | —        |
| **Binary Tree**           | Non-linear | Node-based tree                                   | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Binary Search Tree**    | Non-linear | Ordered binary tree                               | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Trie**                  | Non-linear | Prefix tree (characters as nodes)                 | —      | O(L)     | O(L)     | O(L)     | O(L)     |
| **Graph***                | Non-linear | Adjacency List / Matrix                           | —      | O(V + E) | O(1)     | O(1)     | —        |
| **Union Find**            | Non-linear | Parent array + rank + path compression            | —      | O(log n) | O(log n) | O(log n) | —        |
| **Segment Tree**          | Non-linear | Binary tree (array-based)                         | —      | O(log n) | O(log n) | O(log n) | O(log n) |
| **Fenwick Tree**          | Non-linear | Binary Indexed Tree (array)                       | —      | O(log n) | O(log n) | O(log n) | O(log n) |

---
