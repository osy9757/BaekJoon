def dfs(start, graph, visited, result):
    loop = []
    current = start
    while not visited[current]:
        visited[current] = True
        loop.append(current)
        current = graph[current] - 1
        if current == start:
            result += loop
            break

N = int(input())
graph = [int(input()) for _ in range(N)]

result = []
for i in range(N):
    if graph[i] == i + 1:
        result.append(i)
        continue
    visited = [False] * N
    dfs(i, graph, visited, result)

result = list(set(result))
result.sort()

print(len(result))
for number in result:
    print(number + 1)
