def triangular_number(n):
    return n*(n+1)//2

def approximate_value_of_n(a):
    return int((2*a)**.5)

def find_n(a, n=0):
    while a > triangular_number(n): n += 1
    return n

def make_oblique_line(n):
    if n%2 ==0: return [(i+1,n-i) for i in range(n)]
    else      : return [(n-i,i+1) for i in range(n)]
        #if n==3: [(3,1),(2,2),(1,3)]
        
x = int(input())
n = find_n(x,n=approximate_value_of_n(x))
ol = make_oblique_line(n)
idx = x-triangular_number(n)-1
print('{}/{}'.format(ol[idx][0],ol[idx][1]))
    

