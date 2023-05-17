from heapq import heapify, heappop

def solution(A, B):
    heapify(A)
    heapify(B)
    answer = 0
    while B:
        b = heappop(B)
        if b>A[0]:
            heappop(A)
            answer += 1
    return answer