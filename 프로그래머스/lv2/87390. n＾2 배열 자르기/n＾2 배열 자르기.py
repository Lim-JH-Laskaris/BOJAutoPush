def solution(n, left, right):
    lx,ly = left%n,left//n
    rx,ry = right%n,right//n
    answer = []
    line = [ly+1]*ly+list(range(ly+1,n+1))
    if ly == ry : answer = line[lx:rx+1]
    else : 
        answer = line[lx:]
        for i in range(ly+1,ry):
            line = [i+1]*i+list(range(i+1,n+1))
            answer = answer+line
        line = [ry+1]*ry+list(range(ry+1,n+1))
        answer = answer+line[:rx+1]  
    return answer