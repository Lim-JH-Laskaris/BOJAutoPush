import heapq
import sys 

input = sys.stdin.readline
INF = int(1e9)
v,e = map(int,input().split())
start = int(input())
gragh = [[] for i in range(v+1)]
distance = [INF]*(v+1)

for _ in range(e):
    u1,u2,w = map(int,input().split())
    gragh[u1].append((u2,w))
    
q = []
heapq.heappush(q,(0,start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist>distance[now]:
        continue
    for i in gragh[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

for i in range(v+1):
    if i ==0 : continue
    if distance[i] == INF: print('INF')
    else : print(distance[i])