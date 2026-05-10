# Lab 2: Selection Sort

## Student Information
- **Name:** Uziel Beltran
- **Date:** 02/08/2026

## Algorithm Summary

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** 
  - Chooses the smallest element from a unsorted list and switches it with the first unsorted element.

## Array vs Linked List Analysis

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        | Arrays allow direct access by index, while linked lists require traversal. |
| Insert    | O(n)  | O(1)        | Inserting at the head of a list is quick, but arrays require shifting elements. For example when inserting, the elements of an array have to shft to the right.|
| Delete    | O(n)  | O(1)        | Same reasoning as insertion. Elements shift to the left instead.; it's quick at the head for lists. |

## Test Results
- Sorted list of cities by population shows correct ascending/descending order.
- Compared Python's built-in sort: more efficient due to Timsort (O(n log n)).

## Reflection Questions

1. **Why is selection sort O(n²)?**
   - Each selection requires scanning unsorted elements, leading to (n) iterations and comparisons. This leads to O(n x n) which is equal to O(n^2).


2. **When would you choose a linked list over an array?**
    Use a linked list when the list cna change dynamically. Linked list is much better than dealing with deletions or insertions than arrays.
3. **Why does Python use arrays (lists) as the default sequence type?**
    Arrays provide effecient accesss by index considering they are randomly accessable (O(1)). As opposed to inserting or deleting, arrays are very quick when it comes to reading. They also do not contain any pointers. 
