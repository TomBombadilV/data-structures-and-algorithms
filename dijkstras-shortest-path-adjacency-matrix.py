# Dijkstra's Shortest Path implementation with adjacency matrix
# Two methods:
# 1. Naive method with exhaustive search => O(V * E)
# 2. Heap method with min heap => O(VlogE)
# This implementation uses method #1

from graph import WeightedAdjacencyMatrix
from math import inf
from typing import Dict, List
from queue import PriorityQueue

def select_new_vertex(g: WeightedAdjacencyMatrix, explored: List[bool], dist: List[int]):
    # Preserve the minimum distance and the selected vertex
    min_dist, selected_v = inf, None
    # Go through all tail vertices in matrix
    for v_tail, edges in enumerate(g.matrix):
       # Only visit tail vertices that have already been explored
       if explored[v_tail]:
            # Go through each edge
            for v_head, weight in enumerate(edges):
                # Make sure edge exists and head vertex hasn't been explored
                if weight and not(explored[v_head]):
                    # Calculate greedy score
                    new_dist = dist[v_tail] + weight
                    # If new score minimizes, then save vertex and score
                    if new_dist < min_dist:
                        selected_v = v_head
                        min_dist = new_dist
    return min_dist, selected_v 

def dijkstras(g: WeightedAdjacencyMatrix, s: int, t: int) -> int:
    explored = [False] * g.size()
    dist = [None] * g.size()
    explored[s] = True
    dist[s] = 0
   
    # This assumes that t is findable from s.
    # While t hasn't been explored, keep selecting the edge that crosses
    # from the explored set to the undexplored set and minimiszes Dijkstra's
    # greedy score (finds the shortest distance to the head vertex)
    while not(explored[t]):
        # Select minimizing edge
        min_dist, selected_v = select_new_vertex(g, explored, dist)
        # Mark selected vertex as explored
        explored[selected_v] = True
        # Save score for vertex
        dist[selected_v] = min_dist
    # Return shortest path to t
    return dist[t]

# Driver code
g = WeightedAdjacencyMatrix(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 3)
g.print_graph()

print(dijkstras(g, 0, 3))

# Trying another graph
# This graph is from https://stackabuse.com/graphs-in-java-dijkstras-algorithm/
g = WeightedAdjacencyMatrix(7)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 11)
g.add_edge(1, 2, 7)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 8)
g.add_edge(2, 4, 9)
g.add_edge(3, 4, 5)
g.add_edge(3, 5, 2)
g.add_edge(4, 6, 6)
g.add_edge(5, 4, 1)
g.add_edge(5, 6, 8)
g.print_graph()

print(dijkstras(g, 0, 6))

# Yet another graph
# This one is from https://ycpcs.github.io/cs360-spring2015/lectures/lecture22.html
g = WeightedAdjacencyMatrix(5)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 3)
g.add_edge(1, 0, 3)
g.add_edge(2, 3, 2)
g.add_edge(3, 2, 1)
g.add_edge(3, 1, 1)
g.add_edge(4, 1, 4)
g.add_edge(4, 3, 2)

print(dijkstras(g, 4, 2))
