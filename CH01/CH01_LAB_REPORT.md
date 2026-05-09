# Chapter 1 Lab Report: Binary Search

## Student Information
- **Name:** [Uziel Beltran]
- **Date:** [May 9, 2026]
- **Course:** COSC 2436

## Algorithm Summary

### Linear Search
[Linear search is a simple search algorithm that checks each element in a list one by one until it finds the target item or reaches the end of the list.
Best case: (O(1)) when the item is at the first position.
Worst case: (O(n)) when the item is at the last position or not present.
When to Use:
Use when the list is small or unsorted]

### Binary Search
[Binary search is an efficient search algorithm that works on sorted lists. It repeatedly divides the list in half, checking the middle element and discarding half of the list until it finds the target item or determines it isn't present. 
Best case: (O(1)) when the item is in the middle.
Worst case: (O(\log n)) due to the halving process.
When to Use:
Use when the list is sorted and you need efficient searching.]

## Test Results

[Paste the output:
Binary Search vs Linear Search Time Comparison
================================================
Searching in a sorted list of 128 numbers

Searching for: 1
Linear search time: 0.00010061 seconds
Binary search time: 0.00000334 seconds
Linear search result: 0
Binary search result: 0
Binary search is 30.10x faster

Searching for: 64
Linear search time: 0.00009871 seconds
Binary search time: 0.00000334 seconds
Linear search result: 63
Binary search result: 63
Binary search is 29.55x faster

Searching for: 128
Linear search time: 0.00009584 seconds
Binary search time: 0.00000310 seconds
Linear search result: 127
Binary search result: 127
Binary search is 30.90x faster

Searching for: 50
Linear search time: 0.00002837 seconds
Binary search time: 0.00000358 seconds
Linear search result: 49
Binary search result: 49
Binary search is 7.91x faster

... (more results) ...

Lab Challenge Answer:
Maximum steps for binary search in 128 items:
log2(128) = 7 steps maximum]
