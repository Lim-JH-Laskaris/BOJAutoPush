

def solution(r1, r2):
    answer = 0
    # 우선 1사분면+y축(y>0) 에서만 계산. x축 제외 
    for i in range(r2): # r2포함 점 셈. 
        answer += int((r2**2-i**2)**.5)
    for i in range(r1): # r1포함 점 뺌. 
        answer -= int((r1**2-i**2)**.5)
        if int((r1**2-i**2)**.5) == (r1**2-i**2)**.5 : 
            answer += 1 # r1의 경계에 있는 점 다시 추가
    return answer*4 # 전체 좌표평면으로 확대
