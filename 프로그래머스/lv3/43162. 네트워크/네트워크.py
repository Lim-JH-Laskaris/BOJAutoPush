from collections import deque
#BFS 알고리즘 이용
def solution(n, computers):
    answer = 0
    check_list = [0]*n   
    link_dict = {i:[j for j in range(n) if computers[i][j]==1] for i in range(n)}
    for i in range(n):
        if check_list[i] == 0:
            queue = deque([i])
            while queue:
                p = queue.popleft()
                if check_list[p] == 0:
                    check_list[p] = 1 
                    queue.extend(link_dict[p])
            answer += 1
    return answer
