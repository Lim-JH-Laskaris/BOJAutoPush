from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

gragh = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    gragh[a].append((b,c))

start, end = map(int,input().split())
q = []
heappush(q,(0,start))
distance[start] = 0
while q :
    dist, now = heappop(q)
    if dist > distance[now]:continue
    for i in gragh[now]:
        cost = dist+i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heappush(q,(cost,i[0]))
            
print(distance[end])
