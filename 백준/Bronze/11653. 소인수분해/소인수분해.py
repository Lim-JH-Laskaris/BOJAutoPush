n = int(input())
d = 2

while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 1
        break
        
while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 2 
if n > 1:
    print(n)
    
    