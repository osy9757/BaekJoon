def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)
    left = lost.copy()
    for num in lost:
        if num in reserve:
            reserve.remove(num)
            left.remove(num)
    lost = left.copy()
    for num in lost:
        if (num-1) in reserve:
            left.remove(num)
            reserve.remove((num-1))
        elif (num+1) in reserve:
            left.remove(num)
            reserve.remove((num+1))
    answer = n - len(left)
    return answer
