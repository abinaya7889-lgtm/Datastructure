def job_allocation(cost):
    n = len(cost)
    best_cost = float("inf")
    best_assignment = []

    def branch(employee, assigned, current_cost, assignment):
        nonlocal best_cost, best_assignment

        if employee == n:
            if current_cost < best_cost:
                best_cost = current_cost
                best_assignment = assignment[:]
            return

        for task in range(n):
            if task not in assigned:
                new_cost = current_cost + cost[employee][task]

                if new_cost < best_cost:
                    assigned.add(task)
                    assignment.append(task)

                    branch(employee + 1, assigned, new_cost, assignment)

                    assignment.pop()
                    assigned.remove(task)

    branch(0, set(), 0, [])

    print("Minimum Cost:", best_cost)
    print("Job Allocation:")

    for i in range(n):
        print("Employee", i + 1, "-> Task", best_assignment[i] + 1)


cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

job_allocation(cost)