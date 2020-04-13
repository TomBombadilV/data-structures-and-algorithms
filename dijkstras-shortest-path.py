# Dijkstra's Shortest Path Algorithm
# Two methods:
# 1. Naive method with exhaustive search O(V * E)
# 2. Heap method with min heap (My implementation) O(VlogE)

from graph import WeightedAdjacencyList
from queue import PriorityQueue
from typing import Dict

def add_vertex(g: WeightedAdjacencyList, v: int, explored: List[int], edge_scores: PriorityQueue, vertex_scores: Dict) -> None:
    for edge in g.list[v]:
        vertex, weight = edge
        edge_scores.add((vertex_scores[v] + weight, vertex))
    explored.append(v)


def dijkstras(g: AdjacencyList, s: int, t: int) -> int:
    # Array of explored vertices
    explored = []
    # Add all other vertices to unexplored
    unexplored = [i for i in range(g.size()) if not(i == s)] 
    # Min heap for crossing edges' Dijkstra's greedy scores
    edge_scores = PriorityQueue()
    # Dictionary of vertex scores
    vertex_scores = {s: 0}
    add_vertex(g, s, explored, edge_scores)
    while edge_scores and not(t in explored):
        vertex = edge_scores.get()        

