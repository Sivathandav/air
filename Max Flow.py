class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    def bfs(self, source, sink, parent):
        visited = [False] * self.vertices
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.vertices):
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def max_flow(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            v = sink

            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow

        return max_flow


# Demonstration of solving the Max Flow problem
if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))

    graph = Graph(num_vertices)

    num_edges = int(input("Enter the number of edges: "))

    print("Enter the edges and their capacities:")
    for _ in range(num_edges):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u, v, capacity)

    source = int(input("Enter the source vertex: "))
    sink = int(input("Enter the sink vertex: "))

    max_flow = graph.max_flow(source, sink)

    print("Maximum Flow:", max_flow)
