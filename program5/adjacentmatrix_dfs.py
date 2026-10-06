# DFS using Adjacency Matrix

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0]
]

visited = [False] * 5

def dfs(vertex):
    visited[vertex] = True
    print(vertex, end=" ")

    for i in range(5):
        if graph[vertex][i] == 1 and not visited[i]:
            dfs(i)

print("DFS Traversal:")
dfs(0)