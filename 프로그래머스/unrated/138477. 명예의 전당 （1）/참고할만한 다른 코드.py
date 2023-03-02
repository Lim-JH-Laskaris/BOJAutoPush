import heapq

def solution(k,score):
    max_heap = []
    answer = []
    for sc in score:
        heapq.heappush(max_heap,(-sc,sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])
    return answer

# 예상과 달리 그냥 리스트를 매번 sorted해주는 것보다 효율이 좋지 않다. 파이썬 기본 sorted함수가 최적화가 잘 되어있어서인듯.
# 다만 힙을 사용하는 풀이 예제로 기록해둠
