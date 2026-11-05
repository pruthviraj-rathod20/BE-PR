
# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Display DP table
    print("\nDP Table:")

    for row in dp:
        print(row)

    # Display maximum profit
    print("\nMaximum Profit:", dp[n][capacity])

    # Find selected objects
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(i)
            w -= weights[i - 1]

    selected.reverse()

    # Display selected objects
    print("\nSelected Objects:")

    for i in selected:
        print("Object", i, "- Weight:", weights[i - 1],
              "Profit:", profits[i - 1])

    # Display selection (0/1)
    print("\nSelection (0 = No, 1 = Yes):")

    for i in range(1, n + 1):
        print("Object", i, ":",
              1 if i in selected else 0)


# Main Program

weights = [2, 3, 4, 5]
profits = [3, 4, 5, 6]
capacity = 7

print("Object\tWeight\tProfit")

for i in range(len(weights)):
    print(i + 1, "\t", weights[i], "\t", profits[i])

print("Knapsack Capacity:", capacity)

knapsack(weights, profits, capacity)
