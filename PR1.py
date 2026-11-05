import time

# Non-Recursive Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter number of terms: "))

# Non-Recursive Execution Time
start = time.perf_counter()

print("\nNon-Recursive Fibonacci Series:")
fibonacci_iterative(n)

end = time.perf_counter()
iterative_time = end - start

# Recursive Execution Time
start = time.perf_counter()

print("\n\nRecursive Fibonacci Series:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

end = time.perf_counter()
recursive_time = end - start

# Execution Time
print("\n\nExecution Time:")
print("Non-Recursive Time:", iterative_time, "seconds")
print("Recursive Time:", recursive_time, "seconds")

# Time Complexity
print("\nTime Complexity:")
print("Non-Recursive: O(n)")
print("Recursive: O(2^n)")

# Space Complexity
print("\nSpace Complexity:")
print("Non-Recursive: O(1)")
print("Recursive: O(n)")