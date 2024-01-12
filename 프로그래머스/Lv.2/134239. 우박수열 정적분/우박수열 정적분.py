def solution(k, ranges):
    answer = []
    count_n = 0
    coor_y = [k]
    area = []

    while k != 1:
        count_n += 1
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        coor_y.append(k)
        
    for r in ranges:
        r[1] += count_n 
    
    for i in range(1, len(coor_y)):
        area.append((coor_y[i-1] + coor_y[i]) / 2)

    for r in ranges:
        if r[0] > r[1]:
            answer.append(-1)
        else:
            integral = sum(area[r[0]:r[1]])
            answer.append(integral)

    return answer
