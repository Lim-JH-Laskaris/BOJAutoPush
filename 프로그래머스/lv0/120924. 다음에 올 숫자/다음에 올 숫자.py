def solution(common):
    a,b,c = common[:3]
    if   b-a == c-b : return common.pop() + (b-a)
    elif b/a == c/b : return common.pop() * (b//a) 
    else : raise