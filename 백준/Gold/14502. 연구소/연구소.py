from itertools import combinations
from collections import deque
import sys
import copy

def bfs():
    global max_value
    copied_board = copy.deepcopy(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for virus in virus_position:
        queue = deque([virus])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and copied_board[nx][ny] == 0:
                    copied_board[nx][ny] = 2
                    queue.append([nx, ny])
    count = sum([row.count(0) for row in copied_board])
    max_value = max(max_value, count)

n, m = map(int, sys.stdin.readline().split())
board = []
virus_position = []
empty_position = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    for j in range(m):
        if row[j] == 2:
            virus_position.append([i, j])
        elif row[j] == 0:
            empty_position.append([i, j])

max_value = 0
for walls in combinations(empty_position, 3):
    for x, y in walls:
        board[x][y] = 1
    bfs()
    for x, y in walls:
        board[x][y] = 0

print(max_value)
