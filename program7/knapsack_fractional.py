def fractional_knapsack(weights, values, capacity):
    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            profit += value
        else:
            profit += ratio * capacity
            break

    return profit


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Profit:", fractional_knapsack(weights, values, capacity))