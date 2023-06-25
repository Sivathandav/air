class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        distance = {v: float('inf') for v in self.vertices}
        distance[source] = 0

        for _ in range(len(self.vertices) - 1):
            for u, v, weight in self.edges:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        for u, v, weight in self.edges:
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains negative-weight cycle")

        return distance


# Demonstration of the Bellman-Ford algorithm
if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))
    vertices = list(range(num_vertices))

    graph = Graph(vertices)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter an edge (u, v, weight): ").split()
        graph.add_edge(int(u), int(v), int(weight))

    source = int(input("Enter the source vertex: "))

    distances = graph.bellman_ford(source)

    print("Shortest distances from the source vertex:")
    for vertex, distance in distances.items():
        print(f"Vertex {vertex}: {distance}")
