def dp():
    n = int(input())
    s = list(zip(list(map(int,input().split())),
                 list(map(int,input().split()))))
    if n==1 : return max(s[0])
    (a1, b1), (a2, b2) = s[0], s[1]
    (a2, b2) = (a2+b1, b2+a1)
    if n==2 : return max(a2,b2)
    for i in range(2,n):
        (a3, b3) = s[i]
        (a1, b1), (a2, b2) = (a2, b2),(a3+max(b1,b2),b3+max(a1,a2))
    return max(a2,b2)

for _ in range(int(input())):
    print(dp())
    
    
    