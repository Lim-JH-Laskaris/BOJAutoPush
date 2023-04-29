from heapq import heapify, heappop, heappush

def solution(targets):
    answer = 0
    x = 0 # 현재 훑고 있는 x영역 0부터 순차적으로 훑음
    heapify(targets)
    hq = [] # 요격 미사일의 사정권에 포함된 폭격 미사일 
    while hq or targets:
        if targets and (not hq or hq[0][0]>targets[0][0]):
            # 추가할 미사일이 있고, 
            #hq가 비어있거나 혹은 (x상승시 사정권에서 벗어나는 폭격 미사일이 존재하지 않을 때) 
            s,e = heappop(targets)
            heappush(hq,[e,s]) # e,s 반대
            x = s
        else: # 새 미사일이 hq에 들어오기 전에 끝나는 hq미사일이 있거나, 미사일이 더 없을때
            x = hq[0][0] 
            hq = [] # 미사일 요격
            answer += 1
    return answer