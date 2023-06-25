import math


def tsp_nearest_neighbor(graph):
    n = len(graph)
    start_vertex = 0
    visited = [False] * n
    visited[start_vertex] = True
    path = [start_vertex]
    total_cost = 0

    for _ in range(n - 1):
        min_distance = math.inf
        nearest_vertex = -1

        for v in range(n):
            if not visited[v] and graph[path[-1]][v] < min_distance:
                min_distance = graph[path[-1]][v]
                nearest_vertex = v

        path.append(nearest_vertex)
        visited[nearest_vertex] = True
        total_cost += min_distance

    path.append(start_vertex)
    total_cost += graph[path[-2]][start_vertex]

    return path, total_cost


# Demonstration of solving the Traveling Salesman Problem (TSP) using a Nearest Neighbor Algorithm
if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))

    graph = []
    print("Enter the adjacency matrix for the graph:")
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    path, total_cost = tsp_nearest_neighbor(graph)

    print("Path:", path)
    print("Total cost:", total_cost)
