s = input()
while '00' in s:
    s = s.replace('00','0')
while '11' in s:
    s = s.replace('11','1')
s = list(map(int,list(s)))
print(min(sum(s),len(s)-sum(s)))