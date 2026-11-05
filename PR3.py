
# Fractional Knapsack using Greedy Method

def fractional_knapsack(weights, profits, capacity):

    n = len(weights)
    items = []

    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort by profit/weight ratio
    items.sort(reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    print("\nItems selected:")

    for ratio, weight, profit, item_no in items:

        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:

            total_profit += profit
            remaining_capacity -= weight

            print("Item", item_no, ": Full item",
                  "Weight =", weight,
                  "Profit =", profit)

        else:

            fraction = remaining_capacity / weight
            total_profit += profit * fraction

            print("Item", item_no, ":",
                  round(fraction, 2), "fraction",
                  "Weight =", remaining_capacity,
                  "Profit =", round(profit * fraction, 2))

            remaining_capacity = 0

    print("\nMaximum Profit =", total_profit)


# Main Program

n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):

    weight = float(input("Enter weight of item " + str(i + 1) + ": "))
    profit = float(input("Enter profit of item " + str(i + 1) + ": "))

    weights.append(weight)
    profits.append(profit)

capacity = float(input("Enter capacity of knapsack: "))

fractional_knapsack(weights, profits, capacity)
