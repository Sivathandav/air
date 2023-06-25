def compute_binomial_coefficient(n, k):
    # Create a table to store the computed values
    table = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill in the table using dynamic programming
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]

    return table[n][k]


# Demonstration of computing binomial coefficients
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    k = int(input("Enter the value of k: "))

    coefficient = compute_binomial_coefficient(n, k)
    print(f"The binomial coefficient C({n}, {k}) is: {coefficient}")
