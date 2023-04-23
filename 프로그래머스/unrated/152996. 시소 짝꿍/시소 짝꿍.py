from collections import Counter

def solution(weights):
    count = Counter(weights) # {무게:인원수}
    keys = sorted(list(count.keys())) # 예)[100,180,270,360]
    answer = 0
    for k in keys: 
        answer += count[k]*(count[k]-1)//2 # 무게가 같은 경우의 짝꿍을 셈
        if k*2 in keys : answer += count[k]*count[k*2]
        if k%2==0 and k*3//2 in keys : answer += count[k]*count[k*3//2]
        if k%3==0 and k*4//3 in keys : answer += count[k]*count[k*4//3]
    return answer

"""인원수는 최대 10**6으로 많지만, 값의 범위는 900에 정수 한정이라 Counter를 이용해 
푸는 것으로 계산 중복을 크게 줄일수 있었다. 정수 조건이 없거나 값의 범위가 인원수 보다 많았다면 
이 방법으로 복잡도를 유의미하게 줄이지는 못했을 것"""