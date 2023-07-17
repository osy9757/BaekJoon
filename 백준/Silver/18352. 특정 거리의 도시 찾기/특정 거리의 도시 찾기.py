from collections import deque
import sys

N, M, K, X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    
min_dist = [N] * (N+1)
min_dist[X] = 0

q = deque([X])
while q:
    c_position = q.popleft()
    for n_position in graph[c_position]:
        if min_dist[n_position] > min_dist[c_position] + 1:
            min_dist[n_position] = min_dist[c_position] + 1
            q.append(n_position)

flag = False
for i in range (1,N+1):
    if min_dist[i] == K:
        print(i)
        flag = True

if flag == False:
    print(-1)