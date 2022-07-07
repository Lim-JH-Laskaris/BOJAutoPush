from itertools import permutations

def is_prime_number(number):
    """소수인지 아닌지 판단하여 불리언 출력"""
    return all(number%j for j in range(2,int(number**.5 +1))) and number>1

def prime_number_permutation(numbers,n):
    """numbers를 원소로, n을 길이로 하는 순열 중 소수만을 리스트에 담고 출력"""
    prime_numbers = [int(''.join(i)) 
                     for i in permutations(numbers,n) 
                     if is_prime_number(int(''.join(i)))]
    return prime_numbers

def solution(numbers):    
    prime_numbers = []
    for i in range(1,len(numbers)+1):
        """여러 길이의 순열들에서 찾은 소수를 하나의 리스트에 담는 반복문"""
        prime_numbers = prime_numbers + prime_number_permutation(numbers,i)
    prime_numbers = set(prime_numbers) # 중복 제거
    return len(prime_numbers)