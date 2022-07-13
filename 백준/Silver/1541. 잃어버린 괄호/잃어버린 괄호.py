cal_list = [sum(list(map(int,i.split('+')))) for i in input().split('-')]
print(cal_list[0]-sum(cal_list[1:]))