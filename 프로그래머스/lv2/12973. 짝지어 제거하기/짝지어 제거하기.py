def solution(s):
    stack = []
    s_rev = list(reversed(list(s)))
    while s_rev: 
        if not stack : # stack이 비어있으면 채워줌
            stack.append(s_rev.pop())
        elif stack[-1] == s_rev[-1] : # 같으면 둘다 제거
            s_rev.pop()
            stack.pop()
        else : # 같지 않으면 스택으로 이동
            stack.append(s_rev.pop())  
    return 0 if stack else 1 # 스택이 비어있으면 성공이므로 1