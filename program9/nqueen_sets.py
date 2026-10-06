def solve_n_queens(n):
    board = []

    columns = set()
    diagonal1 = set()
    diagonal2 = set()

    def backtrack(row):
        if row == n:
            print("Solution:")
            for r in board:
                print(" ".join(r))
            print()
            return

        for col in range(n):
            if col in columns:
                continue

            if row - col in diagonal1:
                continue

            if row + col in diagonal2:
                continue

            row_data = ["."] * n
            row_data[col] = "Q"
            board.append(row_data)

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            backtrack(row + 1)

            board.pop()
            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

    backtrack(0)


n = int(input("Enter N: "))
solve_n_queens(n)