n = int(input())
def max_univ():
    name,consum ='',0
    for _ in range(int(input())):
        a,b = input().split()
        if consum <= int(b):
            name,consum = a,int(b)
    return name

for _ in range(n):
    print(max_univ())
    