from collections import deque

def solution(x, y, n):
    deq = deque([(x, 0)])
    visited = set()  

    while deq:
        current, count = deq.popleft()

        if current == y:
            return count

        if current in visited:
            continue
        visited.add(current)

        for next_val in (current + n, current * 2, current * 3):
            if next_val <= y and next_val not in visited:
                deq.append((next_val, count + 1))

    return -1
