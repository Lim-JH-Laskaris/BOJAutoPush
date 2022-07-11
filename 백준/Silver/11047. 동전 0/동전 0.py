n, k  = map(int,input().split())
n_list = [int(input()) for i in range(n)]
n_list.sort(reverse=True)
c = 0
for i in n_list:
    if k//i!=0:
        k, c =k%i, c+k//i
print(c)
        