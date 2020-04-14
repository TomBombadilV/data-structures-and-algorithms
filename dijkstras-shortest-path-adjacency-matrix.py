# Dijkstra's Shortest Path implementation with adjacency matrix
# Two methods:
# 1. Naive method with exhaustive search => O(V * E)
# 2. Heap method with min heap => O(VlogE)
# This implementation uses method #1

from graph import WeightedAdjacencyMatrix
from typing import Dict, List
from queue import PriorityQueue

def dijkstras(g: WeightedAdjacencyMatrix, s: int, t: int) -> int:
    explored = [False] * g.size()
    dist = [None] * g.size()

