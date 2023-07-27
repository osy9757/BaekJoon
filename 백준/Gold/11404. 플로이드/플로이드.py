n = int(input())
m = int(input())

INF = 1e9

graph = [[INF if i !=j else 0 for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = 0 if i == j else min(graph[i][j], graph[i][k] + graph[k][j])
                
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()