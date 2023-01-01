gcd = lambda x,y : y if x%y == 0 else gcd(y,x%y)

def solution(denum1, num1, denum2, num2): 
    denum = denum1*num2+denum2*num1
    num = num1*num2
    gcd_num = gcd(denum,num)
    return [denum//gcd_num,num//gcd_num]