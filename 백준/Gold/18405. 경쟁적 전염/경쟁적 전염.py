from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        virus, s, x, y = q.popleft()
        if s == target_s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s + 1, nx, ny))

n, k = map(int, input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

target_s, target_x, target_y = map(int, input().split())

data.sort()
q = deque(data)

bfs()

print(graph[target_x - 1][target_y - 1])
