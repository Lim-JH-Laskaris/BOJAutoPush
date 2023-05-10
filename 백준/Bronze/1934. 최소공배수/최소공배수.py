from math import gcd

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    print(a*b//gcd(a,b))
    