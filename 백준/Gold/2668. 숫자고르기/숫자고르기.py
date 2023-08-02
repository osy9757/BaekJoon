N = int(input())
graph = [int(input()) for _ in range(N)]

result = []
for i in range(N):
    if graph[i] == i + 1:
        result.append(i)
        continue
    visited = [False] * N
    loop = []
    current = i
    while not visited[current]:
        visited[current] = True
        loop.append(current)
        current = graph[current] - 1
        if current == i:
            result += loop
            break

result = sorted(set(result))
print(len(result))
for number in result:
    print(number + 1)
