from collections import defaultdict
from graph import GraphNode
from typing import Dict, List

def dfs(s: GraphNode) -> None:
    """ Prints list of graph nodes in DFS order starting from given start node.
        For an acyclic, connected graph. Assumes all nodes can be accessed from 
        start node.
    """
    visited = defaultdict(bool)
    res = dfs_recursive(s, visited, [])
    print("Depth First Search Ordering: ", end="")
    print(*[n.val for n in res])

def dfs_recursive(n: GraphNode, visited: Dict[GraphNode, bool], res: List[GraphNode]) -> List[GraphNode]:
    res.append(n)
    visited[n] = True
    for edge in n.edges:
        if not(visited[edge]):
            dfs_recursive(edge, visited, res)
    return res

def bfs(s: GraphNode) -> None:
    """ Prints list of graph nodes in BFS order starting from given start node.
        For an acyclic, connected graph. Assumes all nodes can be accessed from
        start node.
    """
    visited = defaultdict(bool)
    q, res = [], []
    curr = s
    while q or curr:
        # Make sure vertex hasn't been visited yet
        if not(visited[curr]):
            # Mark as visited
            visited[curr] = True
            # Add to list
            res.append(curr)
            # Add all edges to queue
            for edge in curr.edges:
                q.append(edge)
        # Get next vertex in queue
        curr = q[0] if q else None
        q = q[1:]
    print("Breadth First Search Ordering: ", end="")
    print(*[n.val for n in res])

def topological_sort(nodes: List[GraphNode]) -> None:
    visited = defaultdict(bool)
    res = []
    for node in nodes:
        if not(visited[node]):
            topo_sort_recursive(node, visited, res)
    print("Topological Sorting: ", end="")
    print(list(reversed([n.val for n in res])))

def topo_sort_recursive(n: GraphNode, visited: Dict[GraphNode, bool], res: List[GraphNode]) -> List[GraphNode]:
    visited[n] = True
    for edge in n.edges:
        if not(visited[edge]):
            topo_sort_recursive(edge, visited, res)
    res.append(n)
    return res

# Driver code for an acyclic, connected graph
a = GraphNode(0)
b = GraphNode(1)
c = GraphNode(2)

a.edges.append(b)
a.edges.append(c)
b.edges.append(c)

a.print_edges()
nodes = [a, b, c]

dfs(a)
dfs(b)

bfs(a)

topological_sort(nodes)
