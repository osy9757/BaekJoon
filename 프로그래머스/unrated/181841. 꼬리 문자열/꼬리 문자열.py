def solution(str_list, ex):
    answer = ''.join(sub_str for sub_str in str_list if ex not in sub_str)
    return answer
