def solution(ingredient):
    stack = ''
    for i in ''.join(map(str,ingredient)):
        stack = stack + i 
        if len(stack)>=4 and stack[-4:] == '1231':
            stack = stack[:-4] 
    return (len(ingredient)-len(stack))//4

# ingredient와 stack을 문자열이 아닌 리스트로 사용할 경우 시간초과가 된다. 
# 한계상황에서 리스트에 비해 문자열이 10~20배 정도 빠른듯하다.