from collections import deque

def solution(s):
    pre = deque()
    pro = deque(s)
    result = []
    while pro :
        pop = pro.popleft()
        if not pop in pre : result.append(-1)
        else : result.append(pre.index(pop)+1)
        pre.appendleft(pop)
    return result