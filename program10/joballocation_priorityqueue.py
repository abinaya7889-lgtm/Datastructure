import heapq

def job_allocation(cost):
    n = len(cost)

    pq = []
    heapq.heappush(pq, (0, 0, [], set()))

    best_cost = float("inf")
    best_assignment = []

    while pq:
        current_cost, employee, assignment, used = heapq.heappop(pq)

        if employee == n:
            if current_cost < best_cost:
                best_cost = current_cost
                best_assignment = assignment
            continue

        if current_cost >= best_cost:
            continue

        for task in range(n):
            if task not in used:

                new_cost = current_cost + cost[employee][task]

                if new_cost < best_cost:
                    new_assignment = assignment + [task]
                    new_used = used | {task}

                    heapq.heappush(
                        pq,
                        (
                            new_cost,
                            employee + 1,
                            new_assignment,
                            new_used
                        )
                    )

    print("Minimum Cost:", best_cost)
    print("Optimal Allocation:")

    for i in range(n):
        print(
            "Employee", i + 1,
            "-> Task", best_assignment[i] + 1
        )


cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

job_allocation(cost)