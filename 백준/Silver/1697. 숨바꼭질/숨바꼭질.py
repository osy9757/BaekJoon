from collections import deque

N, K = map(int,input().split())
dots = [0] * 100001
q = deque()
q.append(N)
while q:
    x = q.popleft()
    if x == K:
        print(dots[K])
        break
    for i in (x-1,x+1,x*2):
        if 0 <= i < len(dots) and not dots[i]:
            dots[i] = dots[x] + 1
            q.append(i)