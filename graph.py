class AdjacencyList:
    def __init__(self, n: int):
        # Using list of lists instead of list of sets to allow for multiple
        # instances of an edge
        self.list = [[] for _ in range(n)]

    # Returns number of vertices in graph
    def size(self) -> int:
        return len(self.list)

    # Make sure vertex exists in graph
    def is_valid(self, v: int) -> bool:
        return False if v > len(self.list) - 1 or v < 0 else True
   
    # Add an edge to the graph
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

    # Remove an edge from the graph
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
        return True

    # Print entire graph
    def print_graph(self) -> None:
        print("Adjacency List:")
        for i, l in enumerate(self.list):
            print("{0}->{1}".format(i, l))

class WeightedAdjacencyList(AdjacencyList):
    def __init__(self, n: int):
        super().__init__(n)

    # Add weighted edge to graph
    def add_edge(self, v1: int, v2: int, weight: int) -> bool:    
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist.")
            return False
        # Make sure edge doesn't already exist
        if (v2, weight) in self.list[v1]:
            print("Edge already exists in graph.")
        else:
            # Edge is represented as tuple of head vertex and edge weight
            self.list[v1].append((v2, weight))
            print("Edge successfully added.")
        return True 
    
    # Remove an edge from the graph
    def remove_edge(self, v1: int, v2, int, weight: int) -> bool:
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist")
            return False
        # Make sure edge exists
        if not((v2, weight) in self.list[v1]):
            print("Edge does not exist in the graph.")
        else:
            self.list[v1].remove((v2, weight))
            print("Edge successfully deleted.")
        return True

class AdjacencyMatrix:
    def __init__(self, val):
        self.matrix = [[0 for _ in range(val)] for _ in range(val)]
   
    # Returns number of vertices in graph
    def size(self):
        return len(self.matrix)

    # Make sure given vertex exists in graph
    def is_valid(self, v: int) -> bool:
        return False if v > len(self.matrix) - 1 or v < 0 else True
   
    # Add an edge to the graph
    def add_edge(self, v1: int, v2: int) -> bool:
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist.")
            return False
        # Make sure edge doesn't already exist
        if self.matrix[v1][v2] == 1:
            print("Edge already exists in graph.")
        # Add edge
        else:
            self.matrix[v1][v2] = 1
            print("Edge successfully added.")
        return True

    # Remove an edge from the graph
    def remove_edge(self, v1: int, v2: int) -> bool:
        # Make sure vertices are valid
        if not(self.is_valid(v1) or self.is_valid(v2)):
            print("At least one of given vertices does not exist.")
            return False
        # Make sure edge exists
        if self.matrix[v1][v2] == 0:
            print("Edge does not exist in graph.")
        else:
            self.matrix[v1][v2] = 0
            print("Edge successfully deleted.")
        return True

    # Print entire graph
    def print_graph(self) -> None:
        for row in self.matrix:
            print(*row)

class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.edges = []

    def print_edges(self):
        print("{0}'s edges: ".format(self.val), end="")
        print(*[edge.val for edge in self.edges])
