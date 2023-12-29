from itertools import combinations

N = int(input())
startlink = [list(map(int,input().split())) for _ in range(N)]

min_diff = 1e9

start_team = list(combinations(range(N),N//2))
link_team = [list(set(range(N)) - set(mem)) for mem in start_team]

for i in range(len(start_team) // 2):
    start_score, link_score = 0, 0
    for n in range(N // 2):
        for m in range(N // 2):
            start_score += startlink[start_team[i][n]][start_team[i][m]]
            link_score += startlink[start_team[-i-1][n]][start_team[-i-1][m]]
    min_diff = min(min_diff, abs(start_score - link_score))

    if min_diff == 0:
        break

print(min_diff)