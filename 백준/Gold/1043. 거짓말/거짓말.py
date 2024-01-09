N, M = map(int,input().split())
known_truth_numbers = list(map(int,input().split()))
numbers_list = [False] * (N+1)
for mem in known_truth_numbers[1:]:
  numbers_list[mem] = True
count_lie = 0

party_member = [list(map(int,input().split())) for _ in range(M)]

for _ in range(M):
  for member in party_member:
    for mem in member[1:]:
      if numbers_list[mem] == True:
        for mem in member[1:]:
          numbers_list[mem] = True
        break

for member in party_member:
  for mem in member[1:]:
    if numbers_list[mem] == True:
      break
  else:
    count_lie += 1

print(count_lie)