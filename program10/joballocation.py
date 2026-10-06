def branch_and_bound(cost, n):
    best_cost = float("inf")
    best_assignment = []

    def solve(employee, used, total, assignment):
        nonlocal best_cost, best_assignment

        if employee == n:
            if total < best_cost:
                best_cost = total
                best_assignment = assignment[:]
            return

        if total >= best_cost:
            return

        for task in range(n):
            if not used[task]:

                used[task] = True
                assignment.append(task)

                solve(
                    employee + 1,
                    used,
                    total + cost[employee][task],
                    assignment
                )

                assignment.pop()
                used[task] = False

    solve(0, [False] * n, 0, [])

    return best_cost, best_assignment


n = int(input("Enter number of employees/tasks: "))

cost = []

print("Enter the cost matrix:")

for i in range(n):
    row = list(map(int, input(
        f"Employee {i + 1}: "
    ).split()))
    cost.append(row)

minimum_cost, assignment = branch_and_bound(cost, n)

print("\nOptimal Job Allocation")
print("----------------------")

for i in range(n):
    print(
        "Employee", i + 1,
        "-> Task", assignment[i] + 1,
        "Cost =", cost[i][assignment[i]]
    )

print("\nMinimum Total Cost:", minimum_cost)