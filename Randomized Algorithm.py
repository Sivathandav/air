import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)


# Demonstration of randomized quicksort
if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))

    arr = list(map(int, input("Enter the space-separated elements: ").split()))

    randomized_quicksort(arr, 0, len(arr) - 1)

    print("Sorted array:", arr)
