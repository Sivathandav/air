class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def kruskal_mst(self):
        mst = []
        disjoint_set = DisjointSet(self.vertices)

        # Sort edges in non-decreasing order of weight
        self.edges.sort(key=lambda x: x[2])

        for edge in self.edges:
            u, v, weight = edge
            root1 = disjoint_set.find(u)
            root2 = disjoint_set.find(v)

            if root1 != root2:
                mst.append(edge)
                disjoint_set.union(root1, root2)

        return mst


# Demonstration of Kruskal's algorithm with disjoint sets
if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))
    vertices = list(range(num_vertices))

    graph = Graph(vertices)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = input("Enter an edge (u, v, weight): ").split()
        graph.add_edge(int(u), int(v), int(weight))

    mst = graph.kruskal_mst()

    print("Minimum Spanning Tree:")
    for edge in mst:
        u, v, weight = edge
        print(f"{u} -- {v} : {weight}")
