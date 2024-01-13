def solution(order):
    stack = []
    current_box = 1
    loaded_boxes = 0

    for desired_box in order:
        while current_box <= len(order) and current_box <= desired_box:
            stack.append(current_box)
            current_box += 1

        while stack and stack[-1] == order[loaded_boxes]:
            stack.pop()
            loaded_boxes += 1

    return loaded_boxes
