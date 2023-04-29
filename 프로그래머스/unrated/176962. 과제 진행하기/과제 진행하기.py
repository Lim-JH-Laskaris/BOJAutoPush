from heapq import heappop,heapify

def solution(plans):
    answer = [] 
    stack  = [] # 진행중인 과제
    plans = list(map(lambda p:[int(p[1][:2])*60+int(p[1][3:]),int(p[2]),p[0]],plans))
            # 시작시각을 분단위 정수로, 소요시간을 정수로 변환, 순서변경 (시작, 소요, 이름)
    heapify(plans)
    t = 0 # 현재시각
    while stack or plans:
        if not stack: # 진행중인 과제가 없으면 추가.
            stack.append(heappop(plans))
            t = stack[-1][0] # 새 과제 시작 시각으로 현재시각 갱신
        if not plans or t + stack[-1][1] <= plans[0][0]: 
            # 다음 과제가 없거나 다음 과제 시작 전에 지금 과제 끝나면 
            t += stack[-1][1] # 지금과제 마친 시각으로 현재시각 갱신
            answer.append(stack.pop()[2])
        else : # 지금과제 끝나기 전에 다음 과제 받으면, 
            stack[-1][1] -= plans[0][0]-t # 지금 과제의 진행률 차감
            t = plans[0][0] # 다음과제 시작 시각으로 현재시각 갱신
            stack.append(heappop(plans))   
    return answer