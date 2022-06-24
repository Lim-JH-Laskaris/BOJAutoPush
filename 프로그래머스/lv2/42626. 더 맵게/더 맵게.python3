import heapq

def drop_under_k(scoville, K):
    return [x for x in scoville if x>=K]

def drop_upper_k(scoville, K):
    return [x for x in scoville if x<K]

def drop_unnecessary_elements(scoville, K):
    under_k = drop_upper_k(scoville, K)
    upper_k = drop_under_k(scoville, K)
    if upper_k : return under_k + [min(upper_k)]
    else : return under_k

def mix_scoville(scoville):
    new_food = heapq.heappop(scoville) + heapq.heappop(scoville)*2
    heapq.heappush(scoville,new_food)
    return scoville

def solution(scoville, K):
    scoville = drop_unnecessary_elements(scoville, K)
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K: 
        if len(scoville)<2 : 
            return -1
        mix_scoville(scoville)
        count += 1
    return count