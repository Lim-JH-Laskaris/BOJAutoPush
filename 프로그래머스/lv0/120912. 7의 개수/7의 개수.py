def solution(array):
    return sum([1 for i in ''.join(list(map(str,array))) if i=='7'])