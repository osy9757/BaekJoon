import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]

houses.sort()

start = 1
end = houses[-1] - houses[0]

dist = 0

while (start <= end):
    mid = (start+end)//2
    point = houses[0]
    count = 1

    for i in range(1, N):
        if houses[i] >= point + mid:
            count += 1
            point = houses[i]

    if count >= C:
        start = mid + 1
        dist = mid
    else:
        end = mid - 1

print(dist)
