def gcd(x,y):
    """유클리드 호제법. 최대공약수"""
    return gcd(y,x%y) if y else x

def lcm(x,y):
    """두 수의 최소공배수"""
    return x*y//gcd(x,y)

def solution(arr): 
    """누적적으로 lcm을 구하는 함수"""
    return lcm(arr.pop(),solution(arr)) if arr else 1

#제한 사항이 널널하여, 재귀한계 고려없이 코드간결성만 생각하여 작성했습니다.