def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i in range(row_begin - 1, row_end):
        S_i = sum(x % (i + 1) for x in data[i])
        answer ^= S_i

    return answer