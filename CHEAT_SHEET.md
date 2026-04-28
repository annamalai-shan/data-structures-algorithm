# Data Structures Cheat Sheet (Worst Case)

A quick reference for common data structures with **worst-case time complexities** and **internal implementation details**.

---

## 📊 Time Complexity Table

| Data Structure            | Type       | Internal Implementation                           | Access | Search   | Insert   | Delete   | Update   | Space    |
| ------------------------- | ---------- | ------------------------------------------------- | ------ | -------- | -------- | -------- | -------- | -------- |
| **Array**                 | Linear     | Contiguous memory                                 | O(1)   | O(n)     | O(n)     | O(n)     | O(1)     | O(n)     |
| **String (immutable)**    | Linear     | Array of characters                               | O(1)   | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| **Linked List**           | Linear     | Nodes + pointers                                  | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| **Stack**                 | Linear     | Array / Linked List                               | —      | O(n)     | O(1)     | O(1)     | —        | O(n)     |
| **Queue**                 | Linear     | Linked List / Circular Array                      | —      | O(n)     | O(1)     | O(1)     | —        | O(n)     |
| **Deque**                 | Linear     | Doubly Linked List / Circular Array               | —      | O(n)     | O(1)     | O(1)     | —        | O(n)     |
| **HashMap**               | Non-linear | Hash Table (Array + hashing + collision handling) | —      | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| **Set**                   | Non-linear | Hash Table (keys only)                            | —      | O(n)     | O(n)     | O(n)     | —        | O(n)     |
| **Heap (Priority Queue)** | Non-linear | Binary Heap (array-based tree)                    | —      | O(n)     | O(log n) | O(log n) | —        | O(n)     |
| **Binary Tree**           | Non-linear | Node-based tree                                   | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| **Binary Search Tree**    | Non-linear | Ordered binary tree                               | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     | O(n)     |
| **Trie**                  | Non-linear | Prefix tree (characters as nodes)                 | —      | O(L)     | O(L)     | O(L)     | O(L)     | O(N × L) |
| **Graph***                | Non-linear | Adjacency List / Matrix                           | —      | O(V + E) | O(1)     | O(1)     | —        | O(V + E) |
| **Union Find**            | Non-linear | Parent array + rank + path compression            | —      | O(log n) | O(log n) | O(log n) | —        | O(n)     |
| **Segment Tree**          | Non-linear | Binary tree (array-based)                         | —      | O(log n) | O(log n) | O(log n) | O(log n) | O(n)     |
| **Fenwick Tree**          | Non-linear | Binary Indexed Tree (array)                       | —      | O(log n) | O(log n) | O(log n) | O(log n) | O(n)     |

---

## 🧠 Notes

* **Worst-case complexities only**
* **HashMap / Set**

  * Avg: O(1), Worst: O(n)
* **BST**

  * Avg: O(log n), Worst: O(n)
* **Trie**

  * N = number of words, L = word length → Space = O(N × L)
* **Graph**

  * Adjacency List → O(V + E)
  * Adjacency Matrix → O(V²)
* **String**

  * Immutable → update creates new string → O(n)

---


