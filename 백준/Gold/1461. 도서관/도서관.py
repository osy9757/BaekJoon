N, M = map(int,input().split())
books = list(map(int, input().split()))

positive = sorted([book for book in books if book > 0], reverse=True)
negative = sorted([book for book in books if book < 0])

steps = 0

for i in range(0, len(positive), M):
    steps += positive[i] * 2

for i in range(0, len(negative), M):
    steps += abs(negative[i]) * 2

if positive and negative:
    steps -= max(positive[0], abs(negative[0]))
elif positive:
    steps -= positive[0]
elif negative:
    steps -= abs(negative[0])

print(steps)
