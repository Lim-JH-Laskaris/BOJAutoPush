class FibDict(dict):
    def __init__(self):
        self[0] = 1
        self[1] = 1
    
    def __missing__(self,k):
        self[k] = (self[k-1]+self[k-2])%1234567
        return self[k]

fib_dict = FibDict()  
    #클래스 인스턴스 자체는 다음 문제들에 재활용될 수 있다.
    
solution = lambda n : [fib_dict[i] for i in range(n%200,n+1,200)][-1]
    #재귀한계문제를 해결하기위해 적당한 단위로 끊어서 호출해 메모한다.
    