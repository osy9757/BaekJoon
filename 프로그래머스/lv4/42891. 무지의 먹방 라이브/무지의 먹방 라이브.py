def solution(food_times, k):
    n = len(food_times)
    food_times = list(enumerate(food_times, start=1))  # add indices
    food_times.sort(key=lambda x: x[1])  # sort by time

    previous = 0
    for i, (index, time) in enumerate(food_times):
        diff = time - previous
        if diff != 0:
            spend = diff * (n - i)  # time spend for this round
            if spend <= k:
                k -= spend
                previous = time
            else:  # if k < spend, find the food to eat next
                k %= (n - i)
                food_times = sorted(food_times[i:], key=lambda x: x[0])  # sort by index
                return food_times[k][0]  # return the index of the next food
    return -1  # if there is no more food left
