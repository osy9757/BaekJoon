n = int(input())
arr = sorted(map(int, input().split()))

for i in range(1, n):
    arr[i] += arr[i-1]

print(sum(arr))