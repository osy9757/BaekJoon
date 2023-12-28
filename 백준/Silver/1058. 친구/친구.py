N = int(input())
graph = [input() for _ in range(N)]

max_frined = 0

for i in range(N):
  friends = set()
  Nums = [k for k in range(N) if graph[i][k] == 'Y']
  friends.update(Nums)

  for num in Nums:
    friends.update(k for k in range(N) if graph[num][k] == 'Y')
  
  max_frined=max(max_frined,len(friends) - 1)
  
print(max_frined)