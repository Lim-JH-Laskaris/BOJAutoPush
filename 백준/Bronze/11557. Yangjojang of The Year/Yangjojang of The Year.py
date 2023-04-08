def max_univ_print():
    name,consum ='',0
    for _ in range(int(input())):
        a,b = input().split()
        if consum <= int(b):
            name,consum = a,int(b)
    print(name)

for _ in range(int(input())):
    max_univ_print()
    