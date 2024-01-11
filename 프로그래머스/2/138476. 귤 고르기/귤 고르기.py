def solution(k, tangerine):
    answer = 0
    size_count = {}
    
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1

    count_size = [num for num in size_count.values()]
    count_size.sort(reverse = True)
    for num in count_size:
        if k > 0:
            k -= num
            answer += 1
        else:
            break
    return answer