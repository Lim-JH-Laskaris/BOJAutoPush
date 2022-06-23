def triangular_number(n):
    return n*(n+1)//2

def approximate_value_of_n(a):
    return(int(((a-1)/3)**.5))

def solution(a, n=0):
    while a > triangular_number(n)*6+1: n += 1
    return n+1

a = int(input())
# print(solution(a)) 이 함수를 쓰면 간단하게 구할 수 있지만 시간복잡도가 크다.
print(solution(a,n=approximate_value_of_n(a))) 
    # 정답n과 같거나 작은 근사치 정수를 미리 입력하여 시간복잡도를 줄임