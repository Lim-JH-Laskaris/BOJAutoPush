

def solution(r1, r2):
    answer = 0
    # 우선 하나의 사분면에서만 계산 
    for i in range(1,r2): # r2포함 점 셈. 단 x축 y축 상의 점 빼고
        answer += int((r2**2-i**2)**.5)
    for i in range(1,r1): # r1포함 점 뺌. 단 x축 y축 상의 점 빼고
        answer -= int((r1**2-i**2)**.5)
        if int((r1**2-i**2)**.5) == (r1**2-i**2)**.5 : 
            answer += 1 # r1의 경계에 있는 점 다시 추가
    answer += r2-r1+1 # 축 상의 점 추가 
    return answer*4 # 전체 좌표평면으로 확대
