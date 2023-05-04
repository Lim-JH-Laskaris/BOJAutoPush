def solution(s):
    stack = []
    for i in s:
        if not stack : # stack이 비어있으면 채워줌
            stack.append(i)
        elif stack[-1] == i : # 같으면 제거
            stack.pop()
        else : # 같지 않으면 스택으로 이동
            stack.append(i)  
    return 0 if stack else 1 # 스택이 비어있으면 성공이므로 1