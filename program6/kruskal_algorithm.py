edges = [
    (2, 'A', 'B'),
    (3, 'B', 'C'),
    (6, 'A', 'D'),
    (8, 'B', 'D'),
    (5, 'B', 'E'),
    (7, 'C', 'E'),
    (9, 'D', 'E')
]

edges.sort()

parent = {}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent[find(a)] = find(b)

for edge in edges:
    parent[edge[1]] = edge[1]
    parent[edge[2]] = edge[2]

cost = 0

print("Edges in MST:")

for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, ":", weight)
        cost += weight

print("Minimum Cost:", cost)