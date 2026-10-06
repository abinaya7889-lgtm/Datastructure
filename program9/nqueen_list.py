def solve(n):
    board = [-1] * n

    def safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False

            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def backtrack(row):
        if row == n:
            display()
            return

        for col in range(n):
            if safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    def display():
        print("Solution:")
        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

    backtrack(0)


n = int(input("Enter N: "))
solve(n)