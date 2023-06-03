def solution(s):
    answer = True
    count_r, count_l = 0, 0
    for i in s:
        if i == '(':
            count_r += 1
        else:
            count_l += 1
        if count_l > count_r:
            return False
    
    if count_r != count_l:
        return False
        
    return True