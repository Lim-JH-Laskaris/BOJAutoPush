def solution(park, routes):
    i,j = 0,0 #시작 위치, 이후 현재위치 갱신
    direction = {'N':(-1, 0),
                 'S':( 1, 0),
                 'W':(0 ,-1),
                 'E':(0 , 1)} #이동방향
    pi,pj = len(park),len(park[0]) #공원 세로,가로 길이
    for p in park: #시작위치 탐색
        if 'S' in p : 
            j = p.find('S')
            break
        else : i += 1
    for r in routes: # 경로이동
        ti,tj = i,j #임시변수
        di,dj = direction[r[0]]
        n = int(r[2]) #걸음수. 9걸음 이하라는 조건이 있기 때문.
        while n : # 한걸음씩 늘려가며 장애물이 있는지 확인
            ni, nj = ti+di, tj+dj
            if ni>=0 and nj>=0 and ni<pi and nj<pj and park[ni][nj]!='X':
                ti,tj =ni,nj
                n-=1
            else :
                break
        if n==0: # 경로상에 장애물이 없다면 그 경로이동을 반영
            i,j = ti,tj
    return [i,j]