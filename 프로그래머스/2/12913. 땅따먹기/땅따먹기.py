def solution(land):
    N = len(land)
    dp = [l[:] for l in land]
    
    for i in range(1,N):
        for j in range(4):
            dp[i][j] = max(dp[i - 1][k] for k in range(4) if k != j) + land[i][j]

    return max(dp[-1][:])