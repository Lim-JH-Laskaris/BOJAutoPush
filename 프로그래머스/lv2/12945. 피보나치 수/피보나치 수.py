# 딕셔너리 클래스를 상속받아 피보나치수열을 구현
class FibDict(dict):
    def __init__(self):
        self[0] = 0
        self[1] = 1 

    def __missing__(self, k):
        self[k] = self[k-1] + self[k-2]
        return self[k]
    
def solution(n):
    fib_dict = FibDict()
    #재귀한계문제를 해결하기위해 적당한 단위로 끊어서 호출해 메모한다.
    for i in range(n//200):
        x = fib_dict[i*200]
    return fib_dict[n]%1234567