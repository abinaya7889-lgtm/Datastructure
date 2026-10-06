import heapq

tasks = []

heapq.heappush(tasks, (-3, "Study"))
heapq.heappush(tasks, (-5, "Project"))
heapq.heappush(tasks, (-1, "Email"))
heapq.heappush(tasks, (-4, "Assignment"))

print("Task Schedule:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print(task, "- Priority", -priority)