from math import factorial

def solution(n, k):
    answer = []
    k -= 1 # 0부터 시작하는 서수로 변환
    n = list(range(1,n+1)) 
    while n : 
        d, k = divmod(k,factorial(len(n)-1))
        answer.append(n.pop(d))
    return answer