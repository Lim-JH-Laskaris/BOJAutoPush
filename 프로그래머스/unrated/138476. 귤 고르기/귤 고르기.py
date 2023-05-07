from collections import Counter
        
def solution(k, tangerine):
    c = Counter(tangerine) #{크기:개수}
    c = sorted(c.values(), reverse=True) #[개수]
    answer = 0
    for i in c:
        k -= i
        answer += 1
        if k<=0 : return answer