m,n = tuple(map(int,input().split()))

def is_prime_number(number):
    return all(number%j for j in range(2,int(number**.5 +1))) and number>1

prime_numbers = [i for i in range(m,n+1)if is_prime_number(i)]

for i in prime_numbers:
    print(i)