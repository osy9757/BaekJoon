def binary(lst, N):
    start, end = 1, max(lst)
    while start <= end:
        mid = (start + end) // 2
        total = 0 
        for l in lst:
            total += l // mid
        if total >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
print(binary(lst, N))