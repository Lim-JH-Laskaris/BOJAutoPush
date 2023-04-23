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