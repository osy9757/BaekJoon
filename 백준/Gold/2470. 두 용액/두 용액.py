import sys

N = int(input())
requids = list(map(int, sys.stdin.readline().strip().split()))
answer = [2000000001, 0]
requids.sort(key=abs)

for i in range(N-1):
    if abs(requids[i] + requids[i+1]) < abs(answer[0]):
        answer= [requids[i] + requids[i+1], i]


if requids[answer[1]]< requids[answer[1]+1]:
    print(requids[answer[1]], requids[answer[1]+1])
else:
    print(requids[answer[1]+1], requids[answer[1]])