from itertools import combinations

def cal_slope(a,b):
    """ 두 점을 잇는 직선의 기울기를 구하는 함수"""
    return (a[1]-b[1])/(a[0]-b[0])

def solution(dots):
    """ 점들 사이에 가능한 모든 직선의 기울기를 구한 후, 
    이중 기울기가 같은 경우(평행한 경우) 1을 반환, 없으면 0 반환"""
    slope_list = [cal_slope(i[0],i[1]) for i in combinations(dots,2)]
    if len(slope_list) == len(set(slope_list)):
        return 0 
    else :
        return 1
