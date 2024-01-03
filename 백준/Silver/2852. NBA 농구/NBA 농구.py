N = int(input())
goals = [[int(goal[0]), int(goal[1].split(':')[0])*60 + int(goal[1].split(':')[1])] for goal in (input().split() for _ in range(N))]
score = [0,0]
times = [0,0]
s_time = goals[0][1]
for goal in goals:
  if score[0] != score[1]:
    times[score.index(max(score))] += goal[1]-s_time
  s_time=goal[1]
  score[goal[0]-1] += 1
if score[0] != score[1]:
  times[score.index(max(score))] += 2880 - s_time

for time in times:
  print(f"{time//60:02d}:{time%60:02d}")