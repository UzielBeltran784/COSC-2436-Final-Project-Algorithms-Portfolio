## Student Information
**Name:** [Uziel Beltran]  
**Date:** [04/19/2026]  
**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---

# Algorithm Understanding

**What type of problem is this algorithm solving?**  
[ Packing problem]

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
[No, a greedy algorithm isn't guaranteed to produce the optimal solution. Greedy algorithms make the most optimal immediate choice without considering the overall solution, which might lead to suboptimal results.]

**What is the greedy choice made in this algorithm?**  
[The greedy choice here is to pack the largest boxes first to maximize the utilization of the truck's volume quickly.]

---

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
[Sorting boxes in descending order ensures that the largest boxes are considered first, which maximizes the space used as efficiently as possible.]

**What would happen if we sorted the boxes in ascending order instead?**  
[Sorting boxes in descending order ensures that the largest boxes are considered first, which maximizes the space used as efficiently as possible.]

**Why do we keep track of `used_volume`?**  
[Tracking used_volume ensures the total volume of packed boxes does not exceed the truck's capacity, thus preventing overflow and ensuring adherence to constraints.]

---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
[Volume alone doesn't account for the physical dimensions and arrangement, which can lead to situations where boxes fit by volume but don't physically fit due to size constraints.]

**Give an example where a box fits by volume but not by dimensions.**  
[A long and narrow box may fit within the total volume allowed but can't be positioned due to length exceeding the truck's width or height.]

**How would you modify the algorithm to check dimension constraints before packing a box?**  
[The algorithm should check each box's dimensions against the truck's dimensions to ensure it fits physically, not just in terms of volume.]

---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
[A greedy approach may fail when smaller boxes, if packed first, could allow for more efficient use of the remaining space with larger boxes, ultimately allowing more boxes overall.]

**How is this problem related to the Knapsack Problem?**  
[This problem is akin to the Knapsack Problem, where items are selected to maximize the value (or space usage) within limited capacity without exceeding it.]

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
[A dynamic programming algorithm could guarantee an optimal solution but at the cost of higher computational time and resource usage compared to a greedy approach.]

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
[An additional constraint for weight would be needed, requiring the algorithm to check both volume and weight before packing each box.]

**Why are greedy algorithms often preferred despite not always being optimal?**  
[Greedy algorithms are simple, easier to implement, and execute faster, making them suitable for large-scale problems where absolute precision isn't critical.]
