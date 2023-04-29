from collections import deque
def solution(sequence, k):
    s,e,n,l = 0,0,0,0
    queue = deque()
    sequence = deque(sequence)
    answer = []
    while sequence:
        if n+sequence[0]<=k :
            i = sequence.popleft()
            queue.append(i)
            e+=1
            n+=i
            l+=1
        elif queue : 
            i = queue.popleft()
            s+=1
            n-=i
            l-=1
        else :
            break
        if n==k:
            if not answer or answer[1]-answer[0]>e-1-s:
                answer = [s,e-1]
    return answer