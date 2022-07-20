def make_set_of_divisor(n):
    divisor_list = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0 :
            divisor_list.append(i)
            divisor_list.append(n//i)
    return set(divisor_list)

def solution(n):
    divisor_list = make_set_of_divisor(n)
    return sum(divisor_list)