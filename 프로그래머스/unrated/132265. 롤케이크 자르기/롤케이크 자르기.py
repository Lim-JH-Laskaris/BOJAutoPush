from collections import Counter

def solution(topping):
    count_topping = dict(Counter(topping))
    l_side = set()
    l_side_c = 0
    r_side_c = len(set(topping))
    equal_cut = 0
    for i in topping:
        count_topping[i] -= 1
        if i not in l_side : 
            l_side.add(i)
            l_side_c = len(l_side)
        if   count_topping[i] == 0 : r_side_c -=1
        if   l_side_c == r_side_c  : equal_cut += 1
        elif l_side_c >  r_side_c  : break
    return equal_cut
