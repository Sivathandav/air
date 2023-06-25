import math


def tsp_branch_and_bound(graph):
    n = len(graph)
    best_path = []
    best_cost = math.inf

    def backtrack(curr_vertex, visited, path, cost):
        nonlocal best_path, best_cost

        if len(visited) == n:
            path.append(curr_vertex)
            cost += graph[curr_vertex][0]
            if cost < best_cost:
                best_cost = cost
                best_path = path.copy()
            return

        for next_vertex in range(n):
            if next_vertex not in visited:
                path.append(curr_vertex)
                visited.add(next_vertex)
                backtrack(next_vertex, visited, path, cost + graph[curr_vertex][next_vertex])
                visited.remove(next_vertex)
                path.pop()

    visited = set()
    visited.add(0)
    backtrack(0, visited, [], 0)

    return best_path, best_cost


# Demonstration of solving the Traveling Salesman Problem (TSP) using Branch and Bound
if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))

    graph = []
    print("Enter the adjacency matrix for the graph:")
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    best_path, best_cost = tsp_branch_and_bound(graph)

    print("Best path:", best_path)
    print("Best cost:", best_cost)
