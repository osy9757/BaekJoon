def solution(book_time):
    answer = 0    
    book_time.sort(key=lambda x: x[0])
    book_time_minute = [ (int(s_time[:2])*60 + int(s_time[-2:]), int(e_time[:2])*60 + int(e_time[-2:])+10) 
                        for s_time, e_time in book_time]
    for i in range(0,len(book_time_minute)):
        count = 0
        for j in range(i-1,-1,-1):
            if book_time_minute[i][0] < book_time_minute[j][1]:
                count+=1
        answer = max(answer,count+1)
    return answer