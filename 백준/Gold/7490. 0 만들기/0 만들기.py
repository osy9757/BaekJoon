def solve(n, pos, current_expression, current_value, last_value):
    if pos > n:
        if current_value == 0:
            print(current_expression)
        return
    merged_value = 10*last_value + (pos if last_value > 0 else -pos)
    solve(n, pos + 1, current_expression + ' ' + str(pos), current_value - last_value + merged_value, merged_value)
    solve(n, pos + 1, current_expression + '+' + str(pos), current_value + pos, pos)
    
    solve(n, pos + 1, current_expression + '-' + str(pos), current_value - pos, -pos)
    
    

T = int(input())  
for _ in range(T):
    N = int(input())
    solve(N, 2, '1', 1, 1)
    if _ != T - 1:
        print()
