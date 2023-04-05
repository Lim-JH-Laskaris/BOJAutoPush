import heapq
import sys

input = sys.stdin.readline
INF = 10**10
n,m,x = map(int,input().split())
gragh = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    gragh[a].append((b,c))
    
    
def dijstra(start):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in gragh[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

distance_from_x = dijstra(x)
distance_list = [distance_from_x[i]+dijstra(i)[x] for i in range(n+1)]
print(max(distance_list[1:]))

