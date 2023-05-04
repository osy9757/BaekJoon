N = int(input())
score = [int(input()) for _ in range(N)]
if N <= 2:
    print(sum(score))
else:
    total = score[:1]
    total.append(score[0] + score[1])
    total.append(max(total[0]+score[2],score[1]+score[2]))
    for i in range(3,N):
        total.append(max(total[i-2]+score[i], total[i-3]+score[i-1]+score[i]))
    print(total[-1])