import math 

def cal_peaple_in(k,n):
    return math.prod(range(n,n+k+1))//math.prod(range(1,k+2))

def main():
    for i in range(int(input())):
        k = int(input())
        n = int(input())
        print(cal_peaple_in(k,n))
        
main()