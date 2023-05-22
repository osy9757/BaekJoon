def solution(n, lost, reserve):
    final_lost = [num for num in lost if num not in reserve]
    final_reserve = [num for num in reserve if num not in lost]
    
    for num in sorted(final_reserve):
        if (num-1) in final_lost:
            final_lost.remove((num-1))
        elif (num+1) in final_lost:
            final_lost.remove((num+1))
    answer = n - len(final_lost)
    return answer
