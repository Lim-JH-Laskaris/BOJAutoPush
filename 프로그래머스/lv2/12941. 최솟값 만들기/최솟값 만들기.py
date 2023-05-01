from functools import reduce
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return reduce(lambda x,y:x+y,[x*y for x,y in zip(A,B)])