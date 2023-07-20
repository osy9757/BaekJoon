import heapq

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

total = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sums = a + b
    total += sums
    heapq.heappush(cards, sums)

print(total)
