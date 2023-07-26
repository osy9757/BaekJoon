N = int(input())
bricks = [(int(area), int(height), int(weight), i+1) for i in range(N) for area, height, weight in [input().split()]]

bricks.sort()

dp = [0] * N  
trace = [-1] * N 
for i in range(N):
    dp[i] = bricks[i][1]  
    for j in range(i):
        if bricks[j][2] < bricks[i][2] and dp[i] < dp[j] + bricks[i][1]:
            dp[i] = dp[j] + bricks[i][1]
            trace[i] = j

max_height_idx = dp.index(max(dp))

result = []
while max_height_idx != -1:
    result.append(bricks[max_height_idx][3])
    max_height_idx = trace[max_height_idx]

print(len(result))
for brick in reversed(result):
    print(brick)
