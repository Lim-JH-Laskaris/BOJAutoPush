def replace_to_num(str_):
    if str_ =='(': return 1
    else  : return -1

def is_VPS(ps):
    ps = list(ps)
    ps = list(map(replace_to_num,ps))
    ps = [sum(ps[:i+1])for i in range(len(ps))]
    if min(ps)<0 or ps[-1]!=0 : print('NO')
    else : print('YES')
        
def main():
    for i in range(int(input())):
        is_VPS(input())
    
main()