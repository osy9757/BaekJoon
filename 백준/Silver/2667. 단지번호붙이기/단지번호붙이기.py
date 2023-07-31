from collections import deque

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for nx, ny in ((x + dx[i], y + dy[i]) for i in range(4)):
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

cnt = [bfs(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
cnt.sort()

print(len(cnt))
print(*cnt, sep='\n')
