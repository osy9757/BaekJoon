def solution(storey):
    answer = 0
    while storey:
        last_num = storey % 10
        if last_num > 5 or (storey%100 > 50 and last_num>=5):
            answer += 10 - last_num
            storey += 10
            storey //= 10
        else:
            answer += last_num
            storey //= 10            
    return answer