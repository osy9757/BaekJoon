def update(command, board, merged):
    if len(command) == 4:
        r, c, value = int(command[1])-1, int(command[2])-1, command[3]
        x, y = merged[r][c]
        board[x][y] = value
    elif len(command) == 3:
        value1, value2 = command[1], command[2]
        for i in range(50):
            for j in range(50):
                if board[i][j] == value1:
                    board[i][j] = value2

def merge(command, board, merged):
    r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
    x1, y1 = merged[r1][c1]
    x2, y2 = merged[r2][c2]
    if board[x1][y1] == "EMPTY":
        board[x1][y1] = board[x2][y2]
    for i in range(50):
        for j in range(50):
            if merged[i][j] == (x2, y2):
                merged[i][j] = (x1, y1)

def unmerge(command, board, merged):
    r, c = int(command[1])-1, int(command[2])-1
    x, y = merged[r][c]
    tmp = board[x][y]
    for i in range(50):
        for j in range(50):
            if merged[i][j] == (x, y):
                merged[i][j] = (i, j)
                board[i][j] = "EMPTY"
    board[r][c] = tmp

def Print(command, board, merged, answer):
    r, c = int(command[1])-1, int(command[2])-1
    x, y = merged[r][c]
    answer.append(board[x][y])

def solution(commands):
    board = [["EMPTY"] * 50 for _ in range(50)]
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    answer = []
    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            update(command, board, merged)
        elif command[0] == 'MERGE':
            merge(command, board, merged)
        elif command[0] == 'UNMERGE':
            unmerge(command, board, merged)
        elif command[0] == 'PRINT':
            Print(command, board, merged, answer)
    return answer