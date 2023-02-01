def solution(number, limit, power):
    """어떤 수 i 의 배수들에 약수 개수를 +1 해주는 방식으로 모든 수들의 약수를 구하고, 
    제한 조건을 적용한 후 합을 구함
    """
    divisor_count_list = [0]*(number+1) 
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            divisor_count_list[j] += 1
    weapon_map = map(lambda x:x if x<=limit else power, divisor_count_list)
    return sum(weapon_map)

"""아래는 이전코드. 한 명 한 명 약수를 구하는 방식으로 함.
def one_weapon(n, limit, power):
    #n의 약수의 개수를 반환. 단, limit초과일 경우 계산을 중단하고 power 반환
    divisor_c = 1
    for i in range(2,n+1):
        if i>n : break
        if n%i!=0 : continue
        c = 0
        while n%i==0: n,c = n//i,c+1
        divisor_c = divisor_c*(c+1) 
        if divisor_c>limit : return power
    return divisor_c
    
def solution(number, limit, power):
    print([one_weapon(n, limit, power) for n in range(1,number+1)])
    return sum([one_weapon(n, limit, power) for n in range(1,number+1)])




"""