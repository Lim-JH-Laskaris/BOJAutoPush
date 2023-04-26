from heapq import heappush,heappop

def solution(operations):
    hq = []
    for o in operations:
        o,n = o[0],int(o[2:])
        if o == 'I' : heappush(hq,n)
        elif hq : # 큐가 비어있지 않으면
            if   n == 1 : hq.remove(max(hq[len(hq)//2:]))
            elif n ==-1 : heappop(hq)
    return [max(hq),hq[0]] if hq else [0,0]