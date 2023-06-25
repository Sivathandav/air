import multiprocessing


def parallel_sum(numbers):
    pool = multiprocessing.Pool()
    result = pool.map(sum, numbers)
    pool.close()
    pool.join()
    return sum(result)


# Demonstration of parallel sum calculation
if __name__ == "__main__":
    n = int(input("Enter the number of lists: "))

    numbers = []
    for i in range(n):
        lst = list(map(int, input(f"Enter the space-separated numbers for list {i + 1}: ").split()))
        numbers.append(lst)

    total_sum = parallel_sum(numbers)
    print("Total sum:", total_sum)
