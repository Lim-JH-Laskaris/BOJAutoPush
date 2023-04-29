from collections import deque

def solution(sequence, k):
    sequence = deque(sequence) # 큐로 사용 
    queue = deque() # 수열후보 
    s,e,n = 0,0,0 # 수열후보의 시작점,끝점+1,합
    answer = []
    while sequence:
        if n+sequence[0]<=k : # 추가해도 k를 넘지 않으면 추가
            i = sequence.popleft()
            queue.append(i)
            e+=1
            n+=i
        elif queue : # 추가하면 k가 넘는데, 큐가 비어있지 않으면, 큐 팝
            i = queue.popleft()
            s+=1
            n-=i
        else : # 추가하면 k가 넘는데, 큐가 비어있다면 더이상 진행할 수 없으므로,
            break
        if n==k: # 조건에 맞는 부분수열을 찾으면
            if not answer or answer[1]-answer[0]>e-1-s:
                answer = [s,e-1] # 만약 이전 후보보다 길이가 짧으면 갱신.
    return answer