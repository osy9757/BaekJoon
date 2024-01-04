def solution(boards):
    answer = -1
    count_O, count_X = 0, 0
    bingo_O, bingo_X = 0, 0
    for board in boards:
        count_O += board.count('O')
        count_X += board.count('X')
        
    sub_boards = [[boards[j][i] for j in range(len(boards))] for i in range(len(boards[0]))]
    
    for board in boards:
        if board.count('O') == 3:
            bingo_O = 1
        if board.count('X') == 3:
            bingo_X = 1
    
    for board in sub_boards:
        if board.count('O') == 3:
            bingo_O = 1
        if board.count('X') == 3:
            bingo_X = 1
            
    diagonal1 = [boards[i][i] for i in range(len(boards))]
    diagonal2 = [boards[i][len(boards)-1-i] for i in range(len(boards))]
    if diagonal1.count('O') == 3 or diagonal2.count('O') == 3:
        bingo_O = 1
    if diagonal1.count('X') == 3 or diagonal2.count('X') == 3:
        bingo_X = 1
        
        
    if count_O-count_X!=0 and count_O-count_X!=1:
        return 0
    if bingo_O == 1 and bingo_X == 1:
        return 0
    if bingo_O == 1 and count_O-count_X!=1:
        return 0
    if bingo_X == 1 and count_O-count_X!=0:
        return 0
    
    return 1