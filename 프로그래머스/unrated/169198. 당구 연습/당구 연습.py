def is_blocked(x,y,a,b,i,j):
    """ (x,y)(시작점)와 (a,b)(기존 타깃) 두 점을 이은 선과, 
    (x,y)와 (i,j)(거울 타깃- 거울 타깃은 아래 solution함수에 설명) 두 점을 이은 선에 대해,
    두 점을 이은 선이 같은가(깉은 선상에 위치하는가), 그리고 방향도 같은가(++ or --) 판단.
    두 가지가 성립하면, (x,y)에서 (i,j)로 가는 경로상에 (a,b) 가 막고 있기 때문에
    치는것이 불가능한 경우의 수를 나타낸다. 이때 True 반환"""
    if y-b != 0 and y-j != 0 :
        return (x-a)/(y-b)==(x-i)/(y-j) and (x-a)*(x-i)>=0 and (y-b)*(y-j)>=0
    else : 
        return (y-b)/(x-a)==(y-j)/(x-i) and (x-a)*(x-i)>=0 and (y-b)*(y-j)>=0

def solution(m, n, x, y, balls):
    """각 벽면에 거울을 단 것 처럼 하여 주위 8개의 평면을 새롭게 생성, 
    기본 시작점과 8개 거울평면 내 타깃 사이의 거리를 측정하고 최소값 반환"""
    answer = []
    for a,b in balls:
        targets = [[i,j] for i in [-a,a,2*m-a] for j in [-b,b,2*n-b]] # 거울 타깃
        targets.pop(4) # 타깃의 기본 위치 제외
        answer.append(min([(x-i)**2+(y-j)**2 
                           for i,j in targets if not is_blocked(x,y,a,b,i,j)]))   
                            # 거울 타깃 중, 불가능한 경우 제외
    return answer