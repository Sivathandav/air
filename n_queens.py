def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if no queens are attacking in the same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # Check if no queens are attacking diagonally
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == "Q":
                return False

        return True

    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return solutions


# Demonstration of solving the n-Queens problem
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    solutions = solve_n_queens(n)

    print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
    for i, solution in enumerate(solutions):
        print(f"Solution {i+1}:")
        for row in solution:
            print(row)
        print()
