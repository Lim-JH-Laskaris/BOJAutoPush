class TilingDict(dict):
    def __init__(self):
        self[0] = 1
        self[2] = 3
        
    def __missing__(self,k):
        self[k] = (self[k-2]*4-self[k-4])%1000000007
        return self[k]

def solution(n):
    td = TilingDict()
    for i in range(n//200): td[i*200]
    return td[n]

"""
점화식이 
s[k] = s[k-2]*4-s[k-4]
의 형태를 가지는 이유 해설.

https://s2choco.tistory.com/24
이곳 등 대부분의 글에서는 
s[k] = s[k-2]*3+s[k-4]*2+s[k-6]*2+...+s[4]*2++s[2]*2+2
의 점화식으로 문제를 풀고있다. 

그런데 위의 식에서 
s[k-2] = s[k-4]*3+s[k-6]*2+...+s[4]*2++s[2]*2+2
이고 양변에 s[k-4]를 빼면
s[k-2]-s[k-2] = s[k-4]*2+s[k-6]*2+...+s[4]*2++s[2]*2+2
인데, 이는 위의 s[k]에 대한 점화식의 s[k-2]*3+~~ 이후부분과 동일하므로
s[k] = s[k-2]*3+s[k-2]-s[k-2] = s[k-2]*4-s[k-2]
이렇게 단순화 할 수 있다.
"""