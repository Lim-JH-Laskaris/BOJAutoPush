from collections import defaultdict

def solution(name, yearning, photo):
    ny = defaultdict(int,{n:y for n,y in zip(name, yearning)})
    return [sum(map(lambda i : ny[i] ,p)) for p in photo]