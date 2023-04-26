"""최소 비용 신장트리 minimum spinning tree(MST)"""
from heapq import heapify, heappop, merge
    
def solution1(n, costs,k):
    graph = [[] for _ in range(n)] 
        # 주의!! [[]]*n으로 할당하면 []주소가 모두 같은 동일 []가 할당되어, 
        # 한곳에 append시 모든 곳에 append됨
    linked = [False]*n
    for a,b,c in costs:
        graph[a].append((c,b)) # 추후 c를 기준으로 최소힙 생성
        graph[b].append((c,a))
    for g in graph:
        heapify(g)

    start = k
    linked[start] = True # 추후 다리 비용으로 채움. 합계를 구하면 True=1이므로 이는 제외
    priority_queue = graph[start] # 시작지점에서 이어나갈 수 있는 다리들을 후보군에 추가
    while not all(linked): 
        c,b = heappop(priority_queue) # 0에서 갈 수있는 곳에서의 비용이 가장 작은 다리
        if linked[b] == False : # 아직 연결되어있지 않으면
            linked[b] = c
            priority_queue = list(merge(priority_queue,graph[b])) # 후보군 추가
    return sum(linked)-1

def solution(n,costs):
    return min([solution1(n,costs,k) for k in range(n)])