N = int(input())
points = [tuple(map(int, input().strip().split())) for _ in range(N)]

x_count = {}
y_count = {}

for x, y in points:
    if x not in x_count:
        x_count[x] = 0
    if y not in y_count:
        y_count[y] = 0

    x_count[x] += 1
    y_count[y] += 1

count = 0
for x, y in points:
    count += (x_count[x] - 1) * (y_count[y] - 1)

print(count)
