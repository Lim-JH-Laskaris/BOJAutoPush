from heapq import heappop, heappush, heapify

def solution(n, works):
    """최초코드"""
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

def solution(n, works):
    """라인 수를 줄인 개선 코드"""
    heapify(works := [-w for w in works])
    for i in range(n):
        heappush(works, min(heappop(works)+1,0))
    return sum([w**2 for w in works])
""" := 대입과 할당을 동시에."""

def solution(n, works):
    """약간의 효율성 개선 코드"""
    if sum(works)<=n : return 0 # 야근 없는 경우
    heapify(works := [-w for w in works])
    for _ in range(n):
        if (p := heappop(works)+1)<0 : heappush(works, p) 
    return sum([w**2 for w in works])