import sys

N, S, M = map(int,input().split())
V = list(map(int,input().split()))

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for i, v in enumerate(V):
    dp[i+1] = [dp[i][j-v]*(j>=v) or (j+v<=M and dp[i][j+v]) for j in range(M+1)]

result = next((i for i in reversed(range(M+1)) if dp[-1][i]), -1)
print(result)