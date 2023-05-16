from heapq import heappop, heappush, heapify

def solution(n, works):
    works = list(map(lambda x:-x,works))
    heapify(works)
    while n:
        p = heappop(works)
        if p != 0:
            heappush(works, p+1)
            n -= 1
        else: 
            break
    return sum(list(map(lambda x:x**2,works)))