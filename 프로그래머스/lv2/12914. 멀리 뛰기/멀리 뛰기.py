class FibDict(dict):
    def __init__(self):
        self[0] = 1
        self[1] = 1
    
    def __missing__(self,k):
        self[k] = (self[k-1]+self[k-2])%1234567
        return self[k]

def solution(n):
    fib_dict = FibDict()
    return [fib_dict[i] for i in range(n%200,n+1,200)][-1]
    #재귀한계문제를 해결하기위해 적당한 단위로 끊어서 호출해 메모한다.