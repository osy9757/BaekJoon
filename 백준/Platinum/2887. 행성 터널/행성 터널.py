import sys
import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution():
    n = int(sys.stdin.readline())
    parent = [0] * n
    edges = []
    result = 0

    x = []
    y = []
    z = []

    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        x.append((a, i))
        y.append((b, i))
        z.append((c, i))
        parent[i] = i

    x.sort()
    y.sort()
    z.sort()

    for i in range(n - 1):
        heapq.heappush(edges, (x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
        heapq.heappush(edges, (y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
        heapq.heappush(edges, (z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

    while edges:
        cost, a, b = heapq.heappop(edges)
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    print(result)

solution()
