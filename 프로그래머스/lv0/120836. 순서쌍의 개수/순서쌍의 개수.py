def make_prime_number_list(n):   
    """n이하의 모든 소수를 리스트로 반환"""
    return [i for i in range(2,n+1) if all(i%j!=0 for j in range(2,int(i**.5)+1))]

def divide_t_time(n,d,t=0):
    """n이 d로 몇 번 나누어지는지(t)와 그 결과 값(n//d**t)을 반환 (순서는 반대)"""
    if n%d==0: return divide_t_time(n//d,d,t+1)
    else : return n, t

def multiply_all(_list):
    """리스트 내 모든 값을를 곱하는 함수"""
    a = 1 
    while _list : 
        a *= _list.pop()
    return a

def solution(n):
    prime_number_list = make_prime_number_list(n) 
    prime_factorization_list = [0]*len(prime_number_list)
    for i in range(len(prime_number_list)):
        n, prime_factorization_list[i] = divide_t_time(n,prime_number_list[i])
    return multiply_all(list(map(lambda x:x+1, prime_factorization_list)))

