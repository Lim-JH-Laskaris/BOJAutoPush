from collections import deque
def solution(money):
    if len(money)==3 : #세집일때
        return max(money) 
    # 마지막 지점을 안 턴다 가정할 때.
    s = [0]*(len(money)-1)
    s[0] = money[0]
    s[1] = max(money[0],money[1])
    for i in range(2,len(s)):
        s[i] = max(s[i-1],s[i-2]+money[i])
    answer1 = s[-1]
    # # 마지막 지점을 턴다 가정할 때.
    s = [0]*(len(money)-1)
    s[1] = money[1]
    s[2] = max(money[1],money[2])
    for i in range(3,len(s)):
        s[i] = max(s[i-1],s[i-2]+money[i])
    answer2 = s[-2] + money[-1]
    return max(answer1,answer2)