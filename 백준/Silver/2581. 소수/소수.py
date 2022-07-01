def is_prime_number(number):
    return all(number%j for j in range(2,int(number**.5 +1))) and number>1

m,n = int(input()), int(input())
prime_numbers = [i for i in range(m,n+1)if is_prime_number(i)]
if len(prime_numbers)==0: 
    print(-1)
else : 
    print(sum(prime_numbers))
    print(prime_numbers[0])


