# 2436 Lab 8 Balanced Tree


## Lab Report

### Student Information
- **Name:** [Uziel Beltran]
- **Date:** [04/05/2026]

### Algorithm Analysis

#### AVL Trees
- **Balance Factor Range:** [The balance factor is the difference between the heights of the left node and right node. -1 means left note is greater than right. 1 means the opposite. The acceplable range is between -1 and 1. ]
- **Why rebalance?** [Rebalancing makes sure that the tree remians properly balanced. As a result, worst case time complexities are prevented from occuring in binary search trees. Without rebalancing, the time complexity for the operations would cerianly worsen. Blancing enusres a time complexity of O(log n)for all operations.   ]
- **Time Complexity (all operations):** O(log n)

#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   |Left-Left  | RR  |
| RR   |Right-Right| LL  |
| LR   |Left-Right | RL  |
| RL   |Right-Left | LR  |


### Reflection Questions

1. Why is an unbalanced BST bad?
An unbalanced BST can result in tree operations that are inefficient, with a time complexity degrading to O(n) as the tree becomes skewed. This defeats the purpose of using a BST for rapid search and update operations intended to be O(log n)
2. How do rotations maintain the BST property?
Rotations adjust the structure of the tree without affecting the in-order sequence of the nodes. This means they restructure the tree to maintain balance while preserving the binary search tree property, where the left child is less than the parent node, and the right child is greater.
3. What other self-balancing trees exist?
Other than AVL trees, self-balancing trees include Splay Trees and B-Trees.
