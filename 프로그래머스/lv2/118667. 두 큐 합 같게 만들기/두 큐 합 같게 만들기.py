from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1,s2 = sum(q1),sum(q2)
    l1,l2 = len(q1),len(q2)
    c = 0
    while c<(l1+l2)*2:
        if   l1==0 or l2==0 : 
            return -1
        if   s1==s2:
            return c
        elif s1>s2:
            p = q1.popleft()
            q2.append(p)
            s1,s2 = s1-p,s2+p
            l1,l2 = l1-1,l2+1
            c += 1
        elif s2>s1:
            p = q2.popleft()
            q1.append(p)
            s1,s2 = s1+p,s2-p
            l1,l2 = l1+1,l2-1  
            c += 1
    return -1

