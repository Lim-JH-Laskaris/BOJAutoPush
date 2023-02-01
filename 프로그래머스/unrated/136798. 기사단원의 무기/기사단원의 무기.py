def solution(number, limit, power):
    divisor_count_list = [0]*(number+1) 
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            divisor_count_list[j] += 1
    weapon_map = map(lambda x:x if x<=limit else power, divisor_count_list)
    return sum(weapon_map)
