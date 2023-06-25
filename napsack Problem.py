class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_branch_and_bound(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    n = len(items)
    best_value = 0
    best_taken = [0] * n

    def backtrack(i, current_weight, current_value, taken):
        nonlocal best_value, best_taken

        if current_weight > capacity:
            return

        if current_value > best_value:
            best_value = current_value
            best_taken = taken.copy()

        if i == n:
            return

        remaining_capacity = capacity - current_weight
        potential_value = current_value
        for j in range(i, n):
            if items[j].weight <= remaining_capacity:
                remaining_capacity -= items[j].weight
                potential_value += items[j].value
            else:
                potential_value += items[j].ratio * remaining_capacity
                remaining_capacity = 0
                break

        if potential_value <= best_value:
            return

        backtrack(i + 1, current_weight + items[i].weight, current_value + items[i].value, taken + [1])
        backtrack(i + 1, current_weight, current_value, taken + [0])

    backtrack(0, 0, 0, [])

    return best_value, best_taken


# Demonstration of solving the Knapsack problem using Branch and Bound
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))

    items = []
    for _ in range(n):
        weight, value = map(int, input("Enter the weight and value of an item: ").split())
        items.append(Item(weight, value))

    capacity = int(input("Enter the capacity of the knapsack: "))

    best_value, best_taken = knapsack_branch_and_bound(items, capacity)

    print("Best value:", best_value)
    print("Items taken:", best_taken)
