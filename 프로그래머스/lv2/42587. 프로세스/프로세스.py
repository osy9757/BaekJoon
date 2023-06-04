def solution(priorities, location):
    answer = 0
    priorities = [(i, v) for i, v in enumerate(priorities)]
    
    while priorities:
        value = priorities.pop(0)
        if priorities and value[1] < max(p[1] for p in priorities):
            priorities.append(value)
        else:
            answer += 1
            if value[0] == location:
                return answer