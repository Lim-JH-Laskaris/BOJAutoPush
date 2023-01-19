def solution(ingredient):
    stack = ''
    for i in ''.join(map(str,ingredient)):
        stack = stack + i 
        if len(stack)>=4 and stack[-4:] == '1231':
            stack = stack[:-4] 
    return (len(ingredient)-len(stack))//4