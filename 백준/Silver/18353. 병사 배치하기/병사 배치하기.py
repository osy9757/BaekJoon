N = int(input())
soldiers = list(map(int, input().split()))
count = [1] * N

for i in range(N):
    count[i] = max([count[j] for j, num in enumerate(soldiers[:i]) if num > soldiers[i]], default=0) + 1

print(N - max(count))
