graph = {'A': {'B': 2, 'C': 4}, 'B': {'C': 1, 'D': 7}, 'C': {'D': 3}, 'D': {}}
dist = {'A': 0, 'B': 999, 'C': 999, 'D': 999}
visited = []
while len(visited) < len(graph):
    u = min((n for n in dist if n not in visited), key=dist.get)
    visited.append(u)
    for v in graph[u]:
        dist[v] = min(dist[v], dist[u] + graph[u][v])
print("Shortest distance:", dist)