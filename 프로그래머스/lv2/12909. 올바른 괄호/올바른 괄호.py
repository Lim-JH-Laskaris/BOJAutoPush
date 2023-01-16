def solution(s):
    """ s 문자열의 첫 문자부터 하나씩 뽑는다. 
    '(' 문자면 stack 변수를 +1, ')'문자면 -1을 한다. 
    이때 중간에라도 stack 변수가 음수가 된다면 이는 ())( 와 같은 경우로,
    닫을 괄호가 없는데도 괄호를 닫은 경우다.
    s 문자열을 모두 뽑았다면 stack 변수가 0인지 아닌지에 따라 
    최종 반환을 수행한다.
    """
    stack = 0
    for i in s:
        stack = stack+1 if i=='(' else stack-1
        if stack < 0 : return False 
    return True if stack==0 else False

