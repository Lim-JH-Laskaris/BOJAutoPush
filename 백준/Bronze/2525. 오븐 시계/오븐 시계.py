h,m = map(int,input().split())
x = int(input())
y = (h*60+m+x)%(60*24)
h,m = y//60,y%60
print(h,m)