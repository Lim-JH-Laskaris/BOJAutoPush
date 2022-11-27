class TilingDict(dict):
    def __init__(self):
        self[0] = 1
        self[2] = 3
        
    def __missing__(self,k):
        self[k] = (self[k-2]*4-self[k-4])%1000000007
        return self[k]


def solution(n):
    td = TilingDict()
    for i in range(n//50):
        x = td[i*50]
    return td[n]