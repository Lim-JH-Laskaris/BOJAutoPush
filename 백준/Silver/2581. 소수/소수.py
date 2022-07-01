m,n = int(input()), int(input())
prime_numbers = [i for i in range(m,n+1)if all(i%j for j in range(2,int(i**.5 +1))) and i>1]
if len(prime_numbers)==0: 
    print(-1)
else : 
    print(sum(prime_numbers))
    print(prime_numbers[0])


