from collections import Counter
from collections import deque

def solution(topping):
    count_topping = dict(Counter(topping))
    deque_topping = deque(topping)
    l_side = set()
    r_side_c = len(set(topping))
    equal_cut = 0
    for i in range(len(topping)):
        i_popleft = deque_topping.popleft()
        l_side.add(i_popleft)
        l_side_c = len(l_side)
        count_topping[i_popleft] -= 1
        r_side_c = r_side_c-1 if count_topping[i_popleft] == 0 else r_side_c
        if   l_side_c == r_side_c : equal_cut += 1
        elif l_side_c >  r_side_c : break
    return equal_cut


#시도1 - 시간초과 : 중복되는 부분을 제거 필요
# def solution(topping):
#     return sum([1 for i in range(1,len(topping)) if len(set(topping[:i]))==len(set(topping[i:]))])
