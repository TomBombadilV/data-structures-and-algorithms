class AdjacencyList:

    def __init__(self, n: int):
        # Using list of lists instead of list of sets to allow for multiple
        # instances of an edge
        self.list = [[] for _ in range(n)]

    # Returns number of vertices in graph
    def size(self) -> int:
        return len(self.list)

    # Make sure node is within range of list
    def is_valid(self, v: int) -> bool:
        return False if v > len(self.list) - 1 or v < 0 else True
    
    def add_edge(self, v1: int, v2: int) -> bool:
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist")
            return False
        # Make sure edge doesn't already exist. Remove this if you want to
        # allow multiple instances of the same edge. 
        if v2 in self.list[v1]:
            print("Edge already exists in the graph.")
        # Add edge. Yey.
        else:
            self.list[v1].append(v2)
            print("Edge successfully added.")
        return True

    def remove_edge(self, v1: int, v2: int) -> bool:
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist.")
            return False
        # Make sure edge exists
        if not(v2 in self.list[v1]):
            print("Edge does not exist in the graph.")
        # Delete edge
        else:
            self.list[v1].remove(v2)
            print("Edge successfully deleted.")
  
    def print_list(self) -> None:
        print("Adjacency List:")
        for i, l in enumerate(self.list):
            print("{0}->{1}".format(i, l))

class GraphNode:

    def __init__(self, val):
        self.val = val
        self.edges = []

    def print_edges(self):
        print("{0}'s edges: ".format(self.val), end="")
        print(*[edge.val for edge in self.edges])
