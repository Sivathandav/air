class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_greedy_approximation(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    n = len(items)
    total_value = 0
    total_weight = 0
    taken = [0] * n

    for i in range(n):
        if total_weight + items[i].weight <= capacity:
            total_weight += items[i].weight
            total_value += items[i].value
            taken[i] = 1

    return total_value, taken


# Demonstration of solving the Knapsack problem using a Greedy Approximation Algorithm
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))

    items = []
    for _ in range(n):
        weight, value = map(int, input("Enter the weight and value of an item: ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the capacity of the knapsack: "))

    total_value, taken = knapsack_greedy_approximation(items, capacity)

    print("Total value:", total_value)
    print("Items taken:", taken)
