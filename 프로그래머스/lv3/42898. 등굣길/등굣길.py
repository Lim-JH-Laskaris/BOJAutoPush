def solution(m, n, puddles):
    map = [[0]+[-1]*(m) if i>0 else [0]*(m+1) for i in range(n+1)]
            # 첫 행과 첫 열은 0로 채우고 나머지는 -1로 채운 행렬
            # 집은 1,1에 있으며 그 위와 왼쪽으로는 가상의 웅덩이가 있다 가정
            # 웅덩이는 0으로 표현, -1은 아직 계산되지 않은 경로
    map[1][1] = 1 # 시작지점
    for a,b in puddles: # 웅덩이 표시
        map[b][a] = 0
    for i in range(3,m+n+1): 
        for a in range(1,i): #좌하양 대각선 방향으로 진행
            b = i-a
            if (a<=m and b<=n) and map[b][a] == -1:
                map[b][a] = (map[b-1][a] + map[b][a-1])%1000000007
    return map[n][m]