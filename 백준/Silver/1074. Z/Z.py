N, r, c = map(int, input().split())

result = 0
for i in range(N, 0, -1):
    mask = 1 << (i - 1)  # 현재 확인하고자 하는 비트의 위치를 mask로 표시
    if r & mask and c & mask:       # 4사분면
        result += 3 * (mask ** 2)
    elif r & mask:                  # 3사분면
        result += 2 * (mask ** 2)
    elif c & mask:                  # 2사분면
        result += mask ** 2
    # 1사분면일 경우는 아무것도 더하지 않습니다.

print(result)
