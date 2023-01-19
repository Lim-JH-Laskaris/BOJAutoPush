def solution(ingredient):
    #ingredient_reverse = ingredient[::-1]
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack)>=4 and stack[-4:] == [1,2,3,1]:
            stack = stack[:-4] 
    return (len(ingredient)-len(stack))//4

def solution(ingredient):
    stack = ''
    for i in ''.join(map(str,ingredient)):
        stack = stack + i 
        if len(stack)>=4 and stack[-4:] == '1231':
            stack = stack[:-4] 
    return (len(ingredient)-len(stack))//4