from collections import deque

def solution(maps,x=0,y=0):
    n, m = len(maps),len(maps[0])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque([(0,0)])
    
    while queue :
        x,y = queue.popleft()
        for i,j in zip(dx,dy):
            nx = x+i
            ny = y+j
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
                
    return maps[-1][-1] if maps[-1][-1]>1 else -1