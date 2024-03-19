def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        add_case = dfs(index + 1, current_sum + numbers[index])
        subtract_case = dfs(index + 1, current_sum - numbers[index])
        
        return add_case + subtract_case
    
    answer = dfs(0, 0)
    return answer