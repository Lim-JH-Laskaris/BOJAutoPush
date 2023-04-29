def is_blocked(x,y,a,b,i,j):
    """두 점을 이은 선이 같은가(깉은 선상에 위치하는가), 그리고 방향도 같은가(++ or --)
    두 가지가 성립하면 치는것이 불가능한 경우의 수."""
    if y-b != 0 and y-j != 0 :
        return (x-a)/(y-b)==(x-i)/(y-j) and (x-a)*(x-i)>=0 and (y-b)*(y-j)>=0
    else : 
        return (y-b)/(x-a)==(y-j)/(x-i) and (x-a)*(x-i)>=0 and (y-b)*(y-j)>=0

def solution(m, n, x, y, balls):
    """각 벽면에 거울을 단 것 처럼 하여 주위 8개의 평면을 새롭게 생성, 
    기본 시작점과 8개 거울평면 내 타깃 사이의 거리를 측정하고 최소값 반환"""
    answer = []
    for a,b in balls:
        targets = [[i,j] for i in [-a,a,2*m-a] for j in [-b,b,2*n-b]]
        targets.pop(4) # 타깃의 기본 위치 제외
        answer.append(min([(x-i)**2+(y-j)**2 
                           for i,j in targets if not is_blocked(x,y,a,b,i,j)]))   
    return answer