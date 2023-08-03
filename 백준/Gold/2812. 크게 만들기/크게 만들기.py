N, K = map(int, input().strip().split())
number = input().strip()

result = []
for num in number:
    while K > 0 and result and result[-1] < num:
        result.pop()
        K -= 1
    result.append(num)

while K > 0:
    result.pop()
    K -= 1

print(''.join(result))
