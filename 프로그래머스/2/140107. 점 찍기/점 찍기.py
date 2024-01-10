import math

def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        max_y = math.sqrt(d**2 - i**2)
        answer += max_y//k + 1
    return answer