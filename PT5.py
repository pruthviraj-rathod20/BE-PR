
# N-Queens Problem using Backtracking

def solve_n_queens(n):

    board = [[0] * n for _ in range(n)]

    # Check whether placing a queen is safe
    def is_safe(row, col):

        # Check same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False

            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1

        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False

            i -= 1
            j += 1

        return True

    # Backtracking function
    def backtrack(row):

        if row == n:
            return True

        for col in range(n):

            if is_safe(row, col):

                board[row][col] = 1

                if backtrack(row + 1):
                    return True

                # Backtrack
                board[row][col] = 0

        return False

    # Find solution
    if backtrack(0):

        print("\nFinal 8-Queens Matrix:")

        for row in board:
            print(*row)

    else:
        print("Solution does not exist")


# Main Program

n = int(input("Enter number of Queens: "))

if n == 8:
    solve_n_queens(n)
else:
    print("Please enter 8")
