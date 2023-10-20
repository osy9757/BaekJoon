import copy                


def solution(numbers, target):
    answer = 0
    temps = [0]
    results = []
    
    for num in numbers:
        results = []
        for temp in temps:
            results.append(temp+num)
            results.append(temp-num)
        temps = copy.deepcopy(results)
    return results.count(target)