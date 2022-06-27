def room_assignment():
    h,w,n = map(int,input().split())
    print(f'{n%h}{n//h+1:0>2d}'if n%h!=0 else f'{h}{n//h:0>2d}')
    
for i in range(int(input())):
    room_assignment()