def solution(ingredient):
    stack = ''
    for i in ''.join(map(str,ingredient)):
        stack = stack + i 
        if len(stack)>=4 and stack[-4:] == '1231':
            stack = stack[:-4] 
    return (len(ingredient)-len(stack))//4

#ingredient와 stack을 문자열이 아닌 리스트로 사용할 경우 시간초과가 된다. 