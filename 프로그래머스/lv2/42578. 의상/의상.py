from collections import Counter

def solution(clothes):
    c = Counter(map(lambda x:x[1],clothes))
    answer = 1 
    for i in c.values():
        answer *= i+1
    return answer - 1