class FibDict(dict):
    def __init__(self):
        self[0] = 1
        self[1] = 1
    
    def __missing__(self,k):
        self[k] = (self[k-1] + self[k-2]) %1000000007
        return self[k]


def solution(n):
    fib_dict = FibDict()
    for i in range(n//200):
        x = fib_dict[i*200]
    return fib_dict[n]