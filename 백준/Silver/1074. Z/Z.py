N, r, c = map(int, input().split())
result = 0
for i in range(N, 0, -1):
    mask = 1 << (i - 1)
    if r & mask and c & mask:       
        result += 3 * (mask ** 2)
    elif r & mask:                 
        result += 2 * (mask ** 2)
    elif c & mask:                
        result += mask ** 2
print(result)