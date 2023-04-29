from functools import reduce
solution = lambda k,d : reduce(lambda r,i:r+(d**2-i**2)**.5//k +1,range(0,d+1,k),0)


# def solution(k, d):
#     answer = 0
#     for i in range(0,d+1,k):
#         answer += (d**2-i**2)**.5//k +1
#     return answer

