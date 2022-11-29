def solution(spell, dic):
    answer = [i for i in dic if all(i.count(j)==1 for j in spell)]
    return 1 if answer else 2