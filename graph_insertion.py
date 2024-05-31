class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.adjacency_list = {node: [] for node in range(num_of_nodes)}

    def add_edge(self, source, destination, weight=1):
        if source >= self.num_of_nodes or destination >= self.num_of_nodes:
            raise ValueError("Node index out of range.")

        self.adjacency_list[source].append((destination, weight))

        if not self.directed:
            self.adjacency_list[destination].append((source, weight))

    def print_adj_list(self):
        for node in self.adjacency_list:
            print('Node', node, ':', end=' ')
            for neighbor, weight in self.adjacency_list[node]:
                print(f'({neighbor}, {weight})', end=' ')
            print()

graph = Graph(5)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)
graph.print_adj_list()