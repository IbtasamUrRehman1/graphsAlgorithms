import  numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = np.zeros((vertices, vertices), dtype=int)
        self.graph = nx.Graph()

    def add_edge(self,u,v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.graph.add_edge(u,v)

    def display_graph_with_adjancy_matrix(self): # Create a figure with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,4))
        # plot the graph
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', ax=ax1)
        ax1.set_title('Graph Visualization')
        # Plot the adhancy matrix as an image
        ax2.matshow(self.adj_matrix, cmap='viridis')
        ax2.set_title('Adjancy Matrix')

        # Display the adjancy matrix in the terminal
        print("Adjancy Matrix:")
        for row in self.adj_matrix:
            print(row)
        # Display the figure
        plt.show()
#Example
if __name__ == "__main__": # Create a graph with 5 vertices
    vertices = 5
    graph = Graph(vertices)
    # Add Edges
    graph.add_edge(0,1)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(2,3)

    # Dispplay the graph with adjancy matrix
    graph.display_graph_with_adjancy_matrix()









