from math import gcd
a,b = tuple(map(int,input().split()))
print(a*b//gcd(a,b))