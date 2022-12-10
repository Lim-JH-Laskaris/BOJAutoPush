solution = lambda n : sorted([i for i in range(1,int(n**0.5+1)) if n%i==0 and n//i!=i]+[n//i for i in range(1,int(n**0.5+1)) if n%i==0])
    