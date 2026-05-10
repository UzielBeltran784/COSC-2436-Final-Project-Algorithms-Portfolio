# Chapter 11: Dynamic Programming — Lab Report

## Student Information
- **Name:** [Uziel Beltran]
- **Date:** [4/26/2026]
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** [Dynamic programming (DP) works by breaking a complex problem into smaller, simpler subproblems, solving each once, and storing the answers so they can be reused later. This improves efficiency by avoiding repeated calculations.]
- **Time complexity:** [O(n X w)]
- **When to use it:** [Dynamic programming is best used for optimization problems that contain
overlapping subproblems and optimal substructure. Common examples include
finding shortest paths, calculating Fibonacci numbers, solving knapsack
problems, and sequence alignment problems.]

## Test Results

| Capacity | Best Items Selected | Total Value |
|----------|---------------------|-------------|
| 1 | GOLD BAR | $30000 |
| 2 | GOLD BAR + iPHONE | $32000 |
| 3 | GOLD BAR + GUITAR + iPHONE | $33500 |
| 4 | GOLD BAR + GUITAR + iPHONE | $33500 |
| 5 | GOLD BAR + GUITAR + iPHONE + BOOK | $33600 |
| 6 | GOLD BAR + GUITAR + iPHONE + BOOK | $33600 |

### Sample Program Output

```
                   1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33`500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)
```

# Reflection Questions

1. **[Why is the knapsack problem considered an optimization problem]**
   [The knapsack problem requires finding the best possible combination of items
while staying within a fixed capacity limit. Since there are many possible
choices, the algorithm must determine which selection produces the maximum
total value. This makes it an optimization problem because the goal is to
find the most optimal solution among many possibilities.]

2. **[Describe the role of the 2D grid in solving the knapsack problem.]**
   [The 2D grid (or table) records the best combination of items for each subproblem, defined by the number of items considered and the weight capacity available. Each cell (grid[i][w]) contains the optimal list of items when considering the first i items with a total possible weight of w.]

4. **[How did item weights and values affect the final solution?]**
   [The algorithm compared both the weight and value of each item to determine
which combination produced the highest overall value without exceeding the
capacity limit. Some items with smaller weights but higher values were more
beneficial than heavier items with lower value. This comparison process helped
the program find the optimal combination.]

## Challenges Encountered
[One challenge during this lab was understanding how the two-dimensional grid
stored the best item combinations for each capacity. At first, it was confusing
to determine why certain items were included or excluded as the algorithm moved
through the table. I resolved this by tracing the program step by step and
comparing the values of including versus excluding each item, which helped me
better understand how dynamic programming builds the optimal solution.]

