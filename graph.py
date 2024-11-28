import networkx as nx
import matplotlib.pyplot as plt

def display_graph(adjacency_structure):
    G = nx.DiGraph() 

    if isinstance(adjacency_structure, list):
        for node, neighbors in enumerate(adjacency_structure):
            G.add_node(node)
            G.add_edges_from((node, neighbor) for neighbor in neighbors)
    elif isinstance(adjacency_structure, (list, tuple)):
        num_nodes = len(adjacency_structure)
        G.add_nodes_from(range(num_nodes))

        for i in range(num_nodes):
            for j in range(num_nodes):
                if adjacency_structure[i][j] == 1:
                    G.add_edge(i, j)
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7, connectionstyle='arc3,rad=0.1')

    plt.show()

def input_adjacency_matrix():
    num_nodes = int(input("Enter the number of nodes : "))
    matrix = []

    print("Enter the adjacency matrix row-wise :")
    for i in range(num_nodes):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix

def input_adjacency_list():
    num_nodes = int(input("Enter the number of nodes: "))
    adjacency_list = []

    print("Enter the adjacency list for each node :")
    for i in range(num_nodes):
        neighbors = list(map(int, input(f"Enter neighbors for node {i} (-1 to end): ").split()))
        adjacency_list.append(neighbors)

    return adjacency_list

def main():
    print("Choose input type:")
    print("1. Adjacency Matrix")
    print("2. Adjacency List")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        adjacency_data = input_adjacency_matrix()
    elif choice == 2:
        adjacency_data = input_adjacency_list()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    display_graph(adjacency_data)

if __name__ == "__main__":
    main()
