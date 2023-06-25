def solve_hamiltonian_circuit(graph):
    n = len(graph)
    path = [None] * n

    def is_valid(v, pos, path):
        if graph[path[pos-1]][v] == 0:
            return False

        if v in path:
            return False

        return True

    def backtrack(pos):
        if pos == n:
            if graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, n):
            if is_valid(v, pos, path):
                path[pos] = v
                if backtrack(pos + 1):
                    return True
                path[pos] = None

        return False

    path[0] = 0
    if not backtrack(1):
        return None

    return path


# Demonstration of solving the Hamiltonian Circuit problem
if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))

    graph = []
    print("Enter the adjacency matrix:")
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    path = solve_hamiltonian_circuit(graph)

    if path is None:
        print("No Hamiltonian Circuit exists for the given graph.")
    else:
        print("Hamiltonian Circuit:")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])
