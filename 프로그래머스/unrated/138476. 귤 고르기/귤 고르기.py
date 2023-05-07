from collections import Counter
        
def solution(k, tangerine):
    c = Counter(tangerine) #{크기:개수}
    cc = sorted(c.values(), reverse=True) #[개수]
    answer = 0
    for a in cc:
        k -= a
        answer += 1
        if k<=0 : return answer
    

def solution(k, tangerine):
    c = Counter(tangerine) #{크기:개수}
    cc = sorted(Counter(c.values()).items(), reverse=True) #[(개수,개수의 개수)]
    answer = 0
    for a,b in cc:
        for i in range(b):
            k -= a
            answer += 1
            if k<=0 : return answer