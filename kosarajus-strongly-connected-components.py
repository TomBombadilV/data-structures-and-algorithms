# Kosaraju's Two Pass Algorithm to find strongly connected components
# 1. Perform DFS on reversed graph to create finishing order
# 2. Perform DFS on original graph with finishing times as node order to find
#    strongly connected components.

from graph import AdjacencyList
from typing import List

def kosaraju_scc(g: AdjacencyList) -> List[List]:
   
    # Reverses all of the edges of the original graph and returns as new graph 
    def reverse_graph(g: AdjacencyList) -> AdjacencyList:
        # Create new graph
        g_rev = AdjacencyList(g.size())
        # For each vertex in old graph, add its reversed edge to new graph
        for i, l in enumerate(g.list):
            for v in l:
                g_rev.add_edge(v, i)
        return g_rev

    # Perform DFS, marking the finishing time when all of vertice's edges have 
    # been visited
    def dfs_finishing_time_util(g_rev: AdjacencyList, s: int, 
                                visited: List[bool], time: int, 
                                finishing_time: List[int]) -> int:
        visited[s] = True
        for v in g_rev.list[s]:
            if not(visited[v]):
                time = dfs_finishing_time_util( g_rev, v, visited, time, 
                                                finishing_time)
        # Once all edges have been visited, mark and increment finishing time
        finishing_time[s] = time
        time += 1
        return time
   
    # Perform DFS on reversed graph to get finishing time of vertices
    def dfs_finishing_time(g_rev: AdjacencyList) -> List[int]:
        # Counter for finishing time
        time = 0
        # Array to keep track of finishing time for each vertex
        finishing_time = [None] * g_rev.size()
        # Whether each vertex has been visited or not
        visited = [False] * g_rev.size()
        # Perform DFS on all vertices
        for i in reversed(range(g_rev.size())):
            if not(visited[i]):
                time = dfs_finishing_time_util( g_rev, i, visited, time, finishing_time)
        print(time)
        print(finishing_time, visited)
        return finishing_time
   
    # Alter finishing_time from ft[i] where i is vertex number and ft[i] is
    # finishing time => ft[i] where i is finishing time and ft[i] is vertex 
    # number. This is so we can perform DFS in incremental order based on the
    # finishing time and also look up the original vertex number.
    def convert_finishing_time(finishing_time: List[int]) -> List[int]:
        converted = [None] * len(finishing_time)
        for i, t in enumerate(finishing_time):
            converted[t] = i
        return converted

    def dfs_scc_util(   g: AdjacencyList, s: int, visited: List[int], 
                        res: List[int]) -> List[int]:
        visited[s] = True
        res.append(s)
        for v in g.list[s]:
            if not(visited[v]):
                dfs_scc_util(g, v, visited, res)
        return res

    # Perform DFS on original graph with vertices ordered by finishing time to
    # get strongly connected components
    def dfs_scc(g: AdjacencyList, finishing_time: List[int]) -> List[List[int]]:
        # List of groups of strongly connected components
        scc = []
        # Whether each vertex has been visited or not
        visited = [False] * g.size()
        for i in reversed(range(g.size())):
            if not(visited[finishing_time[i]]):
                scc.append(dfs_scc_util(g, finishing_time[i], visited, []))
        return scc

    g_rev = reverse_graph(g) 
    g_rev.print_list()
    ft = dfs_finishing_time(g_rev)
    ft = convert_finishing_time(ft)
    return dfs_scc(g, ft) 

# Driver code
g = AdjacencyList(4)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(2, 1)
g.print_list()

print(kosaraju_scc(g))

# Trying another graph!
g = AdjacencyList(9)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 6)
g.print_list()

print(kosaraju_scc(g))
