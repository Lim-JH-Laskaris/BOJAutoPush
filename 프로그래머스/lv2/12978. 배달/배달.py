from heapq import heappop,heappush

def solution(n, road, k):
    """다익스트라"""
    INF = 10**8
    distance = [INF]*(n+1)
    graph = [[] for i in range(n+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    hq = [(0,1)]
    distance[1] = 0
    while hq:
        dist, now = heappop(hq)
        if dist> distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(hq,(cost,i[0]))
    return sum([d<=k for d in distance])