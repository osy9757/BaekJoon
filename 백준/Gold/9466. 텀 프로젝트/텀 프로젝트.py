import sys

def find_team(start, graph, visited):
    current = start
    path = []
    while not visited[current]:
        visited[current] = True
        path.append(current)
        current = graph[current]
    if current in path:
        return path[path.index(current):]
    return []

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    graph = [0] + list(map(int, sys.stdin.readline().strip().split()))

    visited = [False] * (N + 1)
    result = set()
    for i in range(1, N + 1):
        if not visited[i]:
            result.update(find_team(i, graph, visited))

    print(N - len(result))
