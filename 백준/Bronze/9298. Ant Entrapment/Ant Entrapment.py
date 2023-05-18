def ractangle(dot_list):
    """dot_list list<(x,y)>
    """
    max_x = max(dot_list,key=lambda x:x[0])[0]
    max_y = max(dot_list,key=lambda x:x[1])[1]
    min_x = min(dot_list,key=lambda x:x[0])[0]
    min_y = min(dot_list,key=lambda x:x[1])[1]
    x = max_x-min_x
    y = max_y-min_y
    return x*y,2*(x+y)

n = int(input())
for i in range(n):
    m = int(input())
    dot_list = [list(map(float,input().split())) for j in range(m)]
    a,b = ractangle(dot_list)
    print('Case {0}: Area {1}, Perimeter {2}'.format(i+1,a,b))
