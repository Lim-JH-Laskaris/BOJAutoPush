def solution(brown, yellow):
    """x는 카펫의 가로, y는 카펫의 세로.
    xy는 카펫의 넓이. max_x는 가로의 최대 길이. 즉 세로가 2일때의 x
    x>y이므로, x가 최대일 때부터 하나씩 감소시켜가며 
    x*y와 brown+yellow가 동일한 경우를 찾는다.
    """
    xy = brown+yellow
    max_x = brown//2
    for x in range(max_x, 1, -1):
        y = max_x+2-x
        if x*y == xy : 
             return [x,y]