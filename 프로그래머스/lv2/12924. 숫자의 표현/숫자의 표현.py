def solution(n):
    c = 0
    for i in range(1,n+1):
        if i%2 == 1:
            if n%i==0 and n//i-i//2>0:
                c +=1
        else : 
            if (n+i//2)%i==0 and (n+i//2)//i-i//2>0:
                c +=1
    return c
            