import math

def solution(r1, r2):
    count = 0

    for x in range(1,r2+1):
        y2 = math.sqrt(r2**2-x**2) if r2>=x else 0
        y1 = math.sqrt(r1**2-x**2) if r1>=x else 0
        
        count += math.floor(y2)-math.ceil(y1)+1 
    return count*4