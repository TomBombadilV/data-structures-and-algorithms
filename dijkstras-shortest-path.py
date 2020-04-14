# Dijkstra's Shortest Path Algorithm
# Two methods:
# 1. Naive method with exhaustive search => O(V * E)
# 2. Heap method with min heap => O(VlogE)
# This implementation uses method #2

from graph import WeightedAdjacencyList
from queue import PriorityQueue
from typing import Dict, List

# Add a vertex to explored set and add its edges to the heap
def add_vertex( g: WeightedAdjacencyList, v: int, explored: List[int], 
                crossing_edges: PriorityQueue, vertex_scores: List[int], 
                curr_vertex_score: int) -> None:
    # Mark as explored
    explored[v] = True
    # Save value of shortest path from s to this vertex
    vertex_scores[v] = curr_vertex_score
    # Add each outgoing edge from vertex to unvisited vertex
    for edge in g.list[v]:
        # Retrieve head vertex and edge weight
        head_vertex, weight = edge
        # Add edge if head vertex has not been explored yet
        if not(explored[head_vertex]):
            # Dijkstra's greedy score is tail vertex score plus edge weight
            crossing_edges.put((vertex_scores[v] + weight, head_vertex))

# Calculate shortest path in graph from vertex s to vertex t
def dijkstras(g: WeightedAdjacencyList, s: int, t: int) -> int:
    # Keep track of whether vertex has been explored or not
    explored = [False] * g.size()
    # Min heap for crossing edges' Dijkstra's greedy scores
    crossing_edges  = PriorityQueue()
    # List of vertex scores
    vertex_scores = []
    # Add start vertex
    add_vertex(g, s, explored, crossing_edges, vertex_scores, 0)
    while crossing_edges.qsize():
        # Get edge with smallest Dijkstra score
        weight, vertex = crossing_edges.get()  
        # Make sure vertex has not been explored yet
        if not(explored[vertex]):
            # Add vertex to explored set
            add_vertex(g, vertex, explored, crossing_edges, vertex_scores, weight)
    return vertex_scores[t]

# Driver code
g = WeightedAdjacencyList(4)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 3)
g.print_graph()

print(dijkstras(g, 0, 3))

# Trying another graph
g = WeightedAdjacencyList(7)
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

print(dijkstras(g, 0, 6))
