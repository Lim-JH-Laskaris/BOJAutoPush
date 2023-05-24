n = int(input())
board = []
for _ in range(n):
    board.extend(list(map(int,input().split())))
    
direction = [(1,0),(0,1)]
roots = [0]*(n*n)
roots[0] =1
for k in range(n*n-1):
    b = board[k]
    i,j = divmod(k,n)
    for d in direction:
        di,dj = i+d[0]*b,j+d[1]*b
        if all([di<n,dj<n]):
            roots[di*n+dj] += roots[i*n+j]
print(roots[n*n-1])
            
        