from collections import deque

def max_zip(q, idx=0):
    if q : return max(list(map(lambda x:x[idx],q)))
    else : return -1

def solution(priorities, location):
    q = deque(zip(priorities,range(len(priorities))))
    c = 0
    while q:
        p,i = q.popleft()
        if p < max_zip(q):
            q.append((p,i))
        else :
            c += 1
            if i==location:
                return c
            
            