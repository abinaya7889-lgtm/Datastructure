from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

source = "A"
destination = "F"

queue = deque([[source]])
visited = []

while queue:
    path = queue.popleft()
    node = path[-1]

    if node == destination:
        print("Shortest Route:", " -> ".join(path))
        break

    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)