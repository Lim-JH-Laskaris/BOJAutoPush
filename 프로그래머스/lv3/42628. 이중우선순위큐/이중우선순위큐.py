from heapq import heappush,heappop

def solution(operations):
    hq = []
    for o in operations:
        o,n = o[0],int(o[2:])
        if o == 'I' : heappush(hq,n)
        elif hq : # 큐가 비어있지 않으면
            if   n == 1 : hq.remove(max(hq[len(hq)//2:]))
            elif n ==-1 : heappop(hq)
    return [max(hq),hq[0]] if hq else [0,0]

"""
나와 동일한 접근인 답에 대한 댓글들
--------------------------------------
이건 시간초과가 안날까요? 50만개의 데이터가 들어오고, 
50만개의 데이터를 pop할 시에는 remove를 사용했기에 어마어마한 연산이 일어날 것 같은데요.

max가 리프 노드에 있다는 것은 보장되지만 가장 끝 노드(인덱스)에 있다는 것은 보장되지 않습니다. 
저렇게 remove로 제거해버리면 heap 구조가 깨지게 돼요

윗분을 조금 부연설명 하자면저렇게 삭제를 한다면 해당 리프의 뒤에 있던 원소들이 
앞으로 끌려와서 트리가 깨집니다

["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]일 때 
[7, 4]가 답인데 이 코드는 [7, 3]이라고 나옵니다.

remove를 쓰신이후 heapify를 써서 다시 만들어주면 됩니다.
"""