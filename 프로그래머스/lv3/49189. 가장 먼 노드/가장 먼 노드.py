from collections import deque
def solution(n, edge):
    """BFS"""
    graph = [[] for _ in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    INF = 10**10 
    distance = [INF]*(n+1)
    q = deque()
    q.append(1)
    distance[1] = 0
    while q :
        now = q.popleft()
        for i in graph[now]:
            if distance[i]==INF:
                distance[i]=distance[now]+1
                q.append(i)
    max_d = max(distance[1:])
    return distance.count(max_d)