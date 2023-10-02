import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]

jewels.sort(key=lambda x: x[0])

bags.sort()

ans = 0
idx = 0
available_jewels = []

for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(available_jewels, -jewels[idx][1])
        idx += 1

    if available_jewels:
        ans -= heapq.heappop(available_jewels)

print(ans)
