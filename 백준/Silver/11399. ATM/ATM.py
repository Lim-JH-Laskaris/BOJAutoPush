n = int(input())
time_list = list(map(int, input().split()))
time_list.sort(reverse=True)
time_list = [(i+1)*time_list[i] for i in range(n)]
print(sum(time_list))