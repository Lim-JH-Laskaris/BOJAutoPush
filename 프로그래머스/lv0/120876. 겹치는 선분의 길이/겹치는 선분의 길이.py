def solution(lines):
    l = [0]*201
    for a,b in lines:
        for i in range(a,b):
            l[i] += 1
    result = sum([1 for i in l if i>1])    
    return result