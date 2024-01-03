def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        diffX = startX-ball[0] # X차이
        diffY = startY-ball[1] # Y차이
        
        left = (startX+ball[0])**2 + (diffY**2)          # 왼쪽 쿠션
        right = ((m-startX)+(m-ball[0]))**2 + (diffY**2) # 오른쪽 쿠션
        top = (diffX**2) + ((n-startY)+(n-ball[1]))**2   # 위쪽 쿠션
        bottom = (diffX**2) + (startY+ball[1])**2        # 아래쪽 쿠션
        
        if diffX == 0: # X축 같은 선상일 때
            if diffY > 0: # 아래쪽 방향 쿠션 안됨
                res = min(left, right, top)        
            else : # 위쪽 방향 쿠션 안됨
                res = min(left, right, bottom)    
                
        elif diffY == 0: # Y축 같은 선상일 때
            if diffX > 0: # 왼쪽 쿠션 안됨
                res = min(right, top, bottom)        
            else : # 오른쪽 쿠션 안됨
                res = min(left, top, bottom)      
                
        else: # 같은 축 없을 때
            res = min(left, right, top, bottom)
            
        # 결과 append
        answer.append(res)
    return answer