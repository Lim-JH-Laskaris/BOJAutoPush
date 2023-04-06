""" 총 여섯개의 최단경로를 구하고 이들을 둘로 묶어서 비교한다.
1->v1, v1->v2, v2->n
1->v2, v2->v1, v1->n
이때 그래프가 양방향이므로 v1-v2는 동일.
"""
import heapq
import sys

input = sys.stdin.readline
INF = 10**10
n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

dj1 = dijkstra(1)
djv1= dijkstra(v1)
djv2= dijkstra(v2)
answer = min(dj1[v1]+djv1[v2]+djv2[n],
            dj1[v2]+djv2[v1]+djv1[n])
if answer>=INF:
    print(-1)
else :
    print(answer)