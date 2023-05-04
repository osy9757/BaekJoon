N = int(input())
Num = [int(input()) for _ in range(N)]

Value = [1,2,4]

for i in range(3,max(Num)):
    Value.append(Value[i-1]+Value[i-2]+Value[i-3])

for i in range(N):
    print(Value[Num[i]-1])