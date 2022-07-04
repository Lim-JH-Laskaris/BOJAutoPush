def custom_divide(a,b):
    if a%b==0: 
        print(b)
        return custom_divide(a//b,b)
    else :
        return a


def prime_factorization(number):
    prime_number_list = range(2,number+1)
    for i in prime_number_list:
        number = custom_divide(number,i)
        if number == 1 :break
        
prime_factorization(int(input()))