def solution(array):
    count = [0]*(max(array)+1)
    for i in array:
        count[i] += 1
    if count.count(max(count)) > 1: 
        return -1
    else :
        return count.index(max(count))