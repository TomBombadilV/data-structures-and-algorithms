# Implementation of Prim's Minimum Spanning Tree Algorithm

from graph import WeightedAdjacencyMatrix, undirected
from queue import PriorityQueue
from typing import List, Set

def _add_edges(g: WeightedAdjacencyMatrix, 
               v: int, 
               explored: Set, 
               crossing_edges: PriorityQueue) -> PriorityQueue:
    """
    Adds a vertex's crossing edges (edges that go from explored vertex to 
    unexplored vertex) to heap of crossing edges 
    '"""
    v_edges = g.matrix[v]
    for v_tail, weight in enumerate(v_edges):
        # Only add crossing edges
        if weight and not v_tail in explored:
            crossing_edges.put((weight, v, v_tail))
    return crossing_edges

def prims(g: WeightedAdjacencyMatrix) -> WeightedAdjacencyMatrix:
    """
    Performs Prim's algorithm on a Weighted Adjacency Matrix graph and returns
    its minimum spanning tree. Assumes graph is connected and undirected.
    """
    # Initialize starting vertex, heap, and MST
    s = 0 
    crossing_edges = PriorityQueue()
    mst = WeightedAdjacencyMatrix(g.size())
    
    # Add s to explored set and add its edges to heap
    explored = {s}
    crossing_edges = _add_edges(g, s, explored, crossing_edges)

    # While vertices haven't been explored
    while len(explored) < g.size():
        # Get edge with smallest weight
        weight, v_head, v = crossing_edges.get()
        # Make sure it hasn't been explored, then add it to MST
        if not v in explored:
            explored.add(v)
            crossing_edges = _add_edges(g, v, explored, crossing_edges)
            mst.add_edge(v_head, v, weight)
            mst.add_edge(v, v_head, weight)
    return mst

# Driver Code

# Graph from https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
g = WeightedAdjacencyMatrix(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)
g.print_graph()
g = undirected(g)
g.print_graph()
print("MST -------- ")
mst = prims(g)
mst.print_graph()
