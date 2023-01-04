x, y, w, h = tuple(map(int,input().split()))
print(min(x,w-x,y,h-y))
