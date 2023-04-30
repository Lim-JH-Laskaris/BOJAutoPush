def gcd(x,y): 
    """유클리드 호제법으로 두 수의 최대공약수 반환"""
    return gcd(y,x%y) if x%y else y

def n_gcd(array):
    """n개의 수의 최대공약수 반환"""
    a = min(array)
    for b in array:
        if a == 1: return 1
        a = min(a,gcd(a,b))
    return a

def find_divisor(a):
    """a의 모든 약수를 set에 담아 반환"""
    divisor = []
    for i in range(1,int(a**.5)):
        if a%i==0:
            divisor.extend(list(set([i,a//i])))
    return divisor

def isnt_divide(a,array):
    """정수a가 array의 모든 수에대해 나머지가 있을때 True 반환"""
    for b in array:
        if b%a==0: return False
    return True

def solution(arrayA, arrayB):
    answer = []
    for i in sorted(find_divisor(n_gcd(arrayA)),reverse=True):
        if isnt_divide(i,arrayB): 
            answer.append(i)
            break
    for i in sorted(find_divisor(n_gcd(arrayB)),reverse=True):
        if isnt_divide(i,arrayA): 
            answer.append(i)
            break
    return max(answer) if answer else 0