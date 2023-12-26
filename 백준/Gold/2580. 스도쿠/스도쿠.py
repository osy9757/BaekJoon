def find_empty_cells(graph):
    return [(i, j) for i in range(9) for j in range(9) if graph[i][j] == 0]

def is_valid_move(graph, row, col, num):
    for i in range(9):
        if graph[row][i] == num or graph[i][col] == num or graph[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def solve_sudoku(graph, empty_cells):
    if not empty_cells:
        return True
    row, col = empty_cells[0]

    for num in range(1, 10):
        if is_valid_move(graph, row, col, num):
            graph[row][col] = num
            if solve_sudoku(graph, empty_cells[1:]):
                return True
            graph[row][col] = 0
    return False

graph = [list(map(int, input().split())) for _ in range(9)]
empty_cells = find_empty_cells(graph)

if solve_sudoku(graph, empty_cells):
    for row in graph:
        print(*row)
