from collections import deque, defaultdict

def solution(x, y, n):
    d = defaultdict(int)
    q = deque([x])
    while q:
        a = q.popleft()
        if a == y : 
            return d[a]
        for b in [a+n,a*2,a*3]:
            if b<= y and (d[b]==0 or d[b]>d[a]+1): 
                d[b] = d[a]+1
                q.append(b)
    return -1