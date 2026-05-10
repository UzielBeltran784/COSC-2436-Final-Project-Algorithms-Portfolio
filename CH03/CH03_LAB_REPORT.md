# Lab 3: Recursion

## Student Information
- **Name:** Uziel Beltran
- **Date:** 02/15/2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** Explain when the function should stop calling itself. The simplest, non-recursive case; when the function knows what value to return.
Example: For fact(x), the base case is x == 1, returning 1.
When it 
2. **Recursive Case:** Explain how the function calls itself with a smaller problem. The part where the function calls itself with a smaller problem.
Example: For fact(x), the recursive call is x * fact(x - 1).

### The Call Stack
The stack of function calls that keeps track of multiple function invocations.
Example: In fact(5), the stack grows with calls for fact(4), fact(3), etc., and unwinds as it returns results.

## Function Analysis

| Function        | Base Case       | Recursive Case                  | Time Complexity |
|-----------------|-----------------|---------------------------------|-----------------|
| countdown       | i <= 0          | countdown(i-1)                  | O(n)            |
| fact            | x <= 1          | x * fact(x-1)                   | O(n)            |
| recursive_sum   | empty list      | first + sum(rest)               | O(n)            |
| recursive_count | empty list      | 1 + count(rest)                 | O(n)            |
| recursive_max   | single element  | max(first, max(rest))           | O(n)            |

## Reflection Questions

1. What happens if you forget the base case?
Without a base case, the function would enter an infinite recursive loop, eventually causing a stack overflow error.
2. Why is the naive Fibonacci implementation inefficient?
It recalculates values for the same Fibonacci numbers multiple times, leading to exponential time complexity.
3. Draw the call stack for `fact(4)`.
fact(4)
→ 4 * fact(3)
→ 3 * fact(2)
→ 2 * fact(1)
→ returns 1
↳ Unwinds:
2 * 1 = 2
3 * 2 = 6
4 * 6 = 24
