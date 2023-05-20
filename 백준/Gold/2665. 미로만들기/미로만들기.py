import heapq

n = int(input())
arr = [[0]*n for _ in range(n)]
dist = [[float('inf')]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# Input
for i in range(n):
    line = input().strip()
    for j in range(n):
        arr[i][j] = 1 - int(line[j])

# Dijkstra
queue = []
heapq.heappush(queue, (0, (0, 0)))
dist[0][0] = 0
while queue:
    cost, (x, y) = heapq.heappop(queue)
    if cost > dist[y][x]:
        continue
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if dist[y][x] + arr[ny][nx] < dist[ny][nx]:
            dist[ny][nx] = dist[y][x] + arr[ny][nx]
            heapq.heappush(queue, (dist[ny][nx], (nx, ny)))

# Output
print(dist[n-1][n-1])
