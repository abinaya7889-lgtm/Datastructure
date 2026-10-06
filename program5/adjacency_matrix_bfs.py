# BFS using Adjacency Matrix

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

visited = [False] * 5
queue = [0]
visited[0] = True

print("BFS Traversal:")

while queue:
    vertex = queue.pop(0)
    print(vertex, end=" ")

    for i in range(5):
        if graph[vertex][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)