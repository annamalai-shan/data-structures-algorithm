# Data Structures Cheat Sheet (Worst Case)
A quick reference for common data structures with **worst-case time complexities** and **internal implementation details

---

## 📊 Time Complexity Table

| Data Structure            | Type       | Internal Implementation                           | Access | Search   | Insert   | Delete   | Update     |
| ------------------------- | ---------- | ------------------------------------------------- | ------ | -------- | -------- | -------- | -------- |
| **Array**                 | Linear     | [Contiguous memory](#array)                        | O(1)   | O(n)     | O(n)     | O(n)     | O(1)     |
| **String (immutable)**    | Linear     | [Array of characters](#string)                               | O(1)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Linked List**           | Linear     | [Nodes + next pointers](#linked-list)     | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Doubly Linked List**           | Linear     | [Nodes + next & previous pointers](#doubly-linked-list)                                  | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Stack**                 | Linear     | [LIFO principle](#stack)                             | —      | O(n)     | O(1)     | O(1)     | —        |
| **Queue**                 | Linear     |[FIFO principle](#queue)  | —      | O(n)     | O(1)     | O(1)     | —        |
| **Deque**                 | Linear     | [Double-ended queue](#deque)                | —      | O(n)     | O(1)     | O(1)     | —        |
| **HashMap**               | Non-linear | [Stores key–value pairs](#hashmap) | —      | O(n)     | O(n)     | O(n)     | O(n)     |
| **Set**                   | Non-linear | [Stores only unique keys](#set) | —      | O(n)     | O(n)     | O(n)     | —        | O(n)     |
| **Heap (Priority Queue)** | Non-linear | Binary Heap (array-based tree)                    | —      | O(n)     | O(log n) | O(log n) | —        |
| **Binary Tree**           | Non-linear | Node-based tree                                   | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Binary Search Tree**    | Non-linear | Ordered binary tree                               | O(n)   | O(n)     | O(n)     | O(n)     | O(n)     |
| **Trie**                  | Non-linear | Prefix tree (characters as nodes)                 | —      | O(L)     | O(L)     | O(L)     | O(L)     |
| **Graph**                | Non-linear | Adjacency List / Matrix                           | —      | O(V + E) | O(1)     | O(1)     | —        |
| **Union Find**            | Non-linear | Parent array + rank + path compression            | —      | O(log n) | O(log n) | O(log n) | —        |
| **Segment Tree**          | Non-linear | Binary tree (array-based)                         | —      | O(log n) | O(log n) | O(log n) | O(log n) |
| **Fenwick Tree**          | Non-linear | Binary Indexed Tree (array)                       | —      | O(log n) | O(log n) | O(log n) | O(log n) |

---

## 🧠 Internal Implementation

### Array
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access.


### String
- A string is internally represented as a contiguous sequence of characters with metadata like length and encoding.


### Linked List
- A linked list is internally implemented as a chain of nodes, where each node stores data plus a reference to the next node. The first node is reached through a head pointer, and the last node points to null.


### Doubly Linked List
- A doubly linked list is internally implemented as a chain of nodes where each node stores data, a pointer to the next node, and a pointer to the previous node. The first node is reached through a head pointer, and the last node’s next is null


### Stack
- A stack is a linear data structure where elements are stored in an order and accessed from one end called the top, following the LIFO (Last In, First Out) principle, meaning the last element added is the first one removed.


### Queue
- A queue is a linear data structure where elements are stored in an order and accessed from two ends called front and rear, following the FIFO (First In, First Out) principle, meaning the first element added is the first one removed.


### Deque
- A deque is a linear data structure where elements can be inserted and removed from both ends, called front and rear, allowing operations at both sides without strict ordering like stack or queue.


### HashMap
- A HashMap is a data structure that stores key–value pairs, where each key is processed using a hash function to find an index in an internal array (bucket array), allowing fast average-time access, insertion, and deletion.

### Set
- A Set is a data structure that stores unique elements only, where each element is passed through a hash function (in hash-based sets) to determine its position in an internal bucket array, allowing fast average-time operations like add, remove, and search.


### Heap
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access


### Binary Tree
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access


### Binary Search Tree
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access

### Trie
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access


### Graph
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access


### Union Find
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access


### Segment Tree
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access

### Fenwick Tree
- An array is a contiguous block of memory that stores elements of the same type, and each element can be accessed directly using its index, which gives constant-time access



