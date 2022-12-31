def mk_prime_numbers(n):
    """n이하의 소수 리스트를 생성하는 함수"""
    prime_numbers = [2]
    for i in range(3,n+1):
        if 0 in [i%j for j in prime_numbers]:
            continue
        else :
            prime_numbers.append(i)
    return prime_numbers
        
    
def solution(n):
    prime_numbers = mk_prime_numbers(n)
    return [j for j in prime_numbers if n%j==0]