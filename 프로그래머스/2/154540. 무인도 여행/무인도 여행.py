from collections import deque

def sum_food(maps, visited,x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    total_food = 0
    
    deq = deque()
    deq.append((x,y))
    visited[x][y] = True
    while deq:
        x, y = deq.popleft()
        total_food += int(maps[x][y])
        
        for i in range(4):
            if 0<=x+dx[i]<len(maps) and 0<=y+dy[i]<len(maps[0]) and maps[x+dx[i]][y+dy[i]] != "X" and visited[x+dx[i]][y+dy[i]] == False:
                visited[x+dx[i]][y+dy[i]] = True
                deq.append((x+dx[i],y+dy[i]))
    return total_food, visited
    
def solution(maps):
    answer = []
    
    visited=[[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            foods = 0
            if maps[i][j] != 'X' and visited[i][j] == False:
                foods, visited = sum_food(maps, visited,i,j)
            
            if foods != 0:
                answer.append(foods)                
    
    if answer == []:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer