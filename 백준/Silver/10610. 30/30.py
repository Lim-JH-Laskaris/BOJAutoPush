n_list = list(map(int,input()))
if 0 not in n_list : print(-1)
elif sum(n_list)%3 != 0 : print(-1)
else : 
    n_list.sort(reverse=True)
    print(''.join(list(map(str,n_list))))