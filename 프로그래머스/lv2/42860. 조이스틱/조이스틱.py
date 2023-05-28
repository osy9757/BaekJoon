def solution(name):
    length = len(name)

    # 상하 조작
    count = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]

    # 좌우 조작
    move = length - 1
    for i in range(length):
        # 연속되는 A의 개수 확인
        index = i + 1
        while index < length and name[index] == 'A':
            index += 1

        # 순서대로 가는 것과, 뒤로 돌아가는 것 중 이동수가 적은 것을 선택
        move = min(move, i * 2 + length - index)
        # BBBBAAAAAAAB와 같이, 처음부터 뒷부분을 먼저 입력하는 것이 더 빠른 경우 고려
        move = min(move, (length - index) * 2 + i)

    return sum(count) + move
