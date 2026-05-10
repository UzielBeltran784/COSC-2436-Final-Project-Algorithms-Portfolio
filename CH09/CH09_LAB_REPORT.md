# Lab Report — Dijkstra's Shortest Path

Student Information

Name: Uziel Beltran  
Date: 04/12/2026  
Algorithm Analysis: Dijkstra's Algorithm

What type of graph does this program build? [undirected, weighted]

Why must all edge weights be non-negative for Dijkstra's to work? [Dijkstra's algorithm assumes that once a node is processed, the shortest path to it is found, making negative weights break this assumption.]

Time Complexity (with simple array scan for min-node): [O(V^2)]  
Time Complexity (with a min-heap/priority queue): [O((V+E)log V)]

Core Data Structures

Structure    Variable Name    What It Stores  
Adjacency dict    graph    connections and weights between nodes  
Cost table    costs    Current shortest paths costs  
Parent table    parents    Previous node on the shortest path  
Visited list    processed    Nodes that have been processed

Algorithm Trace

Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D:

Iteration    Current Node    costs[A]    costs[B]    costs[C]    costs[D]    processed  
Init    —    0    ∞    ∞    ∞    —  
1    A    0    1    4    ∞    A  
2    B    0    1    3    7    A, B  
3    C    0    1    3    6    A, B, C  
4    D    0    1    3    6    A, B, C, D

Shortest path A to D: A to B to C to D  
Total cost: 6

Reflection Questions

Why does the algorithm initialize all node costs to infinity except the start node?  
Initializing node costs to infinity implies that the nodes are unreachable initially, except the start node. This allows the algorithm to compare and find the shortest path, updating the costs as shorter paths are discovered.

Why do we store edges in both directions (graph[a][b] and graph[b][a])? What would break if we only stored one direction?  
Storing edges in both directions makes the graph undirected, allowing traversal in both directions. If we only stored one direction, you could only traverse the graph in one way, potentially missing paths that are bidirectional.

The find_lowest_cost_node() function scans all nodes linearly. How would using a priority queue (min-heap) improve performance, and why does it matter for large graphs?  
Using a min-heap improves find_lowest_cost_node() performance from linear time to logarithmic time for extraction. Instead of scanning all nodes, a min-heap maintains the lowest-cost node at the top, allowing the algorithm to quickly access and remove it, reducing overall complexity for large, sparse graphs. Without a heap, the time spent finding the best node grows linearly with the graph size, leading to severe slowdowns.

If a negative edge weight were introduced (e.g., A-B with weight -3), explain how Dijkstra's algorithm could produce an incorrect result. What algorithm handles negative weights?  
Dijkstra's assumes that once a node's shortest path is found, it won't be updated. Negative weights can lead to recalculations, violating this assumption. The Bellman-Ford algorithm is used to handle graphs with negative weights.

How does the parents dictionary allow path reconstruction? Why do we reverse the path at the end?  
The parents dictionary stores the previous node leading to the current node in the shortest path. By backtracking from the destination to the start node using these parent links, you can reconstruct the path. The path is reversed at the end since it's built from the destination to the start.

What happens when the source and destination are in disconnected components of the graph? How does the code detect this?  
If the destination node's cost remains infinity, it means there's no path from the source to the destination. The algorithm detects this condition during path evaluation and returns None.
