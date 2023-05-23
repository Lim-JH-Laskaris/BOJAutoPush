import sys
sys.setrecursionlimit(10**5)

m,n = map(int,input().split())
class Roots(dict):
    def __init__(self,m,n):
        self.hight = []
        for _ in range(m):
            self.hight.extend(list(map(int,input().split())))
        self[0] = 1
        self.direction = [(-1,0),(0,-1),(1,0),(0,1)]
        
    def __missing__(self,k):
        h = self.hight[k]
        i,j = divmod(k,n)
        self[k] = 0
        for d in self.direction:
            di,dj = i+d[0],j+d[1]
            if all([di>=0,di<m,dj>=0,dj<n]) and h<self.hight[di*n+dj]:
                self[k]+=self[di*n+dj]
        return self[k]
        
root = Roots(m,n)
print(root[m*n-1])