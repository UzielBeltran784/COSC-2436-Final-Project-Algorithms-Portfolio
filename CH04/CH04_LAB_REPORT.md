
## Student Information
- **Name:** [Uziel Beltran]
- **Date:** [02/22/2026]

## Quicksort Concepts

### Divide and Conquer
[Quicksort utilizes divide and conquer by partioning the array into 2 sub arrays around a pivot. It then sorts each sub arrray recursively, and then combines the results to form one final sorted array. ]

### The Three Steps
1. **Choose pivot:** [Basically choose any random element in the array. In this lab it was the first element.]
2. **Partition:** [Once a pivot is chosen, divide the elements into what is greater than the pivot and what is less than. ]
3. **Recurse and combine:** [After partioning, quicksort is applied to each sub arrays. This goes on until the sub array is empty or has one element. ]

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
[Array  [3, 5, 2, 1, 4]:
The pivot is 3.
less becomes [2, 1].
greater becomes [5, 4].
The recursive call sorts each of these:
quicksort([2, 1]) results in [1, 2].
quicksort([5, 4]) results in [4, 5].
Combined, you get [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5].]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | [Happens when the pivot divides the array into two equal halves each time] |
| Average | O(n log n) | [Typical for random data, where partitions are balanced more often than not.  ] |
| Worst | O(n²) | [Occurs when the smallest or largest element is always chosen as the pivot, leading to unbalanced partitions.] |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
 If the array is already sorted and the first element is consistently chosen as the pivot, each partitioning step will create very unbalanced partitions. Specifically, one partition will have only one element (the pivot), and the other partition will contain the rest of the elements.

2. How could you improve pivot selection to avoid worst-case performance?
To avoid worst-case performance, you can improve pivot selection by choosing a pivot more randomly. Select a random element as the pivot to get a more balanced partition.

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
Generally faster on average due to its O(n log n) complexity. However, it has a worst-case of O(n²) if poor pivoting occurs.  

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
array[1:] is used to exclude the pivot from being included in the less and greater lists. The pivot is always the first element in this implementation, and you do not want to compare it with itself when partitioning.
