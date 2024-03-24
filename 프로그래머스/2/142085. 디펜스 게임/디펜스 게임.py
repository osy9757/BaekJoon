import heapq
def solution(n, k, enemy):
    e = 0
    h = []
    for i in range(len(enemy)):
        e += enemy[i]
        heapq.heappush(h,-enemy[i])
        if e > n:
            if k == 0:
                return i
            e += heapq.heappop(h)
            k -= 1
    
    return i+1