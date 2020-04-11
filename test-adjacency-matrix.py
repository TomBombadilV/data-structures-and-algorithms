from graph import AdjacencyMatrix

a = AdjacencyMatrix(5)
a.add_edge(1, 4)
a.add_edge(0, 3)
a.add_edge(2, 0)
a.print_graph()
a.remove_edge(0,0)
a.remove_edge(2, 0)
a.print_graph()
