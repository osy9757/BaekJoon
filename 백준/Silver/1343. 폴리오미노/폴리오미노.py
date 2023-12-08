board = input()
board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')
print(-1 if 'X' in board else board)