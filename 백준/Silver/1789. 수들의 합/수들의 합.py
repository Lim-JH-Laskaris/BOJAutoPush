s = int(input())
start_point = int((s*2)**.5)-1
answer_list = []
while start_point*(start_point+1)<=s*2:
    answer_list.append(start_point)
    start_point += 1
print(answer_list[-1])
