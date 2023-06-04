def solution(operations):
    queue = []

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == 'I':
            queue.append(value)

        elif command == 'D':
            if value == 1 and queue:
                queue.remove(max(queue))
            elif value == -1 and queue:
                queue.remove(min(queue))
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]
