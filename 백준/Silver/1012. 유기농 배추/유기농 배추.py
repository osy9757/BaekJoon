from collections import deque

def dfs(grid, i, j):
    queue = deque([(i, j)])
    while queue:
        i, j = queue.pop()
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            continue
        grid[i][j] = 0
        # 인접 셀을 큐에 추가
        queue.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])


def count_grid(grid, M, N):
    count = 0
    for i in range(N):  
        for j in range(M):  
            if grid[i][j] == 1:
                count += 1
                dfs(grid, i, j)
    return count

T = int(input())
answer = []
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]

    for _ in range(K):
        r, c = map(int, input().split())
        grid[c][r] = 1
    
    answer.append(count_grid(grid, M, N))

for ans in answer:
    print(ans)
