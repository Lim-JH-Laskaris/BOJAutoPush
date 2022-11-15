from itertools import combinations
def solution(number):
    return len([0 for i in combinations(number,3) if sum(i)==0])