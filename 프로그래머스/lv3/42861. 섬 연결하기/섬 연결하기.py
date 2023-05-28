def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    costs.sort(key = lambda x: x[2])
    

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost

    return answer
