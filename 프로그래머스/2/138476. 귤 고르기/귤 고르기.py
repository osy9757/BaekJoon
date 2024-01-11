def solution(k, tangerine):
    answer = 0
    size_count = {}
    
    for size in tangerine:
        size_count[size] = size_count.get(size, 0) + 1

    count_size = sorted(size_count.values(), reverse=True)
    
    for num in count_size:
        if k > 0:
            k -= num
            answer += 1
        else:
            break
    return answer