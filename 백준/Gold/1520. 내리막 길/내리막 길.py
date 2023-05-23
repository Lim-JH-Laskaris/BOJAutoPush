import sys
sys.setrecursionlimit(500**2) 

m,n = map(int,input().split())

class Roots(dict):
    def __init__(self,m,n):
        # 좌표(i,j)에 대해, k=i*n+j로 두고 이때의 k값을 key로, 경로 수를 value로.
        # k를 따로 지정하는 이유: 파이썬 딕셔너리가 튜플,리스트를 키값으로 가지지 못함.
        self[0] = 1         # 시작점
        self.hight = []     # 고도를 담을 리스트, 마찬가지로 k값으로 접근 
        for _ in range(m):
            self.hight.extend(list(map(int,input().split())))
        self.direction = [(-1,0),(0,-1),(1,0),(0,1)]      
        
    def __missing__(self,k):
        h = self.hight[k]
        i,j = divmod(k,n)    # 현재 지점의 좌표
        self[k] = 0
        for d in self.direction:
            di,dj = i+d[0],j+d[1] #(i,j)지점에 인접한 네 곳의 좌표
            if all([di>=0,di<m,dj>=0,dj<n]) and h<self.hight[di*n+dj]:
                # 해당좌표가 범위를 넘어서지 않고, 그 높이가 현재 지점보다 높을경우, 
                self[k]+=self[di*n+dj]     
                # 그곳까지의 경로 수를 현재 지점까지의 경로수에 더한다. 
        return self[k]
        
print(Roots(m,n)[m*n-1])