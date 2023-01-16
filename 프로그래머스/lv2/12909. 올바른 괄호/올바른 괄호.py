#import sys 
#sys.setrecursionlimit(10**5)

#solution = lambda s ,stack=0:(True if stack==0 else False) if len(s)==0 else (
#    False if stack<0 else solution(s[1:], stack+1 if s[0]=='(' else stack-1))
## 효율성 테스트 통과 못함

def solution(s):
    stack = 0
    s=list(s)
    while s:
        a = s.pop()
        stack = stack+1 if a==')' else stack-1
        if stack < 0 : return False 
    return True if stack==0 else False