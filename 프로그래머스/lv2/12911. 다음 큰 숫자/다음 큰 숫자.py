def solution(n):
    n1c = bin(n).count('1')
    while True :
        n += 1
        if n1c == bin(n).count('1'):
            return n
    