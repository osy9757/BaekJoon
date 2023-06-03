def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i-1] != arr[i] or i == 0 :
            answer.append(arr[i])
    return answer
