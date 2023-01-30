from collections import deque

def solution(s):
    pre, pro = deque(), deque(s)
    result = []
    while pro :
        pop = pro.popleft()
        if pop not in pre : result.append(-1)
        else : result.append(pre.index(pop)+1)
        pre.appendleft(pop)
    return result