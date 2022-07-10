class FibDict(dict):
    def __init__(self):
        self[0] = 1
        self[1] = 1
    
    def __missing__(self,k):
        self[k] = (self[k-1] + self[k-2]) %1000000007
        # 기존에는 큰수 나눈 나머지 연산을 solution 함수의 출력 부분에서 사용했으나, 효율성 연산에서 걸렸다.
        # 아예 FiboDict에서 수를 나열할 때부터 나누기를 적용하면 큰수 덧셈에서 낭비되는 계산량을 줄일 수 
        # 있지 않을까 해서 시도해보았다. 다만 이는 덧셈과 나눗셈나머지연산 이어서 가능했던 것
        return self[k]


def solution(n):
    fib_dict = FibDict()
    for i in range(n//200):
        x = fib_dict[i*200]
    return fib_dict[n]