from collections import deque
from copy import deepcopy

def bfs(map_list,x,y,target):
    near = [(0,1),(1,0),(0,-1),(-1,0)]
    is_in = lambda a,b,m=len(map_list),n=len(map_list[0]):all([a>=0,b>=0,a<m,b<n])
    ml = deepcopy(map_list)
    ml[x][y] = 0
    q = deque([(x,y)])
    while q:
        a,b = q.popleft()
        for v,w in near:
            if is_in(a+v,b+w) and ml[a+v][b+w] in ['S','E','O','L']:
                if ml[a+v][b+w] == target: 
                    return ml[a][b] +1
                q.append((a+v,b+w))
                ml[a+v][b+w] = ml[a][b] +1 
    return -1
                

def solution(maps):
    answer = 0
    m,n = len(maps),len(maps[0])
    for i in range(m):
        for j in range(n):
            if   maps[i][j]=='S': sx,sy=i,j
            elif maps[i][j]=='L': lx,ly=i,j
            elif maps[i][j]=='E': ex,ey=i,j 
    map_list = list(map(list, maps)) 
    sl = bfs(map_list,sx,sy,'L')
    if sl == -1 : return -1
    else : answer += sl
    le = bfs(map_list,lx,ly,'E')  
    if le == -1 : return -1
    else : answer += le
    return answer