def collatz_next(k): # 다음 우박수 리턴 # 단, k=1이면 4 리턴
    if k%2 == 0 : return k//2
    else : return 3*k + 1

def collatz_listing(k): # k가 주어지면 우박수열 리스트 리턴
    collatz_list = [k]
    while k != 1 :
        k = collatz_next(k)
        collatz_list.append(k)
    return collatz_list

def collatz_integral(collatz_list, inte_range): #우박수열과 범위 주어지면 정적분 리턴     
    start, end = inte_range 
    col_li = collatz_list
    end_plus = len(col_li)+end-1
    if   start == end_plus : return  0.0
    elif start >  end_plus : return -1.0
    else : return sum(col_li[start:end_plus+1]) - (col_li[start]+col_li[end_plus])/2
    # 예를들어, (0,a),(1,b),(2,c)의 적분은 (a+b)/2 + (b+c)/2 = a+b+c - (a+c)/2

def solution(k, ranges):
    collatz_list = collatz_listing(k)
    answer = [collatz_integral(collatz_list, inte_range) for inte_range in ranges]
    return answer