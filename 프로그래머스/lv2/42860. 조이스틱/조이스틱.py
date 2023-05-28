def solution(name):
    length = len(name)

    count = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]

    move = length - 1
    for i in range(length):
        index = i + 1
        while index < length and name[index] == 'A':
            index += 1

        move = min(move, i * 2 + length - index)
        move = min(move, (length - index) * 2 + i)

    return sum(count) + move
