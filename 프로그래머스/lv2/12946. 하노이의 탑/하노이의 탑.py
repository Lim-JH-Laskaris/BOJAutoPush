def from13toAC(result, a, c):
    """1번 기둥에서 3번기둥으로 원판들을 옮기는 답안을, a에서 c로 옮기는 답으로 변환.
    즉, 답안의 1을 a, 2를 b, 3을 c로 변환하는 함수.
    """
    b = tuple({1,2,3} - {a,c})[0] 
    trans = {1:a,2:b,3:c}
    return [[trans[i[0]],trans[i[1]]] for i in result]
    
def solution(n):
    result = []
    for i in range(n):
        result = from13toAC(result,1,2)+[[1,3]]+from13toAC(result,2,3)
    return result

"""
n-1개의 원판을 1에서 3으로 옮기는 과정(이하 n-1의 1-3과정)을 기록했다고 하자.
그렇다면 n개의 원판을 1에서 3으로 옮기는 과정(이하 n의 1-3과정)은 다음같이 나타낼 수 있다.

1. n-1의 1-2과정
2. 맨 아래 원판을 1에서 3으로 옮김
3. n-1의 2-3과정

따라서, 1-3과정을 1-2과정이나 2-3과정으로 변환하는 함수를 갖추고, 보텀업 방식으로 n번째 답을 제출
"""