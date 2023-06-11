def solution(n, results):
    wins = [[] for _ in range(n+1)]
    loses = [[] for _ in range(n+1)]
    
    for win, lose in results:
        wins[win].append(lose)
        loses[lose].append(win)
    
    for i in range(1,n+1):
        for winner in loses[i]: 
            for player in wins[i]:
                if player not in wins[winner]:
                    wins[winner].append(player)
        for loser in wins[i]: 
            for player in loses[i]:
                if player not in loses[loser]:
                    loses[loser].append(player)
    

    answer = len([i for i in range(1,n+1) if len(wins[i])+len(loses[i]) == n-1])
    return answer