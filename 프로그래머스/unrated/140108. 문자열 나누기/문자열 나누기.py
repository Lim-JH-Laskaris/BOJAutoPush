import sys
sys.setrecursionlimit(10000)

def solution(s,n=0):
    x0,x1 = 0,0
    x = s[0]
    for i in range(len(s)):
        if x == s[i] : x1 += 1
        else : x0 += 1
        if x0 == x1 and i<len(s)-1: return solution(s[i+1:],n+1)
    return n+1